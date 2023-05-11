import streamlit as st
from module_sound import *
from module_game import *
import numpy as np
import pandas as pd

header = st.container()
background = st.container()
tutorial = st.container()
references = st.container()

sound_module = SoundCreator()

# order = "ETASILONUDRHMFWGCY.,BPKV;:ZJXQ"

with header:
    st.title("Morse Trainer Whop!")
    st.info(
        "Welcome to **Morse Trainer!** The aim of this app is to teach you morse code through a series of interactive levels."
    )

    st.write(
        'According to Wikipedia: "Morse code is a method used in telecommunication to encode text characters as standardized sequences of two different signal durations, called dots and dashes, or dits and dahs. Morse code is named after Samuel Morse, one of the inventors of the telegraph."'
    )
    st.write("In short, Morse Code is a way to use short beeps and long beeps to convey messages.")

with background:
    st.header("The Morse Code Alphabet")
    st.write(
        "Every letter is converted into a sequence of dots and dashes. Dots represent short beeps. Dashes represent long beeps. The most common letters, such as 'E' and 'T', usually have shorter sequences - making them faster to transmit."
    )
    st.image("assets/morse_code.webp")
    st.caption("*[Image Source](https://medium.com/fgd1-the-archive/morse-code-771534ff98e4)* :sunglasses:")

    st.markdown(
        """
    The Morse code adheres to the following rules:
    * The length of a dot is one unit.
    * A dash is three units.
    * The space between parts of the same letter is one unit.
    * The space between letters is three units.
    * The space between words is seven units.
    """
    )

    # st.write(
    #     'Using mnemonics is a popular way to make learning the morse sequences easier. Below is a visual mnemonic of the morse code alphabet. Read each letter top-down (except Z). The "di" represent short beeps/dots, and the "dah" represent long beeps/dashes.'
    # )

    # st.image("assets/visualmnemonic.png")
    # st.caption("*[Image Source](https://en.wikipedia.org/wiki/Morse_code_mnemonics)* :sunglasses:")

with tutorial:
    st.header("Tutorial")
    st.info(
        "To learn the format of this guide, let us begin with the most important morse sequence: the emergency call **SOS**. To learn this sequence, we need two letters: **S** and **O**."
    )

    SOS = {"Letter": ["S", "O"], "Code": ["▄ ▄ ▄", "▄▄ ▄▄ ▄▄"], "Mnemonic": ["sí-sí-sí", "OH! MY! GOD!"]}

    st.table(SOS)

    st.markdown("Have a listen to the letters **S** and **O** played *three times each* below:")

    s = sound_module.create_audio_from("S S S")
    st.audio(s, sample_rate=sound_module.sample_rate)

    o = sound_module.create_audio_from("O O O")
    st.audio(o, sample_rate=sound_module.sample_rate)

    st.markdown(
        "Could you hear the difference? Try to say the corresponding letter while listening and learn their rhythm. Below you can hear a sequence of S's and O's in action together."
    )

    st.markdown("**Sequence:** SOS SOS SOS")

    so_sequence = sound_module.create_audio_from("SOS SOS SOS")
    st.audio(so_sequence, sample_rate=sound_module.sample_rate)

    st.subheader("Practice")
    st.write(
        "Click play to hear a sequence of S's and O's. Type what you hear and press ENTER. The program will give you feedback."
    )

    # Setup practice level
    game = GameCreator(label="SOS", symbols="OS")
    sequence = game.generate_sequence(length_unit=5, num_units=5)
    game.initalize_message(sequence)

    audio = sound_module.create_audio_from(game.get_message(), start_delay_ms=1000)
    st.audio(audio, sample_rate=sound_module.sample_rate)

    game.Typer()


with references:
    st.header("References")

    st.markdown(
        """
    * Streamlit, [API Reference](https://docs.streamlit.io/library/api-reference)
    * Wikipedia, [Morse Code Mnemonic](https://en.wikipedia.org/wiki/Morse_code_mnemonics)
    * Chloe Wooldrage, Medium, ['Morse Code (1836)'](https://medium.com/fgd1-the-archive/morse-code-771534ff98e4)
    * MorseCode.World, [Morse Code Timing](https://morsecode.world/international/timing.html)
    * Jon Bloom, ARRL Laboratory, [A Standard for Morse Timing Using the Farnsworth Technique](http://www.arrl.org/files/file/Technology/x9004008.pdf)
    * Quotes, [dwyl](https://github.com/dwyl/quotes/blob/main/quotes.json), [robatron](https://gist.githubusercontent.com/robatron/a66acc0eed3835119817/raw/0e216f8b6036b82de5fdd93526e1d496d8e1b412/quotes.txt), [vinitshahdeo](https://github.com/vinitshahdeo/inspirational-quotes/blob/master/data/data.json), 
    * Bad Words Corpus, [MauriceButler](https://github.com/MauriceButler/badwords/blob/master/array.js), [LDNOOBW](https://github.com/LDNOOBW/List-of-Dirty-Naughty-Obscene-and-Otherwise-Bad-Words/blob/master/en)
    """
    )
