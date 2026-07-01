def rotate_array(arr, d):
    n = len(arr)

    #Check if 'd' is valid,it should be within the range of array len
    if d < 0 or d>= n:
        return "Invalid rotation value."

    #Create a new array to store the rotated elements.
    rotated_arr = [0] *n

    #perform the rotation.
    for i in range (n):
        rotated_arr[i] = arr [(i +d)%n]

    return rotated_arr

#input_array
arr = [1,2,3,4,5]

#number of position to rotate
d = 2

#call the rotate_array function
result =rotate_array(arr,d)

#print the rotated array
print("Original Array:",arr)
print("Rotated Array:",result)