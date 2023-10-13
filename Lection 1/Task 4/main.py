import math


def request_input_in_float(text):
    return float(input(text))


def calculate(action, first_number):
    if action in ["+", "-", "*", "/"]:
        second_number = request_input_in_float("Enter the second number: ")
    elif action == "exponent":
        second_number = request_input_in_float("Enter exponent: ")

    match action:
        case "+":
            result = first_number + second_number
        case "-":
            result = first_number - second_number
        case "*":
            result = first_number * second_number
        case "/":
            result = first_number / second_number
        case "root":
            result = math.sqrt(first_number)
        case "exponent":
            result = first_number ** second_number
        case _:
            print("Error, you have selected an unknown action ._.")
    return result


if __name__ == "__main__":
    action = input("Select the required action (+, -, *, /, root, exponent): ")
    first_number = request_input_in_float("Enter the first number: ")
    print(f"Result: {calculate(action, first_number)}")
