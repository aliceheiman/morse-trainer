import streamlit as st

from module_scraper import *
from module_sound import *
from module_game import *
from symbols import *
from util import *

header = st.container()
playground = st.container()

sound_module = SoundCreator()

with header:
    st.title("Playground")
    st.info(
        "Welcome to the **Playground**! Here you can input your own text to played, play with speeds and spaces, and practice your morse skills on literature and the latest news!"
    )

with playground:
    audio = sound_module.create_audio_from("PARIS")
    st.audio(audio, sample_rate=sound_module.sample_rate)
