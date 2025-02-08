# 2025-02-08 Steve
# In Python, you can create a list with all entries being the same 
# using several methods. 
#   1) Using List Multiplication
#   2) Using a List Comprehension
#   3) Using the list() Constructor with repeat from itertools. (not shown)

print("*********************")
print("Using List Multiplication")
print("*********************")
# Create a list with 3 entries, all of the same value.

print("A boolean list...")
list = [True] * 3
print(list)

print("\nAn integer list...")
row = [0] * 3
print(row)

print("\nA list of lists...")
matrix = [row] * 3
print(matrix)

print("\n\n***************************")
print("Using a List Comprehension")
print("***************************")

print("A boolean list...")
same_value_list = [False for _ in range(3)]
print(same_value_list)

print("\nAn integer list...")
same_value_list = [1 for _ in range(3)]
print(same_value_list)

print("\nA list of lists...")
matrix2 = [ same_value_list for _ in range(3)]
print(matrix2)
