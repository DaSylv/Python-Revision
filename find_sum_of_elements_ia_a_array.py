#function to find the sum of elements in a array
def sum_of_array(arr):
    total = 0 #initialise a variable to store the sum

    for element in arr:
        total += element #add each element to the total
    return total

#example usage:
array=[1,2,3]
result= sum_of_array(array)
print("Sum of the array:",result)