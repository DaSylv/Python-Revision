#Ask the user for the number of rows and colomns
rows = int(input("How many rows should I have?"))
columns = int(input("How many columns should I have?"))
#Print the transition
print("\nHere I go:\n")

for r in range(rows):
    for c in range(columns):
        print(":)", end="")
        print()
print("\nDone!")