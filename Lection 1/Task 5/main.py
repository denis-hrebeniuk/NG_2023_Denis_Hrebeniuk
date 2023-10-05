import math


# Returns opposite integer
def opposite(number):
    return -number


print("Note: if your quadratic equation is incomplete, simply specify 0 in the missing values")
a = int(input("Please, enter A number: "))
b = int(input("Please, enter B number: "))
c = int(input("Please, enter C number: "))

if a != 0 and b != 0 and c != 0:
    discriminant = (b * b) - (4 * a * c)
    if discriminant > 0:
        first_root = (-b + math.sqrt(discriminant)) / (2 * a)
        second_root = (-b - math.sqrt(discriminant)) / (2 * a)
        print(f"Discriminant: {discriminant}, first root: {first_root}, second root: {second_root}")
    elif discriminant == 0:
        root = -(b / (2 * a))
        print(f"Since the discriminant is 0, the only root is {root}")
    elif discriminant < 0:
        print(f"Discriminant: {discriminant}. Equation has no real roots, no further solution is possible")
elif a != 0 and c != 0 and b == 0:
    x2 = -c / a
    if x2 < 0:
        print("No further solution to the quadratic equation is possible, the root cannot be negative")
    else:
        first_root = math.sqrt(x2)
        second_root = -math.sqrt(x2)
        print(f"First root: {first_root}, second root: {second_root}.")
elif a != 0 and b != 0 and c == 0:
    print(f"Result: x = 0 or x = {opposite(b) / a}")
