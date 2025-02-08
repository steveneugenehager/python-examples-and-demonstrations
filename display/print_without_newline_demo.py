# 2025-02-08 Steve
# print_without_newline_demo.py
# In Python, you can print a string without a carriage return (which 
# starts a new line) by using the end parameter of the print() 
# function. By default, print() adds a newline character (\n) at the 
# end of the output. You can change this behavior by specifying a 
# different value for end.

cars = ['audi', 'bmw', 'subaru', 'toyota']

print(f"The list is: {cars}.")

print("Demonstrate how to print with a different EOL marker(\":\"):")
for car in cars:
    print(car == 'bmw',end=':')
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

print("Demonstrate how to print with a different EOL marker(\"tab\"):")
for car in cars:
    print(car == 'bmw',end='\t')
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

print("Demonstrate how to print with a different EOL marker(\"</tag>\"):")
for car in cars:
    print(car == 'bmw',end='</tag>')
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

print("Demonstrate how to print without a newline (EOL marker):")
for car in cars:
    print(car == 'bmw',end='')
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())


