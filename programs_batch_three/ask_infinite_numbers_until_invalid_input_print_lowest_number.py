#loop infinitely until the user inputs an invalid number
while True:
    try:
        num = int(input("Enter a number: "))
    except ValueError:
        break