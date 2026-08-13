numbers = [10, 21, 32, 45, 56, 67, 78, 89, 90, 11, 24, 35, 46, 57, 68]
print("list of numbers:",numbers)
even = 0
odd = 0
for num in numbers:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
print("Even numbers:", even)
print("Odd numbers:", odd)
