#step 1:Display the initial question
#we use int ()because the int from the user must be treated as a number
steps = int(input("How far we are from the target?\n "))

#step2. Use a for loop to count down
#range(start,stop, step)
for i in range(steps,0,-1):
    print(f" {i} steps remaining")
#step 3.display the final message
print("Target achieved")