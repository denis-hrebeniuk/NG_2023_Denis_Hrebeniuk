print("1. Convert degrees Celsius to Fahrenheit")
print("2. Convert degrees Fahrenheit to Celsius")
task_type = int(input("Select the desired conversion: "))
degrees = float(input("How many degrees is it now? "))

if task_type == 1:
    print(f"By my calculations, in degrees Fahrenheit it comes out {degrees * 1.8 + 32} degrees")
elif task_type == 2:
    print(f"By my calculations, in degrees Celsius it comes out {(degrees - 32) / 1.8} degrees")
else:
    print("Error, no selected degree conversion ¯\_(ツ)_/¯")