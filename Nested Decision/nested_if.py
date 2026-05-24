
cover = input("What type of cover does the book have?\n")

if cover == "soft":
    perfect_bound = input("Is the book perfect bound?\n")

    if perfect_bound == "yes":
        print("Soft cover,perfect bound books are verry popular!")
    else:
        print("Soft covers with coils or stiches are great")

elif cover == "hard":
    print("Books with hard cover can be expensive")
