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
Experiment child class that handles the duplicate register instruction skip experiment.
"""

import numpy as np
import pandas as pd
import hvplot.pandas
import datetime
# Module to create buttons making experiment manipulation easier
import panel as pn
import warnings
warnings.simplefilter(action="ignore", category=FutureWarning)

from .experiment import Experiment, ExperimentGUI
from ..utils.logger import Log

class DoubleInstructionSkip(Experiment):
    """
    Experiment child class that handles the duplicate register instruction skip experiment.
    """
    def __init__(self, log: Log, mem_manager_address=("", 50000)):
        super().__init__(log, mem_manager_address)
        # Initialization values, should be set before starting an experiment
        self.min_delay1 = 0
        self.max_delay1 = 1
        self.step_delay1 = 1

    def set_delays(self, min_delay, max_delay, step_delay, min_delay1, max_delay1, step_delay1):
        """
        Overrides the method defined in the inherited class to handle more params.
        """
        self.min_delay = min_delay
        self.max_delay = max_delay
        self.step_delay = step_delay
        self.min_delay1 = min_delay1
        self.max_delay1 = max_delay1
        self.step_delay1 = step_delay1
        self.cli_mm.gui_queue.put(("delays", [
            min_delay,
            max_delay,
            step_delay,
            min_delay1,
            max_delay1,
            step_delay1
        ]))
        # boolean to make sure params were set at least once before allowing experiment start
        self.params_initialized = True

    def exp_control_extra(self, cmd: tuple) -> None:
        pass


class DoubleInstructionSkipGUI(ExperimentGUI):
    def __init__(self, log: Log, csv_dir: str = "./csv/", mem_manager_address=("", 50000)):
        super().__init__(log, csv_dir, mem_manager_address)
        # Initialization values, should be set before starting an experiment
        self.min_delay1 = 0
        self.max_delay1 = 1
        self.step_delay1 = 1

    def build_gui_panel(self):
        errors_plot = hvplot.bind(lambda _: self.data, self.static_text).interactive().hvplot.heatmap(
            x="Delay first glitch",
            y="Delay second glitch",
            C="errors",
            title="Successful errors depending on the delays",
            rot=45,
            xaxis="top",
            width=600,
            height=400,
            #toolbar=None,
            fontsize={"title": 10, "xticks": 8, "yticks": 8}
        ).opts(default_tools = ["save"])

        crashes_plot = hvplot.bind(lambda _: self.data, self.static_text).interactive().hvplot.heatmap(
            x="Delay first glitch",
            y="Delay second glitch",
            C="Crash",
            title="Target com crashes depending on the delays",
            rot=45,
            xaxis="top",
            width=600,
            height=400,
            #toolbar=None,
            fontsize={"title": 10, "xticks": 8, "yticks": 8}
        ).opts(default_tools = ["save"])

        (button_start, button_stop, button_resume) = self.create_start_stop_resume_buttons()

        first_app = pn.Column(pn.Row(button_start, button_stop, button_resume), pn.Row(errors_plot, crashes_plot), self.alert_log)
        return pn.panel (first_app, loading_indicator=True, width=2000)

    def generate_empty_dataframe(self):
        """
        Uses the min/max/step_delay attributes to generate an empty dataframe with the correct X axis values.
        """
        delays0 = np.arange(self.min_delay, self.max_delay, self.step_delay)
        delays1 = np.arange(self.min_delay1, self.max_delay1, self.step_delay1)

        errors = np.zeros((len(delays0) * len(delays1)))
        bad_responses = np.zeros((len(delays0) * len(delays1)))

        index = pd.MultiIndex.from_product([list(delays0), list(delays1)], names=["Delay first glitch", "Delay second glitch"])
        return pd.DataFrame({
            "errors": list(errors),
            "Crash": list(bad_responses)
        }, index=index)

    def update_gui(self, delay0: int, delay1: int, error_type: str = "Crash"):
        self.data.at[(delay0, delay1), error_type] += 1
        self.static_text.value = f"last update: {datetime.datetime.now()}"
        # Update data
        self.data.to_csv(path_or_buf = self.csv_filepath)

    def set_delays(self, min_delay, max_delay, step_delay, min_delay1, max_delay1, step_delay1):
        """
        Set the GUI-scoped minimum, maximum, and step delays for the experiment.
        SHOULD NOT BE CALLED BY THE USER, ONLY BY `gui_control_listener_function`.
        Can be redefined in child classes to implement more parameters. In such
        case, the associated experiment child class needs to put all the params
        in the queue when sending delays to update GUI.
        """
        self.min_delay = min_delay
        self.max_delay = max_delay
        self.step_delay = step_delay
        self.min_delay1 = min_delay1
        self.max_delay1 = max_delay1
        self.step_delay1 = step_delay1

    def gui_control_extra(self, cmd: tuple) -> None:
        pass
