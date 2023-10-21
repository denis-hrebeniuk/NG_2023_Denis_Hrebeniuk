elements = input("Enter any items (enter with a space): ").split()

numbers_list = []
for element in elements:
    try:
        number = int(element)
        numbers_list.append(number)
    except ValueError:
        continue

print(f"You've entered {len(numbers_list)} numbers. List of the numbers you have entered: {numbers_list}")