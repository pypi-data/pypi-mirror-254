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
Base Experiment class that handles plotting and controlling the glitcher and target Arduinos.
Do not instanciate/use. Instanciate specific child classes.
"""

########################################################################################################################
#################################################### IMPORTS ###########################################################

from abc import ABC, abstractmethod
from multiprocessing.managers import BaseManager
from multiprocessing import Queue
from threading import Thread, Timer
#from queue import Queue
import datetime
from time import sleep
import logging
from pathlib import Path
from typing import Callable, Any
# Modules to display things in jupyterlab notebook
from IPython.display import display
# Module to create buttons making experiment manipulation easier
import panel as pn
import pandas as pd
import warnings
warnings.simplefilter(action="ignore", category=FutureWarning)

from ..utils.logger import Log
from ..utils.parallel_thread import ParallelThread
from ..utils.mem_managers import MemManagerSer, MemManagerCli

# ##############################################################################################
# ##############################################################################################
# ##############################################################################################

class Experiment(ABC):
    """
    Base Experiment class that handles plotting and controlling the glitcher and target Arduinos.
    Do not instanciate/use. Instanciate specific child classes.
    """

    def __init__(self, log: Log, mem_manager_address=("", 50000)):
        self.log = log

        self.ser_mm = MemManagerSer(address=mem_manager_address, authkey=b"thisisanautkey")
        self.cli_mm = MemManagerCli(address=mem_manager_address, authkey=b"thisisanautkey")

        # Start mem manager server as soon as possible
        self.ser_mm.start()

        # Does it work ? Only connect once until end of program ?
        sleep(1)
        self.cli_mm.connect()
        self.cli_mm.exp_queue = self.cli_mm.get_exp_queue() # pylint: disable=E1101
        self.cli_mm.gui_queue = self.cli_mm.get_gui_queue() # pylint: disable=E1101

        self.mem_manager_cli_thread = Thread(target=self.exp_control_listener_function)
        self.mem_manager_cli_thread.start()

        # Initialization values, should be set before starting an experiment
        self.min_delay  = 0
        self.max_delay  = 1
        self.step_delay = 1
        self.params_initialized = False

        # Parallel processes for the experiment function
        self.glitch_process = None

    def exp_control_listener_function(self):
        while True:
            if not self.cli_mm.exp_queue.empty():
                got = self.cli_mm.exp_queue.get()
                match got:
                    case "exit":
                        break
                    case "start":
                        if self.start_exp():
                            self.cli_mm.gui_queue.put("started")
                        else:
                            self.cli_mm.gui_queue.put("notstarted")
                    case "stop":
                        if self.stop_exp():
                            self.cli_mm.gui_queue.put("stopped")
                        else:
                            self.cli_mm.gui_queue.put("notstopped")
                    case "resume":
                        if self.start_exp():
                            self.cli_mm.gui_queue.put("resumed")
                        else:
                            self.cli_mm.gui_queue.put("notresumed")
                    case other:
                        self.exp_control_extra(other)

    @abstractmethod
    def exp_control_extra(self, cmd: tuple) -> None:
        """
        This function is called at the end of `exp_control_listener_function`
        if the cmd did not match any default behaviour.
        """
        pass

    def stop_mm_server_thread(self):
        self.cli_mm.exp_queue.put("exit")
        self.mem_manager_cli_thread.join()

        self.ser_mm.shutdown()

        self.log.debug("Successfully shutdown all threads")
        return True

    def update_gui(self, *args):
        """
        Method used to push data to plot to a queue shared with the graph plot process.
        Child classes need to implement it.
        """
        self.cli_mm.gui_queue.put(("update_gui", args))

    def clear_graph(self):
        """
        Method should clear the graph and update it's size depending on min/max/step_delays.
        Child classes need to implement it.
        """
        self.cli_mm.gui_queue.put(("clear_graph", datetime.datetime.now()))

    def log_alert(self, md_msg: str, alert_type: str = "info"):
        """
        Appends an alert in the corresponding section of the GUI.

        Args:
            - md_msg: (str) Markdown-formatted message to render in alert.
            - alert_type: (str) See Holoviz Panel lib panel.pane.Alert for reference of possible values.
        """
        self.cli_mm.gui_queue.put(("log_alert", datetime.datetime.now(), md_msg, alert_type))

    def set_experiment_function(self, exp_fn: Callable[[Log, Queue, Any], None], params: list[Any] | None = None):
        if params is not None:
            self.glitch_process = ParallelThread(self.log, exp_fn, *[self, *params])
        else:
            self.glitch_process = ParallelThread(self.log, exp_fn, self)

    def start_exp(self):
        if self.params_initialized and (self.glitch_process is not None):
            self.glitch_process.start()
            return True
        else:
            self.log.critical("Attempted to start experiment without having set parameters with `self.set_delays()` or an experiment fn with `self.set_experiment_function()`. Ignoring.")
            return False

    def stop_exp(self):
        if self.glitch_process is None:
            self.log.critical("Attempted to stop experiment without having set an experiment fn with `self.set_experiment_function()`. Ignoring.")
            return False
        else:
            self.glitch_process.stop()
            return True

    def set_delays(self, min_delay, max_delay, step_delay):
        """
        Set the minimum, maximum, and step delays for the experiment.
        """
        self.min_delay = min_delay
        self.max_delay = max_delay
        self.step_delay = step_delay
        self.cli_mm.gui_queue.put(("delays", [min_delay, max_delay, step_delay]))
        # boolean to make sure params were set at least once before allowing experiment start
        self.params_initialized = True

# ##############################################################################################
# ##############################################################################################
# ##############################################################################################

class ExperimentGUI(ABC):
    """
    Base Experiment class that handles plotting and showing alert logs.
    Do not instanciate/use. Instanciate specific child classes.
    """

    def __init__(self, log: Log, csv_dir: str, mem_manager_address=("", 50000)):
        self.log = log

        self.mm = MemManagerCli(address=mem_manager_address, authkey=b"thisisanautkey")
        self.mm.connect()
        self.mm.exp_queue = self.mm.get_exp_queue() # pylint: disable=E1101
        self.mm.gui_queue = self.mm.get_gui_queue() # pylint: disable=E1101

        self.static_text = pn.widgets.StaticText()
        self.data: pd.DataFrame = pd.DataFrame({})
        self.panel = None

        # These parameters should only be set remotely by the associated experiment class
        self.min_delay  = 0
        self.max_delay  = 1
        self.step_delay = 1

        # Definition of the widget in which messages can be printed (to replace the logger output).
        # A placeholder is created and popped for the purpose of creating an empty log during start-up.
        self.alert_log = pn.Column(pn.pane.Alert("placeholder"))
        self.alert_log.scroll = True # type: ignore
        #self.alert_log.scroll_button_threshold = 200
        self.alert_log.pop(0)

        assert len(csv_dir) >= 1
        csv_dir_slash = "" if (csv_dir[-1] == "/") else "/"
        self.csv_filepath = csv_dir + csv_dir_slash + self.__class__.__name__ + ".csv"

        self.listening_thread = None

    def gui_control_listener_function(self):
        while True:
            if not self.mm.gui_queue.empty():
                #self.log_alert(datetime.datetime.now(), f"GUI queue: {self.cli_queue.qsize()}", alert_type="info")
                got = self.mm.gui_queue.get()
                match got:
                    case "exit":
                        break
                    case "started":
                        timestamp = datetime.datetime.now()
                        self.clear_graph(timestamp)
                        self.log_alert(timestamp, "**Started/Restarted experiment.**", alert_type="info")
                    case "notstarted":
                        self.log_alert(timestamp, "**Failed to start/restart experiment.**", alert_type="warning")
                    case "stopped":
                        self.log_alert(datetime.datetime.now(), "**Stopped experiment.**", alert_type="info")
                    case "notstopped":
                        self.log_alert(timestamp, "**Failed to stop experiment.**", alert_type="warning")
                    case "resumed":
                        self.log_alert(datetime.datetime.now(), "**Resumed experiment.**", alert_type="info")
                    case "notresumed":
                        self.log_alert(timestamp, "**Failed to resume experiment.**", alert_type="warning")
                    case ("update_gui", args):
                        self.update_gui(*args)
                    case ("clear_graph", timestamp):
                        self.clear_graph(timestamp)
                    case ("log_alert", timestamp, md_msg, alert_type):
                        self.log_alert(timestamp, md_msg, alert_type)
                    case ("delays", args):
                        self.set_delays(*args)
                    case other:
                        self.gui_control_extra(other)

    @abstractmethod
    def gui_control_extra(self, cmd: tuple) -> None:
        """
        This function is called at the end of `gui_control_listener_function`
        if the cmd did not match any default behaviour.
        """
        pass

    def set_delays(self, min_delay, max_delay, step_delay):
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

    def stop_gui_control_thread(self):
        if self.listening_thread is not None:
            self.mm.gui_queue.put("exit")
            self.listening_thread.join()

        self.log.debug("Successfully shutdown GUI control thread")
        return True

    @abstractmethod
    def build_gui_panel(self):
        """
        Method that builds and returns the panel that contains an interactive plot. Child classes need to implement it.
        """
        pass

    def load_and_display_gui(self):
        """
        Method that builds and displays the panel in the Jupyterlab Notebook.
        """
        try:
            # Try to resume from last saved data (in csv file)
            self.data = pd.read_csv(self.csv_filepath)
        except (FileNotFoundError, pd.errors.EmptyDataError):
            # If no csv file was found or if it was empty, generate an empty dataframe
            self.data = self.generate_empty_dataframe()
            self.data.to_csv(path_or_buf = self.csv_filepath)

        # Generate panel with current dataframe
        self.panel = self.build_gui_panel()

        # Display panel in Notebook
        display(self.panel)

    @abstractmethod
    def update_gui(self, *args):
        """
        Method used to push data to plot to a queue shared with the graph plot process.
        Child classes need to implement it.
        """
        pass

    def clear_graph(self, timestamp):
        """
        Method should clear the graph and update it's size depending on min/max/step_delays.
        Child classes need to implement it.
        """
        self.data = self.generate_empty_dataframe()
        self.static_text.value = f"last update: {timestamp}"

    def log_alert(self, timestamp, md_msg: str, alert_type: str = "info"):
        """
        Appends an alert in the corresponding section of the GUI.

        Args:
            - md_msg: (str) Markdown-formatted message to render in alert.
            - alert_type: (str) See Holoviz Panel lib panel.pane.Alert for reference of possible values.
        """
        self.alert_log.height = 300
        self.alert_log.styles = {"border-radius": "15px", "padding": "10px", "border": "0.1em solid black"}
        if len(self.alert_log.objects) > 10:
            self.alert_log.pop(-1)
        self.alert_log.insert(0, pn.pane.Alert("*" + str(timestamp) + "* - " + md_msg, alert_type=alert_type))

    def start_gui(self):
        """
        Starts a thread that listens to the remote headless experiment server memory manager.
        Initializes and displays GUI.
        """
        # To prevent panel from showing unnecessary information (because self.log is setup for DEBUG level)
        # (TODO: dirty solution, find alternative; without self.log ?)
        logging.basicConfig()
        logging.getLogger().setLevel(logging.INFO)

        self.listening_thread = Thread(target=self.gui_control_listener_function)
        self.listening_thread.start()

        self.load_and_display_gui()

    @abstractmethod
    def generate_empty_dataframe(self) -> pd.DataFrame:
        """
        Uses the min/max/step_delay attributes to generate an empty dataframe with the correct X axis values.
        """
        pass

    # The next 3 functions are used to handle on_click event of basic start, stop and resume buttons
    def button_start_run(self, _):
        #self.clear_graph()
        #self.log_alert("**Starting/Restarting experiment.**", alert_type="info")
        self.mm.exp_queue.put("start")

    def button_stop_run(self, _):
        #self.log_alert("**Stopping experiment.**", alert_type="info")
        self.mm.exp_queue.put("stop")

    def button_resume_run(self, _):
        #self.log_alert("**Resume experiment.**", alert_type="info")
        self.mm.exp_queue.put("resume")

    def create_start_stop_resume_buttons(self):
        """
        Misc function to generate typical start, stop and resume buttons.

        Returns:
            - tuple of 3 pn.Button
        """
        button_start = pn.widgets.Button(name="Start/Restart experiment", button_type="primary", icon="caret-right", icon_size="1.5em")
        button_stop = pn.widgets.Button(name="Stop experiment", button_type="primary", icon="player-stop-filled", icon_size="1.5em")
        button_resume = pn.widgets.Button(name="Resume experiment", button_type="primary", icon="arrow-forward-up", icon_size="1.5em")

        button_start.on_click(self.button_start_run)
        button_stop.on_click(self.button_stop_run)
        button_resume.on_click(self.button_resume_run)

        return (button_start, button_stop, button_resume)

# ##############################################################################################
# ##############################################################################################
# ##############################################################################################

def should_stop_thread(control_queue: Queue) -> bool:
    if not control_queue.empty():
        return control_queue.get() == "stop"
    return False
