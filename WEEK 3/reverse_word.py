phrase = input("What phrase do you want to see in reverse?")
print("\nReversing...\n")

reversed_phrase = ""
for char in phrase:
    reversed_phrase = char + reversed_phrase

print(f"The phrase is : {reversed_phrase}")
