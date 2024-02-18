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
This file contains a pair of class that inherits from multiprocessing's
BaseManager to handle shared queues between multiple processes/machines.
"""

from multiprocessing.managers import BaseManager
from multiprocessing import Queue

class MemManagerSer(BaseManager):
    """
    This class should be used as the server that listens to clients.

    """
    def __init__(self, address=("", 50000), authkey=b"thisisanautkey"):
        super().__init__(address=address, authkey=authkey)
        self._exp_queue: Queue = Queue()
        self._gui_queue: Queue = Queue()

        MemManagerSer.register("get_exp_queue", lambda: self._exp_queue)
        MemManagerSer.register("get_gui_queue", lambda: self._gui_queue)

class MemManagerCli(BaseManager):
    def __init__(self, address=("", 50000), authkey=b"thisisanautkey"):
        super().__init__(address=address, authkey=authkey)
        self.exp_queue = None
        self.gui_queue = None

        MemManagerCli.register("get_exp_queue")
        MemManagerCli.register("get_gui_queue")
