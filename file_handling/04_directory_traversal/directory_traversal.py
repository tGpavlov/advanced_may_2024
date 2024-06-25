import os


def save_file_types(dir_name, first_level=False):
    for filename in os.listdir(dir_name):
        file = os.path.join(dir_name, filename)

        if os.path.isfile(file):
            file_type = filename.split(".")[-1]

            if file_type not in file_types:
                file_types[file_type] = []
            file_types[file_type].append(filename)

        elif os.path.isdir(file) and not first_level:
            save_file_types(file, first_level=True)


directory = input()
file_types = {}
result = []

try:
    save_file_types(directory)
except FileNotFoundError:
    print("Directory not found!")


for types, files in sorted(file_types.items()):
    result.append(f".{types}")

    for file in sorted(files):
        result.append(f"- - - {file}")


with open("report.txt", "w") as report_file:
    report_file.write('\n'.join(result))