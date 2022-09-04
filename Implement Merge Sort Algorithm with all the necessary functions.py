def merge(x,y,arr):                   # Python program for implementation of MergeSort
    i = j = k = 0
    while i < len(x) and j < len(y):
        if x[i] <= y[j]:              #compare first elements of two arrays
            arr[k] = x[i]        
            i+=1
        else:                         #process stops when while condition is terminated
            arr[k] = y[j]
            j+=1
        k+=1

    while i < len(x):                
        arr[k] = x[i]
        i+=1
        k+=1

    while j < len(y):
        arr[k] = y[j]
        j+=1
        k+=1
        
def merge_sort(arr):
    if len(arr) <= 1:
        return
      
    mid = len(arr)//2                # Finding the mid of the array

    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    merge(left, right, arr)         #now we merge two sorted arrays in merge function


Array=[9,7,1,6,9,4]
merge_sort(Array)
print(Array)
