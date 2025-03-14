#initialize empty varaible list
numbers = []

# Continuously ask for user input until an invalid entry is given
while True:
    try:
        #Ask for user input
        num = int(input("Enter a number: "))
        numbers.append(num)
    except ValueError:
        break