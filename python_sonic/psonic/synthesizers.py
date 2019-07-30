"""Synthesizer"""

class Synth:
    """Synthesizer"""

    def __init__(self, name):
        self.name = name

DULL_BELL = Synth('dull_bell')
PRETTY_BELL = Synth('pretty_bell')
SINE = Synth('sine')
SQUARE = Synth('square')
PULSE = Synth('pulse')
SUBPULSE = Synth('subpulse')
DTRI = Synth('dtri')
DPULSE = Synth('dpulse')
FM = Synth('fm')
MOD_FM = Synth('mod_fm')
MOD_SAW = Synth('mod_saw')
MOD_DSAW = Synth('mod_dsaw')
MOD_SINE = Synth('mod_sine')
MOD_TRI = Synth('mod_tri')
MOD_PULSE = Synth('mod_pulse')
SUPERSAW = Synth('supersaw')
HOOVER = Synth('hoover')
SYNTH_VIOLIN = Synth('synth_violin')
PLUCK = Synth('pluck')
PIANO = Synth('piano')
GROWL = Synth('growl')
DARK_AMBIENCE = Synth('dark_ambience')
DARK_SEA_HORN = Synth('dark_sea_horn')
HOLLOW = Synth('hollow')
ZAWA = Synth('zawa')
NOISE = Synth('noise')
GNOISE = Synth('gnoise')
BNOISE = Synth('bnoise')
CNOISE = Synth('cnoise')
DSAW = Synth('dsaw')
TB303 = Synth('tb303')
BLADE = Synth('blade')
PROPHET = Synth('prophet')
SAW = Synth('saw')
BEEP = Synth('beep')
TRI = Synth('tri')
CHIPLEAD = Synth('chiplead') # Sonic Pi 2.10
CHIPBASS = Synth('chipbass')
CHIPNOISE = Synth('chipnoise')
TECHSAWS = Synth('tech_saws')  # Sonic Pi 2.11
SOUND_IN = Synth('sound_in')
SOUND_IN_STEREO = Synth('sound_in_stereo')

Synth_Dict = {'dull_bell': DULL_BELL,
'pretty_bell': PRETTY_BELL,
'sine': SINE,
'square': SQUARE,
'pulse': PULSE,
'subpulse': SUBPULSE,
'dtri': DTRI,
'dpulse': DPULSE,
'fm': FM,
'mod_fm': MOD_FM,
'mod_saw': MOD_SAW,
'mod_dsaw': MOD_DSAW,
'mod_sine': MOD_SINE,
'mod_tri': MOD_TRI,
'mod_pulse': MOD_PULSE,
'supersaw': SUPERSAW,
'hoover': HOOVER,
'synth_violin': SYNTH_VIOLIN,
'pluck': PLUCK,
'piano': PIANO,
'growl': GROWL,
'dark_ambience': DARK_AMBIENCE,
'dark_sea_horn': DARK_SEA_HORN,
'hollow': HOLLOW,
'zawa': ZAWA,
'noise': NOISE,
'gnoise': GNOISE,
'bnoise': BNOISE,
'cnoise': CNOISE,
'dsaw': DSAW,
'tb303': TB303,
'blade': BLADE,
'prophet': PROPHET,
'saw': SAW,
'beep': BEEP,
'tri': TRI,
'chiplead': CHIPLEAD,
'chipbass': CHIPBASS,
'chipnoise': CHIPNOISE,
'tech_saws': TECHSAWS,
'sound_in': SOUND_IN,
'sound_in_stereo': SOUND_IN_STEREO
}
