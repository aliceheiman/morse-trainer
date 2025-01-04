import streamlit as st

from module_scraper import *
from module_sound import *
from module_game import *
from symbols import *
from util import *

header = st.container()
playground = st.container()
player = st.container()

with header:
    st.title("Playground")
    st.info(
        "Welcome to the **Playground**! Here you can input your own text to played, play with speeds and spaces, and practice your morse skills on literature and the latest news!"
    )

with playground:
    with st.form("free-text"):
        #
        text = st.text_area("Translate Message", placeholder="Type your message here...")

        # SLIDERS
        col1, col2 = st.columns(2)
        with col1:
            character_speed = st.slider("Character Speed", min_value=1, max_value=70, value=22)

        with col2:
            farnsworth_speed = st.slider("Farnsworth Speed", min_value=1, max_value=70, value=8)

        # GENERATE BUTTON
        submitted = st.form_submit_button("Generate")
        if submitted:
            sound_module = SoundCreator(character_speed=character_speed, farnsworth_speed=farnsworth_speed)

            text = clean(text, allowed_symbols=BASIC_SYMBOLS)
            audio = sound_module.create_audio_from(text)
            st.audio(audio, sample_rate=sound_module.sample_rate)

with player:
    st.header("Practice")
    sequence = ""

    sound_player = SoundCreator(character_speed=character_speed, farnsworth_speed=farnsworth_speed)
    game = GameCreator(label="Practice", symbols=BASIC_SYMBOLS)
    game.reset_message()

    option = st.selectbox("What excerpt do you want to practice on?", ("Nature Daily Briefing", "Shakespeare"))

    if option == "Nature Daily Briefing":
        news, dates = get_nature_briefings()

        options = list(dates[0:5])
        select = st.radio("Select Date", options, 0)

        op_index = options.index(select)
        st.write(f"Nature Daily Briefing from {select}")

        sequence = news[op_index]

    if option == "Shakespeare":
        sonnet_nr = st.slider("Sonnet Number", min_value=1, max_value=154)

        sonnet = get_shakespeare(sonnet_nr)
        sequence = " ".join(sonnet["lines"])
        st.write(sonnet["title"])

    sequence = clean(sequence, allowed_symbols=BASIC_SYMBOLS)
    game.initalize_message(sequence)
    audio = sound_player.create_audio_from(game.get_message(), start_delay_ms=1000)
    st.audio(audio, sample_rate=sound_player.sample_rate)

    game.Typer()
