def request_list():
    print("Enter any item (number, word, etc.). To finish entering items, enter \"stop this list\" as the item.")

    arr = []
    while True:
        element = input("Enter an element: ")
        if element == "stop this list":
            break

        arr.append(element)

    return arr