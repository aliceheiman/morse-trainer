import streamlit as st
from module_sound import *
from module_game import *
from symbols import *
from util import *

header = st.container()
background = st.container()
tutorial = st.container()

sound_module = SoundCreator()

# Configuration
level = {
    "level": "Level 1",
    "new_symbols": "ET",
    "new_label": "ET",
    "all_label": "ET",
    "length_unit": 5,
    "num_units_tutorial": 5,
    "num_units_all": 7,
}

symbol_msg_bold = get_symbol_message(level["new_symbols"], bold=True)
symbol_msg = get_symbol_message(level["new_symbols"], bold=False)

game_new = GameCreator(label=level["new_label"], symbols=level["new_symbols"])
game_all = GameCreator(label=level["all_label"], symbols=level["all_label"])

with header:
    st.title(level["level"])
    st.info(f"Welcome to **{level['level']}!** Here we start our journey with the symbols {symbol_msg_bold}.")

with background:
    st.header("Background")
    st.markdown(
        "This guide uses the *Koch* method. The characters are played at full speed, but the spacing between symbols and words is increased. We start with two letters, and then build on top of that by adding more characters and eventually forming words."
    )

with tutorial:
    st.header("Tutorial")

    table_mnemonics = [mnemonics[s] for s in level["new_symbols"]]
    table_data = {"Symbol": first(table_mnemonics), "Code": second(table_mnemonics), "Mnemonic": third(table_mnemonics)}

    st.table(table_data)

    st.markdown(f"Have a listen to the symbols {symbol_msg_bold} played *three times each* below:")

    for symbol in level["new_symbols"]:
        audio = sound_module.create_audio_from(f" {symbol}" * 3)
        st.audio(audio, sample_rate=sound_module.sample_rate)

    st.markdown(
        f"Try to say the corresponding mnemonic while listening and learn their rhythm. Below you can hear a sequence of the symbols {symbol_msg}."
    )

    tutorial_sequence = game_new.generate_sequence(length_unit=5, num_units=3)
    st.markdown(f"**Sequence:** {tutorial_sequence}")

    tutorial_audio = sound_module.create_audio_from(tutorial_sequence)
    st.audio(tutorial_audio, sample_rate=sound_module.sample_rate)

    st.subheader(f"Practice {symbol_msg}")
    st.write(
        f"Click play to hear a mixed sequence of the symbols. **The message consists of {number_to_word[level['num_units_tutorial']]} sequences of {number_to_word[level['length_unit']]} characters**. Type what you hear and press ENTER. The program will give you feedback."
    )

    sequence = game_new.generate_sequence(length_unit=level["length_unit"], num_units=level["num_units_tutorial"])
    game_new.initalize_message(sequence)

    audio = sound_module.create_audio_from(game_new.get_message(), start_delay_ms=1000)
    st.audio(audio, sample_rate=sound_module.sample_rate)

    game_new.Typer()
