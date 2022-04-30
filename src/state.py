from history import History
from parse import Parser

class BotState:
    def __init__(self):
        self.parser = Parser()
        self.cfg_latex = True
        self.global_history = History()