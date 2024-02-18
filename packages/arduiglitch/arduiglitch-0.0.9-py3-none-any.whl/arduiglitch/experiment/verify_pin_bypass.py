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
Experiment child class that handles the admin log-in verification skip experiment.
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

class VerifyPinBypass(Experiment):
    """
    Experiment child class that handles the admin log-in verification skip experiment.
    """
    def exp_control_extra(self, cmd: tuple) -> None:
        pass

class VerifyPinBypassGUI(ExperimentGUI):
    def build_gui_panel(self):
        total_plot = hvplot.bind(lambda _: self.data, self.static_text).interactive().hvplot.bar(
            x="X",
            y=["AA", "Crash"],
            stacked=True,
            cmap=["green", "orange"],
            rot=45,
            width=1200,
            height=400,
            title="Fault injection success and Arduino com crashes"
        )

        (button_start, button_stop, button_resume) = self.create_start_stop_resume_buttons()

        first_app = pn.Column(pn.Row(button_start, button_stop, button_resume), total_plot, self.alert_log)
        return pn.panel (first_app, loading_indicator=True, width=2000)

    def generate_empty_dataframe(self):
        """
        Uses the min/max/step_delay attributes to generate an empty dataframe with the correct X axis values.
        """
        X = np.arange(self.min_delay, self.max_delay, self.step_delay)
        Y = np.zeros((X.shape[0]))

        return pd.DataFrame({
            "X": list(X),
            "AA": list(Y),
            "Crash": list(Y),
        })

    def update_gui(self, delay_i: int, error_type: str = "Crash"):
        self.data.at[delay_i, error_type] += 1
        self.static_text.value = f"last update: {datetime.datetime.now()}"
        # Update data
        self.data.to_csv(path_or_buf = self.csv_filepath)

    def gui_control_extra(self, cmd: tuple) -> None:
        pass
