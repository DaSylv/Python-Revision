# Division
num1 = float(input("Enter the divident  for division:"))
num2 = float(input("Enter the divisor for division:"))

if num2 == 0:
    print("Error: Division by zero is not allowed.")

else:
    div_result = num1 /num2
    print(f"Division: {num2}/ {num2} = {div_result}")