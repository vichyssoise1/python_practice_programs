#initialize empty set
numbers = set()
#infinitely take input from user
while True:
    try:
        num = int(input("Enter a number: "))
        numbers.add(num) #add number to set
    except ValueError:
        break
    
    