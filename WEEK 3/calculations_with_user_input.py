#Step 1 : ask the user how many nr they want to sum
numbers = int(input("How many numbers should I sum up?"))

#Step 2:Initialise variables
running_total = 0
counter = 1

#step 3.Run the loop until we reach the total
while counter <= numbers:
    user_num = int(input(f"Please enter number {counter} of {numbers} :"))
    running_total = running_total + user_num

    counter = counter + 1
print(f"The answer is {running_total}.")
