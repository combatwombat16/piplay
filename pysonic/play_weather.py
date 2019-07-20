import sys, time
sys.path.append("../")
from psonic import *
from weather_pilock.SenseHat_Data import Sensor
from helpers.helpers import *
import ipywidgets as widgets

def rescale(reading, new_min = 30.0, new_max = 110.0):
    return ((new_max - new_min) * ((reading.value - reading.min_value) / (reading.max_value - reading.min_value))) + new_min


class Notes(JsonSerializable):
    def __init__(self, notes, 
                 attack = 0.0, decay = 0.0, 
                 sustain = 1.0, sustain_level = 1.0, 
                 release = 0.0, cutoff=0.0, cutoff_attack=0.0, 
                 amp = 1.0, pan = 0.0):
        self.notes = notes
        self.attack = attack
        self.sustain = sustain
        self.sustain_level = sustain_level
        self.release = release
        self.decay = decay
        self.cutoff = cutoff
        self.cutoff_attack = cutoff_attack
        self.amp = amp
        self.pan = pan


class Rates(JsonSerializable):
    def __init__(self, beats_per_minute = 60.0, collections_per_beat = 3.0):
        self.beats_per_minute = beats_per_minute
        self.beats_per_second = self.beats_per_minute / 60.0
        self.seconds_per_beat = 1 / self.beats_per_second
        self.collections_per_beat = collections_per_beat
        self.collection_delay = max((self.beats_per_second / self.collections_per_beat), 0.1)

class NoteUI:
    def __init__(self, name: ""):
        self.name = name
        self.amp_slider = widgets.FloatSlider(value=0.5, min=0.0, max=1.0, step=0.01, description="amp", orientation="horizontal")
        self.pan_slider = widgets.FloatSlider(value=0.0, min=-1.0, max=1.0, step=0.1, description="pan", orientation="horizontal")
        self.attack_slider = widgets.FloatSlider(value=0.1, min=0.0, max=2.0, step=0.1, description="attack", orientation="horizontal")
        self.decay_slider = widgets.FloatSlider(value=0.0, min=0.0, max=2.0, step=0.1, description="decay", orientation="horizontal")
        self.sustain_slider = widgets.FloatSlider(value=1.0, min=0.0, max=2.0, step=0.1, description="sustain", orientation="horizontal")
        self.sustain_level_slider = widgets.FloatSlider(value=1.0, min=0.0, max=1.0, step=0.01, description="sustain level", orientation="vertical")
        self.release_slider = widgets.FloatSlider(value=0.5, min=0.0, max=2.0, step=0.1, description="release", orientation="horizontal")
        self.play_button = widgets.Button(
            description='Update'
        )