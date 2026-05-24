# Ask user what to do
print("What should I do(recover/study)?")
activity = input()

#Decide if user should recover or study
if activity == "recover":

    #Ask user how they want to recover
    print("How would you like to recover(sleep/socialise)?")
    recover_by = input()

# Decide if user should sleep or socialise
    if recover_by == "sleep":
        print("zzzzZZZZzzzz")
    else:
        print("I will text my friend")
else:
    print("I will study!")