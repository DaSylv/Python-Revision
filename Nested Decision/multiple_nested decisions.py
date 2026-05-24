location= input("Where should I look?")

#Room 1 :Bedroom
if location == "In the bedroom":
    bedroom_look = input("Where in the bedroom should I look \n")

    if bedroom_look == "Under the bed":
        print("Found some shoes but no phone")
    else:
        print("Found some mess but no phone")

#Room 2:Bathroom
elif location == "in the bathroom":
    bathroom_look = input("Where in the bathroom should I look \n")
    if bathroom_look == "In the bathtub":
        print("Found a rubber duck but no phone")
    else :
        print("Found bathroom stuff")

#Room 3:Living Room
elif location == "in the living room":
    living_look = input("Where in the living room?")
    if living_look == ("On the table"):
        print("yessss,,,found my phone")
    else:
        print("Not found the phone")

else:
    print("I don't know where it is,but I will look")