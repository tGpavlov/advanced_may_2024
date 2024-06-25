import os

while True:
    command, *info = input().split('-')

    if command == "End":
        break

    if command == "Create":
        file = open(f"{info[0]}", "w")
        file.close()

    elif command == "Add":
        file = open(f"{info[0]}", "a")
        file.write(f"{info[1]}\n")
        file.close()

    elif command == "Replace":
        try:
            with open(f"{info[0]}", "r") as file:
                text = file.read()

            text = text.replace(info[1], info[2])

            with open(f"{info[0]}", "w") as file:
                file.write(text)

        except FileNotFoundError:
            print("An error occurred")

    elif command == "Delete":
        try:
            os.remove(f"{info[0]}")

        except FileNotFoundError:
            print("An error occurred")


