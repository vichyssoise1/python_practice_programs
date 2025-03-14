# Initialize empty set
numbers = []

# Continuously ask for user input until an invalid entry is provided.
while True:
    try:
        num = int(input("Enter a number: "))
        numbers.append(num)
    except ValueError:
        break
    
# Print the numbers entered to verify input collection.
print("Numbers entered:", numbers)