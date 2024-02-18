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
Experiment child class that handles the PIN log-in max attempt protection skip experiment.
"""

import os
import numpy as np
import pandas as pd
import hvplot.pandas
import datetime
import binascii
# Module to create buttons making experiment manipulation easier
import panel as pn
import warnings
warnings.simplefilter(action="ignore", category=FutureWarning)
from IPython.display import display

from .experiment import Experiment, ExperimentGUI
from ..utils.logger import Log
from ..arduino.target import Target
from ..utils.result import Result, Ok, Err
from ..utils.pfa_utils import PfaUtils

class SBoxFault(Experiment):
    """
    Experiment child class that handles the PIN log-in max attempt protection skip experiment.
    """
    def __init__(self, log: Log, mem_manager_address=("", 50000)):
        super().__init__(log, mem_manager_address)

        self.pfa = PfaUtils()

    def was_sbox_faulted(self, target: Target, healthy_plain_cipher_vectors: list[tuple[bytes, bytes]]) -> Result[bool]:
        """
        The purpose of this method is to detect when the SBOX was successfully faulted.
        One way of doing this would be to directly ask the target what the SBOX stored in SRAM is, but
        it requires cooperation with the target which we'd like to avoid for this experiment.
        Thus this method makes the hypothesis that a cipher error implies a successful error on the SBOX storage in SRAM.

        Args:
            - target: (ArduinoFormationFaults) Opened serial com with target Arduino board.
            - healthy_plain_cipher_vectors: (list[tuple[bytes, bytes]]) List of tuples (plain, cipher) generated with an unfaulted target.

        Returns:
            - (bool) Returns Ok(True) when the ref cipher and the received cipher do not match, Ok(False) if they all matched
        """

        # Set plaintext, encrypt and get cipher result
        for (plain, ref_cipher) in healthy_plain_cipher_vectors:
            match target.encrypt_aes128(plain):
                case Ok(cipher):
                    # Check if cipher is different from reference cipher
                    if ref_cipher != cipher:
                        # Only one unmatching cipher is required to detect a faulted SBOX
                        self.log.debug(
                            "At least one test vector failed, assuming that SBOX was successfully faulted.\n"
                            + "ref_cipher = " + str(binascii.hexlify(ref_cipher)) + "\n"
                            + "cipher     = " + str(binascii.hexlify(cipher))
                        )
                        #self.log_alert(f"At least one test vector failed, assuming that SBOX was successfully faulted.\n{ref_cipher=}\n{cipher=}", "success")
                        return Ok(True)
                case Err(err):
                    return Err(err)
        # If all test vectors passed, assume that SBOX was not faulted
        return Ok(False)

    def format_sbox_diff(self, sbox: list[int]):
        """
        Prints the differences between the reference SBOX and the argument SBOX as a markdown table.

        Args:
            - sbox: (list[int]) SBOX to compare with the reference SBOX.
        """
        message = "Diff:\n"
        nb_lines = 0
        for i in range(64):
            line = ""
            for j in range(4):
                index = i * 4 + j
                if sbox[index] != self.pfa.ref_sbox[index]:
                    line += f"[{index}]: {hex(self.pfa.ref_sbox[index])}->{hex(sbox[index])}\t\t|"
                else:
                    line += f"[{index}]: {hex(sbox[index])}\t\t\t|"

            # Only add line to output message if it contains an error
            if line.find("->") != -1:
                line = "\n|" + line
                nb_lines += 1
            else:
                line = ""
            message += line
            if nb_lines >= 4:
                message += "\n..."
                break
        return message

    def is_mono_byte_fault(self, sbox: list[int]) -> bool:
        """
        Return True when only one byte differs between argument sbox and reference sbox.
        """
        faulted = False
        for i in range(256):
            if sbox[i] != self.pfa.ref_sbox[i]:
                if faulted:
                    return False
                faulted = True
        return faulted

    def cheat_verify_mono_byte_sbox_fault(self, target: Target) -> bool:
        """
        The goal of this method is to directly ask the SBOX to the target to confirm or reject the mono-byte error hypothesis.
        This is relevent in the context of a training so as to prevent the trainee to proceed to the next step with a wrong error injection.
        In a real scenario, the PFA algorithm would converge to a number of possible keys higher than one, wich would enable a rejection of the
        mono-byte error hypothesis.
        """
        match target.sbox():
            case Ok(sbox_b):
                sbox = list(sbox_b)
                self.log.debug(self.format_sbox_diff(sbox))
                #self.log_alert(self.format_sbox_diff(sbox), "info")
                if self.is_mono_byte_fault(sbox):
                    self.log.debug("Verification system confirmed mono-byte fault on SBOX. Thread stopped.")
                    #self.log_alert("Verification system confirmed mono-byte fault on SBOX. Thread stopped.", "success")
                    return True
                else:
                    self.log.debug("Verification system did not confirm mono-byte fault: either something else was faulted or more than one SBOX byte.")
                    #self.log_alert("Verification system did not confirm mono-byte fault: either something else was faulted or more than one SBOX byte.", "warning")
                    return False
            case err:
                self.log.critical(f"Failed to read SBOX: {err}")
                #self.log_alert(f"Failed to read SBOX: {err}", "warning")
                return False

    def exp_control_extra(self, cmd: tuple) -> None:
        pass

class SBoxFaultGUI(ExperimentGUI):
    def build_gui_panel(self):
        total_plot = hvplot.bind(lambda _: self.data, self.static_text).interactive().hvplot.bar(
            x="X",
            y=["SBOX changed", "Crash"],
            stacked=True,
            cmap=["green", "orange"],
            rot=45,
            width=1200,
            height=400,
            title="Fault injection success and Arduino com crashes"
        )

        (button_start, button_stop, button_resume) = self.create_start_stop_resume_buttons()

        first_app = pn.Column(pn.Row(button_start, button_stop, button_resume), total_plot, self.alert_log)

        return pn.panel(first_app, loading_indicator=True, width=2000)

    def generate_empty_dataframe(self):
        """
        Uses the min/max/step_delay attributes to generate an empty dataframe with the correct X axis values.
        """
        x = np.arange(self.min_delay, self.max_delay, self.step_delay)
        y = np.zeros((x.shape[0]))

        return pd.DataFrame({
            "X": list(x),
            "SBOX changed": list(y),
            "Crash": list(y),
        })

    def update_gui(self, delay_i: int, error_type: str = "Crash"):
        self.data.at[delay_i, error_type] += 1
        self.static_text.value = f"last update: {datetime.datetime.now()}"
        # Update data
        self.data.to_csv(path_or_buf = self.csv_filepath)

    def gui_control_extra(self, cmd: tuple) -> None:
        pass

# =====================================================================================================================

def generate_pairs(length: int, log: Log, target: Target) -> list[tuple[bytes, bytes]]:
    pairs: list[tuple[bytes, bytes]] = []

    for _ in range(length):
        plaintext = os.urandom(16)
        match target.encrypt_aes128(plaintext):
            case Ok(ciphertext):
                pairs.append((plaintext, ciphertext))
            case Err(err):
                log.error(f"Error while generating a healthy plain/cipher pairs: {err}")

    log.info(f"Successfully created {len(pairs)} healthy plain/cipher pairs.")
    return pairs

def show_generate_pairs_button(length: int, log: Log, target: Target, vectors: list[tuple[bytes, bytes]]):
    # Empty list without losing reference
    for _ in range(len(vectors)):
        vectors.pop()

    button_start = pn.widgets.Button(name="Generate healthy vectors", button_type="primary", icon="caret-right", icon_size="1.5em")
    def on_button_start_click(_, length, log, target, vectors):
        # Generate 10 healthy plain/cipher pairs with the target
        vectors += generate_pairs(length, log, target)
    button_start.on_click(lambda event: on_button_start_click(event, length, log, target, vectors))
    display(pn.Column(button_start))
