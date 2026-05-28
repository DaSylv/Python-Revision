print("Program Started!")
char = input("Please enter a letter:\n")
if len(char) == 1:
    ascii_code = ord(char)
    print(f"The ASCII code for {char} is :{ascii_code}")
else:
    print("Error: You must enter exactly one character.")
print("Program Ended!")