import streamlit as st
import streamlit as st
from module_sound import *
from module_game import *
from symbols import *
from util import *


def generate_level(level):
    header = st.container()
    tutorial = st.container()
    sound_module = SoundCreator()

    symbol_msg_bold = get_symbol_message(level["new_symbols"], bold=True)
    symbol_msg = get_symbol_message(level["new_symbols"], bold=False)

    game_new = GameCreator(label=level["new_label"], symbols=level["new_symbols"])

    if "all_label" in level:
        game_all = GameCreator(label=level["all_label"], symbols=level["all_label"])

    with header:
        st.title(level["level"])
        st.info(
            f"Welcome to **{level['level']}!** Here we extend our character set with the symbols {symbol_msg_bold}."
        )

    with tutorial:
        st.header("Tutorial")

        table_mnemonics = [mnemonics[s] for s in level["new_symbols"]]
        table_data = {
            "Symbol": first(table_mnemonics),
            "Code": second(table_mnemonics),
            "Mnemonic": third(table_mnemonics),
        }

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

        if "all_label" in level:
            st.subheader("Practice Everything")
            st.write(
                f"Click play to hear a sequence of all symbols we have learned so far. **The message consists of {number_to_word[level['num_units_all']]} sequences of {number_to_word[level['length_unit']]} characters**. It might take a couple of tries! Type what you hear and press ENTER. The program will give you feedback."
            )

            sequence_all = game_all.generate_sequence(
                length_unit=level["length_unit"], num_units=level["num_units_all"]
            )
            game_all.initalize_message(sequence_all)
            audio = sound_module.create_audio_from(game_all.get_message(), start_delay_ms=1000)
            st.audio(audio, sample_rate=sound_module.sample_rate)

            game_all.Typer()


def generate_checkpoint(checkpoint):
    header = st.container()
    challenge = st.container()
    reference_table = st.container()

    sound_module = SoundCreator()

    symbol_msg_bold = get_symbol_message(checkpoint["symbols"], bold=True)
    symbol_msg = get_symbol_message(checkpoint["symbols"], bold=False)

    game_checkpoint = GameCreator(label=checkpoint["name"], symbols=checkpoint["symbols"])

    if checkpoint["c_type"] == C_WORDS:
        game_checkpoint.generate_anagrams(filename="data/english-words.txt")
    if checkpoint["c_type"] == C_QUOTES:
        game_checkpoint.get_quotes(filename="data/cleaned-quotes.txt", ignore=checkpoint["ignore"])

    with header:
        st.title(f"{checkpoint['name']}")
        st.info(
            f"Welcome to **{checkpoint['name']}!** Here, we will practice the symbols {symbol_msg_bold}. {checkpoint['text']}"
        )

    with challenge:
        st.header("Challenge Time!")

        if checkpoint["c_type"] == C_WORDS:
            sequence = game_checkpoint.generate_word_sequence(num_words=checkpoint["num_words"])
        if checkpoint["c_type"] == C_QUOTES:
            sequence = game_checkpoint.generate_quote()

        game_checkpoint.initalize_message(sequence)

        audio = sound_module.create_audio_from(game_checkpoint.get_message(), start_delay_ms=1000)
        st.audio(audio, sample_rate=sound_module.sample_rate)

        game_checkpoint.Typer()

    with reference_table:
        st.header("For Reference")

        table_mnemonics = [mnemonics[s] for s in sorted(list(checkpoint["symbols"]))]
        table_data = {
            "Symbol": first(table_mnemonics),
            "Code": second(table_mnemonics),
            "Mnemonic": third(table_mnemonics),
        }

        st.table(table_data)
