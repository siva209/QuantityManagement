class Inch:

    def __init__(self, inch):
        self.inch = inch

    def __eq__(self, other):
        if isinstance(other, Inch):
            if self.inch == other.inch:
                return True
        return False