#ASk the user for the requirement brightness level
brightness = int(input("what level of brightness is required?"))

#step 2:print the initialise
print("\nAdjusting brightness...\n")
#step 3.Loop even numbers
for i in range(2,brightness + 1, 2):
    print(f"Brightness level: {'*'* i}")
print("Complete!")
