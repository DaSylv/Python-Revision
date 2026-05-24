first_number = int(input("Please enter the first whole number:"))
second_number = int(input("Please enter the second whole number:"))
third_number = int(input("Please enter the third number:"))

even_count = even_count = 0
odd_count = odd_count = 0

#we check first number
if first_number % 2 == 0:
    even_count = even_count +1
else:
    odd_count = odd_count + 1

# we check the second number
if second_number % 2 ==0:
    even_count = even_count+1
else:
    odd_count = odd_count+1

# we check the third number
if third_number % 2 ==0:
    even_count = even_count+1
else:
    odd_count = odd_count+1

# we show the result
print(f"There were{even_count} even and {odd_count} odd numbers")