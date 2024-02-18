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
Experiment for the single instruction skip.
"""

import numpy as np
import pandas as pd
import hvplot.pandas
import datetime
from time import sleep
# Module to create buttons making experiment manipulation easier
import panel as pn
import warnings
warnings.simplefilter(action="ignore", category=FutureWarning)

from ..arduino.target import Target
from ..arduino.glitcher import Glitcher
from ..utils.result import Ok, Err
from .experiment import Experiment, ExperimentGUI
from ..utils.logger import Log

class InstructionSkip(Experiment):
    """
    Experiment child class that handles the single instruction skip experiment.
    """
    def __init__(self, log: Log, mem_manager_address=("", 50000)):
        super().__init__(log, mem_manager_address)
        # Reference of was the registers look like after asm code was loaded
        # if no fault was caused.
        self.GOLD_REG = [0x39, 0x38, 0x37, 0x36, 0x35, 0x34, 0x33, 0x32, 0x31, 0x30]

    def send_fault_to_gui(self, delay_i, res_str: str):
        try:
            res = res_str.split(' ')
            for i in range(len(res)):
                if res[i] == "0x55":
                    self.update_gui(delay_i, "reg" + str(i))
                    self.log_alert(f"Detected a correct error : {res} => reg{i}", "info")
        except Exception:
            self.update_gui(delay_i, "Crash")

    def set_glitch_delay(self, delay: int, target: Target, glitcher: Glitcher):
        match glitcher.set_first_glitch_delay(delay):
            case Err(err):
                # If communication with glitcher failed, close both Arduinos and return
                self.log_alert(f"Error during communication with glitcher:\n{err}", alert_type="danger")
                target.close_instrument()
                glitcher.close_instrument()
                exit(-1)

    def get_regs_and_update_graph(self, i: int, target: Target, glitcher: Glitcher):
        match target.get_regs():
            case Ok(regs):
                # If communication was a success, regs is an array of 10 integers
                for reg_i, reg in enumerate(regs):
                    if reg == 0x55:
                        self.update_gui(i, f"reg{reg_i}")
            case Err(err):
                # Reset target Arduino board if communication failed
                self.log_alert(f"Error during communication with target:\n{err}", alert_type="warning")
                self.update_gui(i, "Crash")
                glitcher.reset_target()
                sleep(0.8)

    def exp_control_extra(self, cmd: tuple) -> None:
        pass

class InstructionSkipGUI(ExperimentGUI):
    """
    Experiment child class that handles the instruction skip experiment.
    """
    def __init__(self, log: Log, csv_dir: str, mem_manager_address=("", 50000)):
        super().__init__(log, csv_dir, mem_manager_address)

    def build_gui_panel(self):
        total_plot = hvplot.bind(lambda _: self.data, self.static_text).interactive().hvplot.bar(
            x="X",
            y=["reg0", "reg1", "reg2", "reg3", "reg4", "reg5", "reg6", "reg7", "reg8", "reg9", "Crash"],
            stacked=True,
            cmap=["red", "blue", "green", "yellow", "purple", "cyan", "orange", "pink", "grey", "brown", "olive"],
            rot=45,
            width=1200,
            height=400,
            title="Stacked errors"
        )

        #unique_plots = []
        #for i in range(10):
        #    unique_plots.append((f"reg[{i}]", hvplot.bind(lambda _: self.data, self.static_text).interactive().hvplot.bar(
        #        x="X",
        #        y="reg" + str(i),
        #        color=["red", "blue", "green", "yellow", "purple", "cyan", "orange", "pink", "grey", "brown"][i],
        #        rot=45,
        #        width=1200,
        #        height=400,
        #        title=f"Errors on reg[{i}]"
        #    )))

        plot_tabs = pn.Tabs(("Stacked errors", total_plot))#, *unique_plots)

        (button_start, button_stop, button_resume) = self.create_start_stop_resume_buttons()

        first_app = pn.Column(pn.Row(button_start, button_stop, button_resume), plot_tabs, self.alert_log)
        return pn.panel (first_app, loading_indicator=True, width=2000)

    def generate_empty_dataframe(self):
        """
        Uses the min/max/step_delay attributes to generate an empty dataframe with the correct X axis values.
        """
        X = np.arange(self.min_delay, self.max_delay, self.step_delay)
        Y = np.zeros((X.shape[0]))

        return pd.DataFrame({
            "X": list(X),
            "reg0": list(Y),
            "reg1": list(Y),
            "reg2": list(Y),
            "reg3": list(Y),
            "reg4": list(Y),
            "reg5": list(Y),
            "reg6": list(Y),
            "reg7": list(Y),
            "reg8": list(Y),
            "reg9": list(Y),
            "Crash": list(Y),
        })

    def update_gui(self, delay_i: int, error_type: str = "Crash"):
        self.data.at[delay_i, error_type] += 1
        self.static_text.value = f"last update: {datetime.datetime.now()}"
        # Update data
        self.data.to_csv(path_or_buf = self.csv_filepath)

    def gui_control_extra(self, cmd: tuple) -> None:
        pass
