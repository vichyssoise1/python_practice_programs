#initialize variable
even_count = 0

#add for loop to ask for 10 numbers
for _ in range(10):
    if int(input("Enter a number: ")) % 2 == 0:
        even_count += 1
print("Even count: ",even_count)