import os


file_name = input("Enter the name of file, you want to open: ")

if os.path.isfile(file_name) is False:
    print("\nFile not found, check that the file name is entered correctly!")
    exit()

symbols = {}
with open(file_name, "r") as file:
    content = file.read()

    print(f"Number of characters in the text: {len(content)}")

    for symbol in content:
        if symbol in symbols:
            symbols[symbol] += 1
        else:
            symbols[symbol] = 1

print(symbols)
