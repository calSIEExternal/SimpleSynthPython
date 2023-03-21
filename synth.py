# SIE CONFIDENTIAL
# $
# Copyright(C) 2021 Sony Interactive Entertainment Inc.
# All Rights Reserved

""" DESCRIBE FILE
"""
import argparse

import numpy as np
from scipy.io.wavfile import write
import simpleaudio as sa

class Synth:
    
    def __init__(self, fs=48000):
        self.output = []
        self.fs = fs
        self.phase = 0
        self.amplitude_limit_scale = 0.5

    def clear_output(self):
        self.output = []

    def append_note_to_output(self, type, freq, duration, amplitude):
        """Add a single note of specified type, frequency, duration and amplitude to the output

        Args
        type : What type of note to add
        duration : length of note in seconds
        amplitude : 0 < amplitude of note < 1
        """

        # Limit amplitude to prevent accidental distortion/loud .wav files
        amplitude = min(1, max(0, amplitude))

        if type == 'sine':
            note = self.synth_sine(freq, duration) * amplitude
        elif type == 'saw':
            note = self.synth_sawtooth(freq, duration) * amplitude
        elif type == 'silence':
            note = np.zeros(int(duration*self.fs))

        self.output.append(note)

    def add_tune(self):
        """example function to add a basic tune to the output"""
        self.append_note_to_output('sine', 1000, 0.5, 1)
        self.append_note_to_output('saw', 2000, 0.5, 0.5)
        self.append_note_to_output('silence', 0, 0.5, 0)
        self.append_note_to_output('sine', 500, 0.5, 0.5)

    def play_output(self):
        """Function will format and save self.output to a .wav file and then play that file"""

        render = np.asarray(self.output).flatten()
        render *= self.amplitude_limit_scale
        write("output.wav", self.fs, (np.iinfo(np.int16).max * render).astype(np.int16))

        play_obj = sa.WaveObject.from_wave_file("output.wav").play()
        play_obj.wait_done()

    def synth_sine(self, freq, duration):
        """Produce a sine wave"""

        out_wave = np.zeros(int(duration*self.fs))

        for i, _ in enumerate(out_wave):

            out_wave[i] = np.sin(self.phase * 2 * np.pi)

            self.phase += freq/self.fs

            if self.phase > 1:
                self.phase -= 1

        return out_wave

    def synth_sawtooth(self, freq, duration):
        """Produce a sawtooth wave

        Args
        freq: frequency of wave
        duration: length of not (in seconds)"""

        out_wave = np.zeros(int(duration*self.fs))

        for i, _ in enumerate(out_wave):

            out_wave[i] = (self.phase*2) - 1

            self.phase += freq/self.fs

            if self.phase > 1:
                self.phase -= 1

        return out_wave

def main():
    r"""main function to produce and play tune from command line

    Accepts command line argument list as
    freq, duration, amplitude, freq, duration, amplitude, freq, duration....
    for each note you wish to add

    Example:
        "C\Users\...\SimpleSynthPython> venv\scripts\python synth.py 1000 0.5 0.5 2000 0.5 0.5"
    """

    # Define argument parser and get arguments
    parser = argparse.ArgumentParser(description="play a tune")
    parser.add_argument('values', type=float, nargs='+')
    args = parser.parse_args()
    values = args.values

    # Make synthesiser
    synth = Synth()

    # Loop through groups of 3 arguments
    for i in range(int(len(values)/3)):
        i *= 3
        synth.append_note_to_output('sine', values[i], values[i+1], values[i+2])

    synth.play_output()


if __name__ == "__main__":
    main()
