#ask for ten numbers
numbers = [int(input("Enter a number: ")) for _ in range(10)]
unique_numbers =[]
# Create a new list that contains only the first occurrence of each number
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)
        