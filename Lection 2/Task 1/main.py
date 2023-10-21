elements = input("Enter any items (enter with a space): ").split()
print(f"Your list of items (only unique items will be displayed): {list(set(elements))}")