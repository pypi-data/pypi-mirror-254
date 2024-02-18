
def test_threads():
    from time import sleep
    from arduiglitch.logger import Log
    from arduiglitch.experiment import should_stop_thread
    from arduiglitch.experiment_instruction_skip import ExperimentInstructionSkip, ExperimentInstructionSkipGUI
    from arduiglitch.arduino_formation_faults import ArduinoFormationFaults
    from arduiglitch.arduino_glitcher import ArduinoGlitcher
    from arduiglitch.arduino_com_result import Ok, Err

    # Define serial communication parameters for the two Arduino boards
    port_target = "/dev/ttyACM0"
    port_glitcher = "/dev/ttyACM1"
    baudrate = 115200
    timeout_target = 1.0
    timeout_glitcher = 0.2
    # Instantiate the logging tool
    user_log = Log("tests/logger_config.yml")
    # Instantiate the experiment handler that will run both the graph and serial communication processes
    experiment = ExperimentInstructionSkip(user_log)
    experiment_gui = ExperimentInstructionSkipGUI(user_log, "./tests/csv/")
    #gui = ExperimentInstructionSkipGUI()
    sleep(5)

    user_log.debug("TEST - Stopping threads")

    assert experiment_gui.stop_gui_control_thread()
    assert experiment.stop_mm_server_thread()
