from template import *

# Configuration
checkpoint = {
    "name": "Checkpoint B",
    "text": "We will practice by forming words.",
    "symbols": "ETASILONUDRH",
    "c_type": C_WORDS,
    "num_words": 10,
    "ignore": "",
}

generate_checkpoint(checkpoint)
