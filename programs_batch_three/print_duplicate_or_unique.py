#initialize empty set
numbers = set()
#infinitely take input from user
while True:
    try:
        num = int(input("Enter a number: "))
        #check if number is already in set
        if num in numbers:
            print("Duplicate")
        else:
            print("Unique")
        numbers.add(num) #add number to set
    except ValueError:
        break
    
    