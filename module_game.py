import random
import streamlit as st


class GameCreator:
    def generate_sequence(self, symbols: str, length_unit: int, num_units: int):
        """Creates a random letter sequence of *length_unit* chunks, *num_unit* times.

        Args:
            symbols (str): Symbols to use in the sequence
            length_unit (int): Number of symbols in each chunk, 3 gives "XXX"
            num_units (int): Number of chunks in each sequence, 2 gives "XXX XXX"
        """

        seq = []
        for _ in range(num_units):
            seq.append("".join(random.choices(symbols, k=length_unit)))

        return " ".join(seq)

    def typer(self, symbols: str, sequence: str, label: str):
        """_summary_

        Args:
            symbols (str): _description_
            sequence (str): _description_
            label (str): _description_
        """

        formatted_symbols = ", ".join(sorted(list(symbols)))
        st.markdown(f"*Available symbols:* **{formatted_symbols}**")

        user_input = st.text_input("**:blue[Type what you hear] 👇**")

        if user_input:
            # Compare correct sequence with inputed sequence
            compare = ""
            print(user_input)

            for c1, c2 in zip(list(sequence), list(user_input)[: len(sequence)]):
                if c1.upper() == c2.upper():
                    compare += f":green[{c2}]"
                if c2 == " ":
                    compare += " "
                else:
                    compare += f":red[{c2}]"

            if len(user_input) > len(sequence):
                compare += f":orange[{user_input[len(sequence):]}]"

            st.write(compare)
            st.write(f"Correct: {sequence}")

        if st.button("reset"):
            pass
