import streamlit as st
from module_sound import *
from module_game import *
from symbols import *
from util import *

header = st.container()

sound_module = SoundCreator()

# Configuration
checkpoint = {
    "name": "Checkpoint A",
    "symbols": "KMRSUA",
}

symbol_msg_bold = get_symbol_message(checkpoint["symbols"], bold=True)
symbol_msg = get_symbol_message(checkpoint["symbols"], bold=False)

with header:
    st.title(f"{checkpoint['name']}")
    st.info(
        f"Welcome to **{checkpoint['name']}!** Here, we will practice the symbols {checkpoint['symbols']} in a longer format. We will both practice sequences, and start to form our first words!"
    )
