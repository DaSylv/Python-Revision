kilometres = float(input("Enter the distances in kilometres:"))

#Conversion factor: 1 kilometer = 0.621371 miles
conversion_factor = 0.621371

miles = kilometres * conversion_factor
print(f"{kilometres} kilometres is equal to {miles} miles")