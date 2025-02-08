# 2025-02-08 Steve
# print_without_newline_demo.py
# In Python, you can print a string without a carriage return (which 
# starts a new line) by using the end parameter of the print() 
# function. By default, print() adds a newline character (\n) at the 
# end of the output. You can change this behavior by specifying a 
# different value for end.

# v2 - simplified for demo purposes.

cars = ['audi', 'bmw', 'subaru', 'toyota']

print(f"The list is: {cars}.")

print("\nDemonstrate how to print with a different EOL marker(\":\"):")
for car in cars:
    print(car,end=':')
    print(car.title())

print("\nDemonstrate how to print with a different EOL marker(\"tab\"):")
for car in cars:
    print(car,end='\t')
    print(car.title())

print("\nDemonstrate how to print with a different EOL marker(\"</tag>\"):")
for car in cars:
    print(car,end='</tag>')
    print(car.title())

print("\nDemonstrate how to print without a newline (EOL marker):")
for car in cars:
    print(car,end='')
    print(car.title())

exit