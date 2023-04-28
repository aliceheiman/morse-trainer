import random
import streamlit as st


class GameCreator:
    def __init__(self, label, symbols):
        self.label = label
        self.symbols = symbols
        self.anagrams = None
        self.quotes = None

    @st.cache(allow_output_mutation=True)
    def Message(self):
        return []

    def get_message(self):
        return self.Message()[0]

    def add_message(self, message):
        if not self.Message():
            self.Message().append(message)

    def initalize_sequence(self, sequence):
        self.add_message(sequence)

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

    def generate_anagrams(self, filename):
        """
        Find all possible words with the current symbol set (self.symbols).

        Args:
            filename (str): The name of the file containing the dictionary of words.

        Returns:
            list: A list of all anagrams that can be formed using the current symbol set.
        """

        # Step 1: Read words from the file line by line
        with open(filename, "r") as f:
            words = f.read().split("\n")

        # Step 2: Get all anagrams
        anagrams = []
        symbol_set = set(self.symbols.lower())
        for word in words:
            word_set = set(word.lower())

            if word_set.issubset(symbol_set):
                if word.upper() not in anagrams:
                    anagrams.append(word.upper())

        # Step 3: Save and return the list of anagrams
        self.anagrams = anagrams
        return anagrams

    def generate_word_sequence(self, num_words: int):
        """Assemble possible words into a word sequence."""
        words = random.choices(self.anagrams, k=num_words)
        return " ".join(words)

    def get_quotes(self, filename, ignore=""):
        """
        Get a list of quotes that can be formed using the current symbol set (self.symbols).

        Args:
            filename (str): The name of the file containing the list of quotes.
            ignore (str): A string containing characters to ignore in the quotes (optional).

        Returns:
            list: A list of quotes that can be formed using the current symbol set.
        """

        # Step 1: Read quotes from the file
        with open(filename, "r") as f:
            quotes = f.read().upper().split("\n")

        # Step 2: Filter the quotes based on valid characters
        character_set = set(self.symbols.upper() + ignore.upper() + " ")
        quotes = [q for q in quotes if all(c in character_set for c in q)]

        # Step 3: Remove ignored characters from the quotes
        for s in ignore.upper():
            quotes = [q.replace(s, "") for q in quotes]

        # Step 4: Save and return the list of quotes
        self.quotes = quotes
        return quotes

    def generate_quote(self):
        return random.choice(self.quotes)

    def Typer(self):
        """Component with instructions, audio player, user input, and correction."""
        message = self.get_message()

        formatted_symbols = "".join(list(self.symbols)).strip()
        st.markdown(f"*Available symbols:* **{formatted_symbols}**")

        with st.form(key=self.label, clear_on_submit=True):
            user_input = st.text_input("**:blue[Type what you hear] 👇**")

            if st.form_submit_button("Submit"):
                user = user_input.upper()
                answer = message.upper()
                output = ""

                for i in range(len(user)):
                    if i >= len(answer):
                        output += f":red[{user[i:]}]"
                        break

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
