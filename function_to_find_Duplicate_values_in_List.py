#Program to Write a function to find Duplicate values in the List
integers = input("Enter the integers: ")
integers = integers.split()
integers = [int(val) for val in integers]
unique = set()
duplicates = set()

for val in integers:
    if val in unique:
        duplicates.add(val)
    else:
        unique.add(val)

print("Duplicates values are ", list(duplicates))
