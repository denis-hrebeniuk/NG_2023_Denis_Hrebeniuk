import json
import os


def find_value_by_key(array, desired_key):
    for item_key, item_value in array.items():
        if item_key == desired_key:
            print(f"\nYour key has been found in JSON (key: {desired_key}):\n{item_value}")
            return

        if type(item_value) is dict:
            find_value_by_key(item_value, desired_key)


file_name = input("Enter the name of file, where you json stored: ")
data_key = input("Enter the key, which value you want to get: ")

if os.path.isfile(file_name) is False:
    print("\nFile not found, check that the file name is entered correctly!")
    exit()

with open(file_name, "r") as file:
    data = json.loads(file.read())
    find_value_by_key(data, data_key)
