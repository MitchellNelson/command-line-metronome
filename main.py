import argparse
import time
import simpleaudio as sa

SOUND_PATH = 'audio/beat.wav'
TIMING_OFFSET = .004

class Metronome:
    def __init__(self, bpm):
        self.bpm = bpm
        self.sound = sa.WaveObject.from_wave_file(SOUND_PATH)
        self.downbeat = sa.WaveObject.from_wave_file(DOWNBEAT_SOUND_PATH)

    def start(self):
        print('Press Ctrl-C to terminate metronome')
        sleep_time = (60.0 / self.bpm)
        before = time.time()
        while(1):
            self.sound.play()
            time.sleep(sleep_time - (time.time() - before) - TIMING_OFFSET)
            before = time.time()

def main():
    parser = argparse.ArgumentParser(description='Play a sound at a tempo')
    parser.add_argument('bpm', help='test')
    args = parser.parse_args()
    metronome = Metronome(float(args.bpm))
    try:
        metronome.start()
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()
