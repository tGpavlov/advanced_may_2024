from string import punctuation

with open("text.txt") as file:
    text = file.readlines()

result = []

for idx in range(len(text)):

    line = text[idx]
    letters = 0
    punc_marks = 0

    for symbol in text[idx]:
        if symbol.isalpha():
            letters += 1
        elif symbol in punctuation:
            punc_marks += 1

    result.append(f"Line {idx + 1}: {line.strip()[:-1]}({letters})({punc_marks})")


with open("output.txt", "w") as output_file:
    output_file.write('\n'.join(result))