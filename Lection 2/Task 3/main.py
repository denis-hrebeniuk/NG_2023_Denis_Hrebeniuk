final_number = int(input("Firstly, let's build a table with all the numbers from 1 to the number you specify and all the numbers that are multiples of them.\nEnter the final number: "))
if final_number < 0:
    print("Ooops... You have entered a number that is negative!")
    exit()

# First subtask
print("=" * 64)
print("Number\tNumbers, by which a number is divisible without remainder")
for number in range(1, final_number):
    multiples = []
    for divider in range(1, number + 1):
        if number % divider == 0:
            multiples.append(divider)
    print(f"{number}\t{multiples}")
    

# Second subtask (https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)
print("=" * 64)
print("Nice! Here's a list of all the prime numbers up to the number you entered:")
natural_numbers = list(range(2, int(final_number)))
for number in range(2, final_number):
    if number in natural_numbers:
        if number * number < final_number:
            for natural_number in natural_numbers.copy():
                if natural_number != number and natural_number % number == 0:
                    natural_numbers.remove(natural_number)
print(natural_numbers)