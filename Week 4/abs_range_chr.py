print("Program Started!")
user_input = input("Please enter an ASCII code:")
#Ask the user for an ASCII code
code= abs(int(user_input))
if code in range (32, 127):
    character = chr(code)
    print(f"The character represented by the ASCII code {code} is:{character}")
else:
    print("Error: The code entered is not within the printable range (32 -126)")
print("Program Ended!")
