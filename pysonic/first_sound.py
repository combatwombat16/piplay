from psonic import *

play(70)
sleep(1)

tick = Message()

@in_thread
def drums():
    while True:
        tick.cue()
        for i in range(16):
            r = random.randrange(1,10)
            sample(DRUM_BASS_HARD, rate=r)
            sleep(0.125)

drums()
