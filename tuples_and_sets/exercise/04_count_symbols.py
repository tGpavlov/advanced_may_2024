text = input()

unique_symbols = set()

for symbol in text:
    unique_symbols.add(symbol)

for symbol in sorted(unique_symbols):
    print(f"{symbol}: {text.count(symbol)} time/s")

