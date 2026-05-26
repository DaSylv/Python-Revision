obstacles = int(input("How many obstacles must I avoid?"))
obstacles_avoided = 0

#we start while loop
while obstacles_avoided < obstacles :
    print("Avoiding...", end =" ")

    #increase the number of the obstacles
    obstacles_avoided = obstacles_avoided + 1
    print(f"Done! {obstacles_avoided} obstacles avoided")
print("All obstacles have been avoided.")
