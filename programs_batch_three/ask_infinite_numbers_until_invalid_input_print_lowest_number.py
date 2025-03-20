# Initialize the variable
lowest = None

# Loop infinitely until the user inputs an invalid number
while True:
    try:
        num = int(input("Enter a number: "))

        # Check if it's the lowest number
        if lowest is None or num < lowest:
            lowest = num

    except ValueError:
        break  # Stop the loop when input is invalid

# Print the lowest number if there was at least one valid input
if lowest is not None:
    print("Lowest number:", lowest)
else:
    print("No valid numbers")
