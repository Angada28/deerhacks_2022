
from typing import Dict

class HistoryException(Exception):
    pass

class History:
    channel_hist: Dict
    def __init__(self):
        self.channel_hist = {}
    
    def register_command(self, channel, msg, ans):
        self.channel_hist.setdefault(channel, []).append((msg, ans))

    def last(self, channel, idx):
        try:
            return self.channel_hist[channel][idx]
        except IndexError:
            raise HistoryException("Invalid index... I probably can't remember that far back")
