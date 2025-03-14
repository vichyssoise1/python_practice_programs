# Initialize 'highest' to None to track the highest valid number.
highest = None

# Continuously ask for input until an invalid entry is provided.
while True:
    try:
        # Prompt the user for a number and convert it to a float.
        num = float(input("Enter a number: "))
    except ValueError:
        # Exit the loop if the input is invalid (non-numeric).
        break
    
# Update 'highest' if this is the first valid input or if the current number is higher.
if highest is None or num > highest:
    highest = num