s = input("Enter a string: ")
char = input("Enter the character to find: ")

count = 0

for ch in s:
    if ch == char:
        count += 1

print("Frequency of", char, "=", count)
