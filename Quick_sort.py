def quicksort(arr, left, right):                        #fuction of quicksort
    if left < right:
        partition_pos = partition(arr, left, right) 
        quicksort(arr, left, partition_pos - 1)         # recursive call for left sub array
        quicksort(arr,partition_pos + 1, right)         # recursive call for right sub array
                                    
def partition(arr, left, right):                        # Partition algorithm   
    i = left
    j = right - 1
    pivot = arr[right]
    
    while i < j:
        while i < right and arr[i] < pivot:             # finding values that are below and above pivot
            i += 1
        while j > left and arr[j] >= pivot:
            j -= 1
        
        if i < j:                                       # swapping the values
            arr[i], arr[j] = arr[j], arr[i]
            
        if arr[i] > pivot:
            arr[i], arr[right] = arr[right], arr[i]
            
    return i
        
arr = [89,76,56,99,35,67,43,79]
print("Unsorted Array: ")
print(arr)
quicksort(arr, 0, len(arr) - 1 )
print("Sorted Array: ")
print(arr)

