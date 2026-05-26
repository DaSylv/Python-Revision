#we show the message what it must be print
print("Calculating the sum of the first 100 numbers...")

#prepare variables
total_sum = 0
current_number = 1 #we start adding from 1

#build the while loop
while current_number <= 100:
    total_sum = total_sum + current_number
    current_number = current_number + 1
print(f"...Done!The answer is  {total_sum}")