#initialize empty list to store the valid numbers
numbers = []

# Continue to ask for input until the user types an invalid number
while True:
    try:
        # Ask for a number
        num = int(input("Enter a number: "))
        numbers.append(num)
    except ValueError:
        break
print(numbers)
