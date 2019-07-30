"""Effects"""

class FxName:
    """FX name"""

    def __init__(self, name):
        self.name = name


BITCRUSHER = FxName('bitcrusher')
COMPRESSOR = FxName('compressor')
ECHO = FxName('echo')
FLANGER = FxName('flanger')
KRUSH = FxName('krush')
LPF = FxName('lpf')
PAN = FxName('pan')
PANSLICER = FxName('panslicer')
REVERB = FxName('reverb')
SLICER = FxName('slicer')
WOBBLE = FxName('wobble')

Effect_List = [BITCRUSHER, COMPRESSOR, ECHO, FLANGER,
               KRUSH, LPF, PAN, PANSLICER, REVERB,
               SLICER, WOBBLE
              ]
Effect_Dict = {"bitcrusher": BITCRUSHER,
               "compressor": COMPRESSOR,
               "echo": ECHO,
               "flanger": FLANGER,
               "krush": KRUSH,
               "lpf": LPF,
               "pan": PAN,
               "panslicer": PANSLICER,
               "reverb": REVERB,
               "slicer": SLICER,
               "wobble": WOBBLE
               }
