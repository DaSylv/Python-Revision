sequence = input("Please enter a sequence:\n")
marker = input("Please enter a marker:\n")
parts = sequence.split(marker)
content_between = parts[1]
distance = len(content_between)
print(f"The distance between the markers is {distance}.")