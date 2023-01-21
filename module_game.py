import random
import streamlit as st


class GameCreator:
    def __init__(self, label, symbols):
        self.label = label
        self.symbols = symbols

    @st.cache(allow_output_mutation=True)
    def Message(self):
        return []

    def get_message(self):
        return self.Message()[0]

    def add_message(self, message):
        if not self.Message():
            self.Message().append(message)

    def initalize_sequence(self, length_unit: int, num_units: int):
        self.add_message(self.generate_sequence(length_unit, num_units))

    def generate_sequence(self, length_unit: int, num_units: int):
        """Creates a random letter sequence of *length_unit* chunks, *num_unit* times.

        Args:
            symbols (str): Symbols to use in the sequence
            length_unit (int): Number of symbols in each chunk, 3 gives "XXX"
            num_units (int): Number of chunks in each sequence, 2 gives "XXX XXX"
        """

        seq = []
        for _ in range(num_units):
            seq.append("".join(random.choices(self.symbols, k=length_unit)))

        return " ".join(seq)

    def Typer(self):

        message = self.get_message()

        formatted_symbols = ", ".join(sorted(list(self.symbols)))
        st.markdown(f"*Available symbols:* **{formatted_symbols}**")

        with st.form(key=self.label, clear_on_submit=True):
            user_input = st.text_input("**:blue[Type what you hear] 👇**")

            if st.form_submit_button("Submit"):
                user = user_input.upper()
                answer = message.upper()
                output = ""

                for i in range(len(user)):
                    if user[i] == answer[i]:
                        output += f":green[{user[i]}]" if user[i] != " " else " "
                    else:
                        output += f":red[{user[i]}]" if user[i] != " " else " "

                st.markdown(f"***Your Answer:*** {output}")
                st.markdown(f"*Comparison:*  {answer}")

        reset = st.button(f"Reset {self.label}")
        if reset:
            self.Message().clear()
            st.experimental_rerun()
