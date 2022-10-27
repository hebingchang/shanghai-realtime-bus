class LineSequence:
    direction: bool
    info: bool
    line: str
    sequence: int

    def __init__(self, line: str, sequence: int = 0, direction: bool = False, info: bool = False):
        self.direction = direction
        self.info = info
        self.line = line
        self.sequence = sequence
