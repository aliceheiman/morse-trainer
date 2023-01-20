import streamlit as st
from module_sound import *
from module_game import *

header = st.container()
background = st.container()
tutorial = st.container()

sound_module = SoundCreator()
game = GameCreator(label="KM", symbols="KM")

with header:
    st.title("Level 1")
    st.info("Welcome to **Level 1!** Here we start with the two letters **K** and **M**.")

with background:

    st.header("Background")
    st.markdown(
        "This guide uses the *Koch* method. The characters are played at full speed, but the spacing between symbols and words is increased. We start with two letters, and then build on top of that by adding more characters and eventually forming words."
    )

with tutorial:
    st.header("Tutorial")

    KM = {"Symbol": ["K", "M"], "Code": ["▄▄ ▄ ▄▄", "▄▄ ▄▄"], "Mnemonic": ["KAN-dy KID", "MA-MA"]}

    st.table(KM)

    st.markdown("Have a listen to the letters **K** and **M** played *three times each* below:")

    s = sound_module.create_audio_from("K K K")
    st.audio(s, sample_rate=sound_module.sample_rate)

    o = sound_module.create_audio_from("M M M")
    st.audio(o, sample_rate=sound_module.sample_rate)

    st.markdown(
        "Could you hear the difference? Try to say the corresponding mnemonic while listening and learn their rhythm. Below you can hear a sequence of K's and M's."
    )

    tutorial_sequence = "MMK MKM KKM KMK"
    st.markdown(f"**Sequence:** {tutorial_sequence}")

    tutorial_audio = sound_module.create_audio_from(tutorial_sequence)
    st.audio(tutorial_audio, sample_rate=sound_module.sample_rate)

    st.subheader("Practice")
    st.write(
        "Click play to hear a sequence of K's and M's. Type what you hear and press ENTER. The program will give you feedback."
    )

    game.initalize_sequence(length_unit=3, num_units=5)

    audio = sound_module.create_audio_from(game.get_message(), start_delay_ms=1000)
    st.audio(audio, sample_rate=sound_module.sample_rate)

    game.Typer()
