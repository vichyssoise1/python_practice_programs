#ask user input for a number
numbers = int(input("Enter a number: "))

#empty list to store duplicates
duplicates = []
#loop to check for duplicates
for num in numbers:
    if numbers.count(num) > 1 and num not in duplicates:
        duplicates.append(num)

# Print the numbers to verify input collection.
print("Numbers entered:", numbers)  