# Initialize empty set
numbers = []

# Continuously ask for user input until an invalid entry is provided.
while True:
    try:
        num = int(input("Enter a number: "))
        numbers.append(num)
    except ValueError:
        break
    
numbers.sort(reverse=True)
    
# Print the result of numbers highest to lowest
print("Numbers from highest to lowest:  ", numbers)