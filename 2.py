def move_zeros_to_end(arr):
    count = 0 
    
    # Traverse the array and move non-zero elements to the front
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[count] = arr[i]
            count += 1
    
    # Fill the rest of the array with zeros
    while count < len(arr):
        arr[count] = 0
        count += 1
    
    return arr

arr = [4, 5, 0, 1, 9, 0, 5, 0]
N = len(arr)

result = move_zeros_to_end(arr)

print(f"Array after moving zeros to the end: {result}")