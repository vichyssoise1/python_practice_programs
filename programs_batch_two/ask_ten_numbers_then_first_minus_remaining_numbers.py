#add user input to the list and for loop to ask 10 times
a, *rest = [int(input("Enter a number: ")) for _ in range(10)]
#subtract the remaining numbers from the first number
print(a - sum(rest))