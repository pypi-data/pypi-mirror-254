import time
from datetime import datetime
from types import SimpleNamespace

class Schedule:
    now: bool   # can be removed in future
    timestamp: int

    def __init__(self, data):
        
        if type(data) is dict:
            self.now = data["now"]        

            if self.now:
                self.timestamp = int(time.time())

            else:
                _datetime = datetime.fromisoformat(data["datetime"])
                self.timestamp = int(datetime.timestamp(_datetime))

        if type(data) is SimpleNamespace:
            self.now = data.now
            self.timestamp = data.timestamp