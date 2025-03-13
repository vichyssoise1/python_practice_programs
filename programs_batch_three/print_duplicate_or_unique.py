#initialize empty set
numbers = set()

while True:
    try:
        num = int(input("Enter a number: "))
    except ValueError:
        break
    