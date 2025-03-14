# Initialize an empty list to store valid numbers.
numbers = []

# Continuously ask for user input until an invalid entry is provided.
while True:
    try:
        # Prompt the user for a number and convert it to a float.
        num = int(input("Enter a number: "))
        numbers.append(num)
    except ValueError:
        break
# Calucalte the average
if numbers:
    average = sum(numbers) / len(numbers)
    print("The Average is: ", average)
else:
    print("No valid numbers")