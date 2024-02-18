# Arduiglitch - voltage glitch training on an ATMega328P
# Copyright (C) 2024  Hugo PERRIN (h.perrin@emse.fr)

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
Experiment child class that handles computing the key from ciphers under a single faulted byte hypothesis.
"""

import numpy as np
import pandas as pd
import hvplot.pandas
import datetime
import os
import binascii
from queue import Queue
# Module to create buttons making experiment manipulation easier
import panel as pn
import warnings
warnings.simplefilter(action="ignore", category=FutureWarning)

from .experiment import Experiment, ExperimentGUI, should_stop_thread
from ..utils.logger import Log
from ..arduino.target import Target
from ..utils.result import Result, Ok, Err
from ..utils.pfa_utils import PfaUtils

class Pfa(Experiment):
    """
    Experiment child class that handles computing the key from ciphers under a single faulted byte hypothesis.
    """
    def __init__(
        self,
        log: Log,
        max_batches: int,
        batch_size: int,
        mem_manager_address=("", 50000)
    ):
        super().__init__(log, mem_manager_address)

        self.MAX_BATCHES = max_batches
        self.BATCH_SIZE = batch_size

        # Useless for this experiment but needs to be called for an initialization
        # flag to be set in the parent class.
        self.set_delays(0, 0, 0)

        self.pfa = PfaUtils()

    def generate_test_vectors(self, target: Target, p_key: bytes) -> Result[bytes]:
        """
        Generates a test vector and returns it as a tuple (key, plain, ref_cipher, rec_cipher).
        """
        # First step, generate a random pair of (key, plain) with their associated reference cipher
        (key, plain, _) = self.pfa.generate_sim_vectors(p_key)

        # Second step, perform an encryption with the test vector
        target.set_user_pin(1972)
        target.verifypin()
        target.key_aes128(key)
        match target.encrypt_aes128(plain):
            case Ok(rec_cipher):
                # Third step, store the test tuple for later analysis
                return Ok(rec_cipher)
            case err:
                return err

    def set_progress(self, value: int):
        self.cli_mm.gui_queue.put(("set_progress", value))

    def exp_control_extra(self, cmd: tuple) -> None:
        pass

class PfaGUI(ExperimentGUI):
    def __init__(
        self,
        log: Log,
        max_batches: int,
        batch_size: int,
        csv_dir: str = "./csv/",
        mem_manager_address=("", 50000)
    ):
        super().__init__(log, csv_dir, mem_manager_address)

        self.MAX_BATCHES = max_batches
        self.BATCH_SIZE = batch_size

        self.progress: pn.indicators.Progress | None = None

    def build_gui_panel(self):
        pfa_plot = hvplot.bind(lambda _: self.data, self.static_text).interactive().hvplot.line(
            x="Somme cumulée des chiffrés analysés",
            y="Log 10 du nombre de clés possibles restantes",
            width=1200,
            height=400,
            title="Logarithme du nombre de clés possibles restantes en fonction du nombre de textes chiffrés analysés"
        )

        if self.progress is None:
            self.progress = pn.indicators.Progress(
                name="Progress",
                value=0,
                width=1200
            )

        (button_start, button_stop, button_resume) = self.create_start_stop_resume_buttons()

        first_app = pn.Column(pn.Row(button_start, button_stop, button_resume), pfa_plot, self.progress, self.alert_log)

        return pn.panel(first_app, loading_indicator=True, width=2000)

    def generate_empty_dataframe(self):
        """
        Uses the min/max/step_delay attributes to generate an empty dataframe with the correct X axis values.
        """
        x_number_of_tests = np.arange(0, self.MAX_BATCHES * self.BATCH_SIZE, self.BATCH_SIZE)
        y_number_possible_keys = np.zeros((x_number_of_tests.shape[0]))


        return pd.DataFrame({
            "Log 10 du nombre de clés possibles restantes": list(y_number_possible_keys),
            "Somme cumulée des chiffrés analysés": list(x_number_of_tests),
        })

    def set_progress(self, value: int):
        if self.progress is not None:
            self.progress.value = value

    def update_gui(self, iteration_i: int, value):
        self.data.at[iteration_i, "Log 10 du nombre de clés possibles restantes"] = value
        self.static_text.value = f"last update: {datetime.datetime.now()}"
        # Update data
        self.data.to_csv(path_or_buf = self.csv_filepath)

    def gui_control_extra(self, cmd: tuple) -> None:
        match cmd:
            case ("set_progress", progress):
                self.set_progress(progress)

# =====================================================================================================================

def glitch_function_pfa(log: Log, control_queue: Queue, exp: Pfa, target: Target):
    """
    Glitch function called in a separate thread by the ExperimentPFA experiment.
    """

    # Loading progress bar
    exp.set_progress(-1)
    exp.log_alert("**Success** - Experiment started...", alert_type="success")

    # ====================================================================================================================
    # ================================================== EXPERIMENT ======================================================
    counts = np.zeros((16, 256), dtype=np.uint64)
    all_ciphers: list[np.ndarray] = []
    possible_keys = 100000 # placeholder definition value
    raw_guess = b""

    while possible_keys > 1:
        # Regularily check if thread needs to be interrupted
        if should_stop_thread(control_queue):
                exp.log_alert("**Success** - Experiment interrupted.", alert_type="success")
                return None

        # Generate a batch of new test vectors
        ciphers_batch = []
        exp.log_alert(f"Generating {len(all_ciphers)//exp.BATCH_SIZE}th batch of {exp.BATCH_SIZE} vectors...")

        while len(ciphers_batch) < exp.BATCH_SIZE:
            # Generate a random plain text
            plain = os.urandom(16)
            # Encrypt it with the target
            match target.encrypt_aes128(plain):
                case Ok(cipher):
                    # Append it to vector lists
                    ciphers_batch.append(cipher)
                    all_ciphers.append(
                        np.array(list(cipher)
                        ).reshape((4, 4)
                        ).astype(np.uint8)
                    )
                case Err(err):
                    exp.log_alert(f"Failed to encrypt plain text: {err}", "warning")


        # Analyse vectors with PFA algorithm
        exp.log_alert("Analyzing batch...")
        (possible_keys, raw_guess, _) = exp.pfa.pfa(ciphers_batch, counts)
        # Not a percent per say but serves its purpose
        log_possible_keys = np.log10(float(possible_keys))
        exp.set_progress(max(0, 40 - int(max(1.0, log_possible_keys))) * 100 // 40)
        exp.update_gui(len(all_ciphers)//exp.BATCH_SIZE, log_possible_keys)

    exp.set_progress(-1)

    # Try to guess the key
    (err_i, fault) = exp.pfa.find_right_key_hypothesis(raw_guess, np.array(all_ciphers))
    if err_i != -1:
        # Hypothesis was valid SB'[i] is the faulted byte, thus SB[i] is indeed the missing byte
        exp.log_alert(f"Error position detected at : {err_i}\nMissing byte: {hex(exp.pfa.ref_sbox[err_i])}\nOverpresent byte: {hex(fault)}")

        # The computed key is for j in [0; 16]: K_j = C_j^min xor SB[i]
        guessed_key = bytes([guess_byte ^ exp.pfa.ref_sbox[err_i] for guess_byte in raw_guess])
        final_key_guess_h = binascii.hexlify(exp.pfa.inverse_key_expansion(guessed_key, np.uint8(fault), err_i)[0])

        exp.log_alert(f"*Key guess: {final_key_guess_h}*", "success")
    else:
        exp.log_alert("*Could not find a satisfying SBOX error position hypothesis*", "danger")

    # End of thread
    exp.set_progress(100)
    exp.log_alert("End of thread.", "success")
    # ====================================================================================================================
    # ====================================================================================================================
