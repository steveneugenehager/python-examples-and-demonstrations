# 2025-02-08 Steve Hager
# is_prime() came from ChatGPT

def is_prime(n):
    """Return True if n is a prime number, else False."""
    if n <= 1:
        return False  # 0 and 1 are not prime numbers
    for i in range(2, int(n ** 0.5) + 1):  # Steve-Check up to the sqrt of n.
        if n % i == 0:
            return False  # n is divisible by i, thus not prime
    return True  # n is prime if no factors were found

# Get two numbers and check all the numbers in the range.

user_range = [ ]
# Prompt the user to input two numbers.
for i in range(0,2):
    user_input = int(input("Please enter an integer: "))
    if user_input < 1:
        user_input = 1
    user_range.append(user_input)

start=min(user_range)
end=max(user_range)

print(f"Your range is: [ {start} , {end} ].")

for i in range(start,end+1):
    if is_prime(i):
        print(f"Is {i} prime? {is_prime(i)}")

exit
