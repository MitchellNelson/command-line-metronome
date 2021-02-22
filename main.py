import argparse
import time
import simpleaudio as sa
import os
import threading

SOUND_PATH = 'audio/beat.wav'

class Metronome:
    def __init__(self, bpm):
        self.bpm = bpm
        self.sound = sa.WaveObject.from_wave_file(SOUND_PATH)
    
    def start(self):
        sleep_time = 60 / self.bpm
        cptr = 0
        time_start = time.time()
        time_init = time.time()
        while True:
            cptr += 1
            time_start = time.time()
            time.sleep(((time_init + (sleep_time * cptr)) - time_start ))
            t00 = threading.Thread(name='thread_request', target=self.sound.play, args=([]))
            t00.start()

def main():
    pid = os.getpid()
    os.system("sudo renice -n -19 -p " + str(pid)) 
    parser = argparse.ArgumentParser(description='Play a sound at a tempo')
    parser.add_argument('bpm', type=int, help='test')
    args = parser.parse_args()
    metronome = Metronome(float(args.bpm))
    try:
        metronome.start()
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()
