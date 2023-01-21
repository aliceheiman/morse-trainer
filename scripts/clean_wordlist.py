with open("../common-words.txt") as f:
    contents = f.read().split("\n")

# remove duplicating patterns
words = [w for w in contents if (len(set(w)) > 2)]

words = [w for w in words if len(w) > 2]
words += [
    "I",
    "am",
    "us",
    "to",
    "a",
    "of",
    "in",
    "is",
    "by",
    "or",
    "be",
    "at",
    "as",
    "an",
    "we",
    "if",
    "do",
    "no",
    "he",
    "me",
    "my",
    "so",
    "go",
    "tv",
    "dr",
]

with open("word-test.txt", "w") as f:
    f.write("\n".join(words))
