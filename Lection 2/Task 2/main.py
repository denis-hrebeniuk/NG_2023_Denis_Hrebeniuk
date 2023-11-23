elements = input("Enter any items (enter with a space): ").split()

numbers_list = []
for element in elements:
    if element.isdigit():
        numbers_list.append(element)

print(f"You've entered {len(numbers_list)} numbers. List of the numbers you have entered: {numbers_list}")