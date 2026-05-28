def sum_weights(char_weight,inv_weight):
    total = char_weight + inv_weight
    return total

def calc_avg_weight(char_weight,inv_weight):
    total_sum = sum_weights(char_weight,inv_weight)
    average = total_sum / 2
    return average
#function 3
def run():
    character_weight = int(input("What is the weight of the inventory?\n"))
    inventory_weight = int(input("What is the weight of the inventory?\n"))

    action = input("Would you like to calculate 'sum' or 'avg'?\n")
    if action == "sum":
        result = sum_weights(character_weight, inventory_weight)
        print(f"The total weight is : {result}")

    elif action =="average":
        result = calc_avg_weight(character_weight, inventory_weight)
        print(f"The average weight is : {result}")

    else:
        print("Invalid option selected.")

run()