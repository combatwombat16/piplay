import sys, time
sys.path.append("../")
from psonic import *
from weather_pilock.SenseHat_Data import Sensor
from helpers.helpers import *

def rescale(reading, new_min = 30.0, new_max = 110.0):
    return ((new_max - new_min) * ((reading.value - reading.min_value) / (reading.max_value - reading.min_value))) + new_min

class Notes(JsonSerializable):
    def __init__(self, notes, attack = 0.0, attack_level = 1.0, sustain = 1.0, sustain_level = 1.0, release = 0.0, decay_level = 0.0 , decay = 0.0, amp = 1.0, pan = 0.0):
        self.notes = notes
        self.attack = attack
        self.attack_level = attack_level
        self.sustain = sustain
        self.sustain_level = sustain_level
        self.release = release
        self.decay = decay
        self.decay_level = decay_level
        self.amp = amp
        self.pan = pan

        
class Rates(JsonSerializable):
    def __init__(self, beats_per_minute = 60.0, collections_per_beat = 3.0):
        self.beats_per_minute = beats_per_minute
        self.beats_per_second = self.beats_per_minute / 60.0
        self.seconds_per_beat = 1 / self.beats_per_second
        self.collections_per_beat = collections_per_beat
        self.collection_delay = max((self.beats_per_second / self.collections_per_beat), 0.1)

