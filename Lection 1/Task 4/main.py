import operator

operators = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
}


def request_input_in_float(text):
    return float(input(text))


def calculate(action, first_number):
    result = None

    match action:
        case "+" | "-" | "*" | "/":
            second_number = request_input_in_float("Enter the second number: ")
            result = operators[action](first_number, second_number)
        case "root":
            exponent = request_input_in_float("Enter exponent of the root: ")
            result = first_number ** (1 / exponent)
        case "exponent":
            exponent = request_input_in_float("Enter exponent: ")
            result = first_number ** exponent
        case _:
            result = None
    
    return result


if __name__ == "__main__":
    action = input("Select the required action (+, -, *, /, root, exponent): ")
    first_number = request_input_in_float("Enter the number: ")

    result = calculate(action, first_number)
    if result:
        print(f"Result: {result}")
    else:
        print("Error, you have selected an unknown action ._.")