symbols = ("-", ",", ".", "!", "?")

with open("text.txt") as file:
    text = file.readlines()

for idx in range(0, len(text), 2):

    for symbol in symbols:
        text[idx] = text[idx].replace(symbol, "@")

    print(*text[idx].split()[::-1], sep=' ')

