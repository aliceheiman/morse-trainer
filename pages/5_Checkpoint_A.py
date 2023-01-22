from template import *

# Configuration
checkpoint = {
    "name": "Checkpoint A",
    "text": "We will practice by forming words.",
    "symbols": "ETASIL",
    "c_type": C_WORDS,
    "num_words": 10,
    "ignore": "",
}

generate_checkpoint(checkpoint)
