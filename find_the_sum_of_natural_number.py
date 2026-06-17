limit = int(input("Enter the limit:"))

#initialise the sum
sum = 0

#use a for loop to calculate the sum of natural numbers
for i in range(1,limit+1):
    sum += i

#print the sum
print("The sum of natural numbers up to",limit,"is",sum)