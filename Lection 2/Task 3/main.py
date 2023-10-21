final_number = int(input("Firstly, let's build a table with all the numbers from 1 to the number you specify and all the numbers that are multiples of them.\nEnter the final number: "))
if final_number < 0:
    print("Ooops... You have entered a number that is negative!")
    exit()

# First subtask
print("=" * 64)
print("Number\tNumbers, by which a number is divisible without remainder")
number = 1
while number < final_number:
    multiples = []
    divisible = number
    while divisible > 0:
        if number % divisible == 0:
            multiples.append(divisible)
        
        divisible -= 1
    print(f"{number}\t{multiples}")
    number += 1

# Second subtask
print("=" * 64)
print("Nice! Here's a list of all the prime numbers up to the number you entered:")
number = 1
prime_numbers = []
while number < final_number:
    if number % 2 != 0:
        prime_numbers.append(number)
    number += 1
print(prime_numbers)