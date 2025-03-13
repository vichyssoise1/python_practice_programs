#add list to collect numbers from user input asking 10 times
numbers = [int(input("Enter a number: ")) for _ in range(10)]
#add logic to filter out unique numbers from the list
unique_numbers = [num for num in numbers if numbers.count(num) == 1]
#add print statement to display unique numbers
print(unique_numbers)