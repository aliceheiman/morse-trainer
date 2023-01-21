def get_symbol_message(symbols, bold=False):
    symbol_message = []
    for i, s in enumerate(symbols[::-1]):
        if i == 1:
            symbol_message.append("and")
        elif i > 1:
            symbol_message.append(",")

        if bold:
            symbol_message.append(f"**{s}**")
        else:
            symbol_message.append(s)

    symbol_message = reversed(symbol_message)
    symbol_message = " ".join(symbol_message)
    symbol_message = symbol_message.replace(" ,", ",")

    return symbol_message


first = lambda x: [s[0] for s in x]
second = lambda x: [s[1] for s in x]
third = lambda x: [s[2] for s in x]
