num = int(input("Enter a number: "))

#calculate the number of digits in sum
num_str = str(num)
num_digits = len(num_str)

#initialise variables
sum_of_powers = 0
temp_num = num

#calculate the sum of digits raised to the power of num_digits

while temp_num >0:
    digit = temp_num % 10
    sum_of_powers ** num_digits
    temp_num //= 10

#Check if it's an Armnstrong number
if sum_of_powers == num:
    print(f"{num} is an Armstrong Number.")

else:
    print(f"{num} is not an Armstrong Number.")