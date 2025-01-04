import numpy as np
import math
from symbols import *


class SoundCreator:
    def __init__(self, character_speed=22, farnsworth_speed=8, sample_rate=44100.0):
        self.sample_rate = sample_rate
        self.character_speed = character_speed
        self.farnsworth_speed = farnsworth_speed

        # Compute timings
        u = 1.2 / character_speed
        ta = (60 * character_speed - 37.2 * farnsworth_speed) / (farnsworth_speed * character_speed)
        tc = (3 * ta) / 19
        tw = (7 * ta) / 19

        # Convert to milliseconds
        self.dot_length = round(u * 1000)
        self.dash_length = round(u * 3 * 1000)
        self.intra_character_space = round(u * 1000)
        self.inter_character_space = round(tc * 1000)
        self.inter_word_space = round(tw * 1000)

        # Initialize audio array
        self.audio = []
        self.morse_dict = {k: l[1].replace("▄▄", "-").replace("▄", "*").replace(" ", "") for k, l in mnemonics.items()}

    def _append_silence(self, duration_ms=500):
        """Adding silence by appending zeros."""
        num_samples = duration_ms * (self.sample_rate / 1000.0)

        for _ in range(int(num_samples)):
            self.audio.append(0.0)

    def _append_sinewave(self, freq=550.0, duration_ms=500, volume=0.2):
        """Appends a beep of length duration_ms"""
        num_samples = duration_ms * (self.sample_rate / 1000.0)

        for x in range(int(num_samples)):
            self.audio.append(volume * math.sin(2 * math.pi * freq * (x / self.sample_rate)))

    def create_audio_from(self, sequence: str, start_delay_ms=None):
        """Takes a strings sequence and transforms it into a playable Morse audio clip.

        Args:
            sequence (str): Message to be enconded into Morse Code.

        Returns:
            np_array: audio data for an audio player.
        """

        # reset audio array
        self.audio = []

        # Add silence at beginning
        if start_delay_ms:
            self._append_silence(duration_ms=start_delay_ms)

        for character in sequence:
            character = character.upper()

            if character in self.morse_dict:
                morse_encoding = self.morse_dict[character]

                for i, symbol in enumerate(morse_encoding):
                    if symbol == "*":
                        # Short sound
                        self._append_sinewave(duration_ms=self.dot_length)
                    elif symbol == "-":
                        # Long sound:
                        self._append_sinewave(duration_ms=self.dash_length)

                    if i + 1 < len(morse_encoding):
                        self._append_silence(duration_ms=self.intra_character_space)

                # Add inter-character spacing
                self._append_silence(duration_ms=self.inter_character_space)

            if character == " ":
                # Add inter-word spacing
                self._append_silence(duration_ms=self.inter_word_space)

        return np.array(self.audio)
