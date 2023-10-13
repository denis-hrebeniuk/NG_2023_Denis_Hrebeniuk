import sys


sys.path.append("..") # Import util.py by changing directory to ../
from util import request_list

def is_valid_integer(element):
    try:
        int(element)
        return True
    except ValueError:
        return False

unique_list = request_list()
numbers_list = []
for element in unique_list:
    if is_valid_integer(element):
        numbers_list.append(int(element))
    else:
        continue

print(f"You've entered {len(numbers_list)} numbers. List of the numbers you have entered: {numbers_list}")