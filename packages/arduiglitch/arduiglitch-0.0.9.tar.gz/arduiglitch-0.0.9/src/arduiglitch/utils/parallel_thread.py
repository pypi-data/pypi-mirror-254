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
This class enables the definition of a function in a Jupyter Notebook that
is then executed in a separate thread. The goal is to hide as much
complexity from the user of the Notebook as possible.

The function passed as argument needs to contain some mendatory arguments,
but might use more. The function prototype needs to look as follows:

```python
def my_experiment(log: .logger.Log, queue: multiprocessing.Queue, *args) -> None
```
"""

import time
from threading import Thread as Process
from queue import Queue
from typing import Callable, Any
from .logger import Log


class ParallelThread:
    """
    This class enables the definition of a function in a Jupyter Notebook that
    is then executed in a separate thread. The goal is to hide as much
    complexity from the user of the Notebook as possible.

    The function passed as argument needs to contain some mendatory arguments,
    but might use more. The function prototype needs to look as follows:

    ```python
    def my_experiment(log: .logger.Log, queue: multiprocessing.Queue, *args) -> None
    ```
    """
    def __init__(
        self,
        log: Log,
        function: Callable[[Log, Queue, Any], None],
        *args
    ):
        self.function = function # needs to look like `function(log, control_queue, *args) -> None`
        self.args = args
        self.log = log

        self.process = None
        self.queue = Queue()

    def start(self):
        if (self.process is None) or (not self.process.is_alive()):
            self.process = Process(target=self._thread_fn, name="process", args=(self.log, self.queue, self.args))
            self.process.start()
            self.log.debug(f"Started thread `{self.process.name}`")
        else:
            self.log.critical("Tried to start running thread. Ignoring.")

    def stop(self):
        if (self.process is not None) and (self.process.is_alive()):
            self.queue.put("stop")
            self.process.join()
            self.log.debug("Thread stopped")
        else:
            self.log.critical("Tried to stop unstarted thread. Ignoring.")

    def _thread_fn(self, log, control_queue: Queue, args):
        # Start of thread
        self.log.debug(f"Start of thread; {time.time()}")

        self.function(log, control_queue, *args)

        self.log.debug(f"End of thread; {time.time()}")
