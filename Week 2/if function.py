age = int(input("Enter your age:"))
if age < 12 :
    ticket_price = 0
    print("Entry is free")

elif age > 65 :
    ticket_price = 10
    print("Senior Discount")
else :
    ticket_price = 15
    print(f"ticket is {ticket_price}")
