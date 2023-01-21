import streamlit as st
from module_sound import *
from module_game import *
from symbols import *
from util import *

header = st.container()
challenge = st.container()

sound_module = SoundCreator()

# Configuration
checkpoint = {"name": "Checkpoint B", "symbols": "KMRSUAPTLOWI", "num_words": 10}

symbol_msg_bold = get_symbol_message(checkpoint["symbols"], bold=True)
symbol_msg = get_symbol_message(checkpoint["symbols"], bold=False)

game_checkpoint = GameCreator(label=checkpoint["name"], symbols=checkpoint["symbols"])
game_checkpoint.generate_anagrams(filename="english-words.txt")

with header:
    st.title(f"{checkpoint['name']}")
    st.info(
        f"Welcome to **{checkpoint['name']}!** Here, we will practice the symbols {symbol_msg_bold} in a longer format. Let's practice these symbols by forming words!"
    )

with challenge:
    st.header("Challenge Time!")

    sequence = game_checkpoint.generate_word_sequence(num_words=checkpoint["num_words"])
    game_checkpoint.initalize_sequence(sequence)

    audio = sound_module.create_audio_from(game_checkpoint.get_message(), start_delay_ms=1000)
    st.audio(audio, sample_rate=sound_module.sample_rate)

    game_checkpoint.Typer()
