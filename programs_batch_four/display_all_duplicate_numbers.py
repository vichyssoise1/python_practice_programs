# Ask the user to input 10 numbers and store them in a list
numbers = [int(input("Enter a number: ")) for _ in range(10)]

# Empty list to store duplicates
duplicates = []

# Loop through the list to check for duplicates
for num in numbers:
    # If the number appears more than once and hasn't been recorded yet, it's a duplicate
    if numbers.count(num) > 1 and num not in duplicates:
        duplicates.append(num)

# Print the duplicate numbers
print("Duplicates are:", duplicates)
