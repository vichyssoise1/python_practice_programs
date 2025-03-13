#initialize variable
odd_count = 0
#set up loop to ask user for 10 numbers
for _ in range(10):
    if int(input("Enter a number: ")) % 2:
        odd_count += 1
print("Odd count: ",odd_count)