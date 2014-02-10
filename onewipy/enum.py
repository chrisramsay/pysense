"""
Sets up a 'java' style enum
"""


class Enum(set):

    def __getattr__(self, name):
        if name in self:
            return name
        raise AttributeError


SENS_TYPES = Enum(['TempContact', 'TempIR'])
SENS_STATES = Enum(['YES'])
