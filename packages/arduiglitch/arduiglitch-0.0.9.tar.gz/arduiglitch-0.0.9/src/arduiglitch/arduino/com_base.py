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
Base class to create an Arduino serial communication object.
"""

# Built-in modules
from abc import ABC
import time

# Third-party modules
import serial

# Local dependencies
from ..utils.logger import Log
from ..utils.result import Result, Ok, Err
from ..experiment.experiment import Experiment

class ComBase(ABC):
    """
    Base class to create an Arduino serial communication object.
    """

    def __init__(
        self,
        log : Log,
        port : str,
        baudrate: int = 9600,
        timeout_s: float = 0.5,
        experiment: Experiment | None = None
    ):
        """
        The class constructor.

        Args:
            - log: (Log) Log object to use for console logging.
            - port: (str) Com port to use :
                - Windows: "COMx"
                - Linux: "/dev/ttyACMx" or "/dev/ttyUSBx"
            - baudrate: (int) Baudrate to use, usually 9600 or 115200.
            - timeout_s: (float) Serial com timeout in seconds.
            - experiment: (Experiment) Experiment object to use for GUI logging.
        """
        self.log = log

        self.port = port
        self.baud_rate = baudrate
        self.bytesize = "EIGHTBITS"
        self.stopbits = "STOPBITS_ONE"
        self.parity = "PARITY_NONE"
        self.timeout = timeout_s

        self.experiment = experiment

        self.instrument: serial.Serial = serial.Serial()

    def open_instrument(self) -> Result[None]:
        """
        Opens the instrument from the specified self.PORT.

        Returns:
            - result (Result): Ok(None) if success, Err(...) if error.
        """
        kwargs= {
            "port":     self.port,
            "baudrate": self.baud_rate,
            "bytesize": getattr(serial, self.bytesize),
            "stopbits": getattr(serial, self.stopbits),
            "parity":   getattr(serial, self.parity),
            "timeout":  self.timeout
        }

        class_name = self.__class__.__name__
        port = self.port

        if self.instrument.is_open:
            self.log.debug(f"Port `{port}` is already open for {class_name}")
            if self.experiment is not None:
                self.experiment.log_alert(
                    f"**Info** - Port `{port}` of {class_name} already opened",
                    alert_type="info"
                )
            return Ok(None)
        else:
            self.log.debug(f"Opening port for {class_name}: `{port}`")
            if self.experiment is not None:
                self.experiment.log_alert(
                    f"**Info** - Opening port for {class_name}: `{port}`",
                    alert_type="info"
                )
            try:
                self.instrument = serial.Serial(**kwargs)
                time.sleep(1.5)
                self.log.debug(f"...Serial port is open: `{port}`")
                if self.experiment is not None:
                    self.experiment.log_alert(
                        f"**Info** - Serial port is open: `{port}`",
                        alert_type="success"
                    )
                return Ok(None)
            except serial.SerialException as err:
                self.log.debug(f"ERROR : Could not open serial port: {port}")
                if self.experiment is not None:
                    self.experiment.log_alert(
                        f"**Error** - Could not open serial port `{port}`.\nCheck cable or com port name.",
                        alert_type="danger"
                    )
                return Err(err)

    def strict_open_instrument(self) -> Result[None]:
        """
        Opens the instrument. Crashes the program if it could not be opened.

        Returns:
            - result (Result): Ok(None) if success, Err(...) if error.
        """
        match self.open_instrument():
            case Ok(_):
                return Ok(None)
            case _:
                class_name = self.__class__.__name__
                raise RuntimeError(
                    f"Strict open instrument failed for {class_name}"
                )

    def close_instrument(self):
        if self.instrument.is_open:
            self.instrument.close()

    def __del__(self):
        self.close_instrument()

    def _safe_bytes_write(self, cmd: bytes) -> Result[int | None]:
        try:
            return Ok(self.instrument.write(cmd))
        except (serial.SerialException, serial.SerialTimeoutException) as err:
            return Err(err)

    def _safe_write(self, cmd: str) -> Result[int | None]:
        try:
            return self._safe_bytes_write(cmd.encode())
        except (UnicodeEncodeError) as err:
            return Err(err)

    def _safe_bytes_read(self, nb_bytes=100) -> Result[bytes]:
        try:
            return Ok(self.instrument.read(nb_bytes))
        except (serial.SerialException, serial.SerialTimeoutException) as err:
            return Err(err)

    def _safe_read(self, nb_bytes=100) -> Result[str]:
        match self._safe_bytes_read(nb_bytes):
            case Ok(result_bytes):
                try:
                    return Ok(result_bytes.decode())
                except UnicodeDecodeError as err:
                    return Err(err)
            case err:
                return err

    def _safe_write_then_read(
        self,
        cmd: str,
        nb_bytes: int = 100,
        sleep_before_read_s: float = 0.0
    ) -> Result[str]:
        """
        Writes the command to the serial port and then reads a max of
        `nb_bytes` chars of answer.
        Returns a Result type alias to propagate errors.

        Args:
            - cmd: (str) Command to write to the serial port.
            - nb_bytes: (int) Max number of bytes to read from the serial port.
            - sleep_before_read_s: (float) Number of seconds to wait before
              reading an answer from the serial port.
        """
        match self._safe_write(cmd):
            case Ok(_):
                time.sleep(sleep_before_read_s)
                return self._safe_read(nb_bytes)
            case err:
                return err

    def _safe_write_then_bytes_read(
        self,
        cmd: str,
        nb_bytes: int = 100,
        sleep_before_read_s: float = 0.0
    ) -> Result[bytes]:
        """
        Writes the command to the serial port and then reads a max of
        `nb_bytes` chars of answer.
        Returns a Result type alias to propagate errors.

        Args:
            - cmd: (str) Command to write to the serial port.
            - nb_bytes: (int) Max number of bytes to read from the serial port.
            - sleep_before_read_s: (float) Number of seconds to wait before
              reading an answer from the serial port.
        """
        match self._safe_write(cmd):
            case Ok(_):
                time.sleep(sleep_before_read_s)
                return self._safe_bytes_read(nb_bytes)
            case err:
                return err

    def _safe_bytes_write_then_read(
        self,
        cmd: bytes,
        nb_bytes: int = 100,
        sleep_before_read_s: float = 0.0
    ) -> Result[str]:
        """
        Writes the command to the serial port and then reads a max of
        `nb_bytes` chars of answer.
        Returns a Result type alias to propagate errors.

        Args:
            - cmd: (str) Command to write to the serial port.
            - nb_bytes: (int) Max number of bytes to read from the serial port.
            - sleep_before_read_s: (float) Number of seconds to wait before
              reading an answer from the serial port.
        """
        match self._safe_bytes_write(cmd):
            case Ok(_):
                time.sleep(sleep_before_read_s)
                return self._safe_read(nb_bytes)
            case err:
                return err

    def _safe_bytes_write_then_bytes_read(
        self,
        cmd: bytes,
        nb_bytes: int = 100,
        sleep_before_read_s: float = 0.0
    ) -> Result[bytes]:
        """
        Writes the command to the serial port and then reads a max of
        `nb_bytes` chars of answer.
        Returns a Result type alias to propagate errors.

        Args:
            - cmd: (str) Command to write to the serial port.
            - nb_bytes: (int) Max number of bytes to read from the serial port.
            - sleep_before_read_s: (float) Number of seconds to wait before
              reading an answer from the serial port.
        """
        match self._safe_bytes_write(cmd):
            case Ok(_):
                time.sleep(sleep_before_read_s)
                return self._safe_bytes_read(nb_bytes)
            case err:
                return err

    def _safe_write_then_readline(
        self,
        cmd: str,
        sleep_before_read_s: float = 0.0
    ) -> Result[str]:
        """
        Writes the command to the serial port and then reads the line answered.
        Return a Result type alias to propagate errors.

        Args:
            - cmd: (str) Command to write to the serial port.
            - sleep_before_read_s: (float) Number of seconds to wait before
              reading an answer from the serial port.
        """
        match self._safe_write(cmd):
            case Ok(_):
                time.sleep(sleep_before_read_s)
                return self._safe_readline()
            case err:
                return err

    def _safe_readline(self) -> Result[str]:
        """
        Reads and decodes a line from the instrument. Catches serial
        exceptions in the returned Result.
        """
        try:
            return Ok(self.instrument.readline().decode())
        except (
            serial.SerialException,
            serial.SerialTimeoutException,
            UnicodeDecodeError
        ) as err:
            return Err(err)

    def _safe_instrument_reset_input_buffer(self) -> Result[None]:
        """
        Resets the input buffer of the instrument. Catches serial
        exceptions in the returned Result.
        """
        try:
            self.instrument.reset_input_buffer()
            return Ok(None)
        except serial.SerialException:
            return Err(Exception("Instrument is not open"))
