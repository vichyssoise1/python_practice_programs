#ask user input for two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
#check if the first number is greater than the second number
if num1 > num2:
    #if the first number is greater than the second number, swap the two numbers
    num1, num2 = num2, num1