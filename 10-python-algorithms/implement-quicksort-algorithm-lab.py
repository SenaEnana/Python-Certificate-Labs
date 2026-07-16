def quick_sort(arr):

    if len(arr) <= 1:
        return list(arr) 

    pivot = arr[0]
    
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)