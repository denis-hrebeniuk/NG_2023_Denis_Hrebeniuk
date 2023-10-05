import math


def request_number(text):
    return float(input(text))


def calculate(action, first_number):
    match action:
        case "+":
            second_number = request_number("Enter the second number: ")
            result = first_number + second_number
        case "-":
            second_number = request_number("Enter the second number: ")
            result = first_number - second_number
        case "*":
            second_number = request_number("Enter the second number: ")
            result = first_number * second_number
        case "/":
            second_number = request_number("Enter the second number: ")
            result = first_number / second_number
        case "root":
            result = math.sqrt(first_number)
        case "exponent":
            exponent = request_number("Enter exponent: ")
            result = first_number ** exponent
        case _:
            print("Error, you have selected an unknown action ._.")
    return result


if __name__ == "__main__":
    action = input("Select the required action (+, -, *, /, root, exponent): ")
    first_number = request_number("Enter the first number: ")
    print(f"Result: {calculate(action, first_number)}")
