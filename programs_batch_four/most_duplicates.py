from collections import Counter

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
    
# Check if any valid numbers were entered
if not numbers:
    print("No valid numbers entered.")
else:
    # Count the frequency of each number
    count = Counter(numbers)

print(numbers)
