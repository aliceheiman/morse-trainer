import numpy as np
import math

########################################
# SETUP
########################################

DOT_LENGTH = 150
SILENCE_MULTIPLIER = 1
SAMPLE_RATE = 44100.0

morse_dict = {
    "A": "*-",
    "B": "-***",
    "C": "-*-*",
    "D": "-**",
    "E": "*",
    "F": "**-*",
    "G": "--*",
    "H": "****",
    "I": "**",
    "J": "*---",
    "K": "-*-",
    "L": "*-**",
    "M": "--",
    "N": "-*",
    "O": "---",
    "P": "*--*",
    "Q": "--*-",
    "R": "*-*",
    "S": "***",
    "T": "-",
    "U": "**-",
    "V": "***-",
    "W": "*--",
    "X": "-**-",
    "Y": "-*--",
    "Z": "--**",
}


########################################
# FUNCTIONS
########################################


class SoundCreator:
    def __init__(self, dot_length=70, silence_multiplier=4, sample_rate=44100.0):
        self.dot_length = dot_length
        self.silence_multiplier = silence_multiplier
        self.sample_rate = sample_rate
        self.dash_length = 3 * dot_length
        self.short_silence = (3 * dot_length) * silence_multiplier
        self.long_silence = (4 * dot_length) * silence_multiplier
        self.audio = []

        self.morse_dict = {
            "A": "*-",
            "B": "-***",
            "C": "-*-*",
            "D": "-**",
            "E": "*",
            "F": "**-*",
            "G": "--*",
            "H": "****",
            "I": "**",
            "J": "*---",
            "K": "-*-",
            "L": "*-**",
            "M": "--",
            "N": "-*",
            "O": "---",
            "P": "*--*",
            "Q": "--*-",
            "R": "*-*",
            "S": "***",
            "T": "-",
            "U": "**-",
            "V": "***-",
            "W": "*--",
            "X": "-**-",
            "Y": "-*--",
            "Z": "--**",
        }

    def append_silence(self, duration_ms=500):
        """
        Adding silence is easy - we add zeros to the end of our array
        """
        num_samples = duration_ms * (self.sample_rate / 1000.0)

        for x in range(int(num_samples)):
            self.audio.append(0.0)

        return

    def append_sinewave(self, freq=800.0, duration_ms=500, volume=0.25):
        """
        Appends a beep of length duration_ms to our
        """

        num_samples = duration_ms * (self.sample_rate / 1000.0)

        for x in range(int(num_samples)):
            self.audio.append(volume * math.sin(2 * math.pi * freq * (x / self.sample_rate)))

        return

    def create_audio_from(self, sequence: str, start_delay_ms=None):
        """Generates Morse Code from a symbol sequence

        Args:
            sequence (str): Message to be enconded into Morse Code.

        Returns:
            np_array: audio data for an audio player.
        """

        self.audio = []

        # Add silence at beginning
        if start_delay_ms:
            self.append_silence(duration_ms=start_delay_ms)

        for character in sequence:
            character = character.upper()

            if character in self.morse_dict.keys():
                for symbol in self.morse_dict[character]:
                    if symbol == "*":
                        # Short sound
                        self.append_sinewave(duration_ms=self.dot_length)
                    elif symbol == "-":
                        # Long sound:
                        self.append_sinewave(duration_ms=self.dash_length)

                    self.append_silence(duration_ms=self.dot_length)

                # Add short silence
                self.append_silence(duration_ms=self.short_silence)

            if character == " ":
                # Add long silence
                self.append_silence(duration_ms=self.long_silence)

        return np.array(self.audio)
