def quick_sort(arr):
    # Base case: an empty list or a list with one element is already sorted
    if len(arr) <= 1:
        return list(arr)  # Returns a new list to avoid modifying the original if it's empty
    
    # Choose the first element as the pivot
    pivot = arr[0]
    
    # Partition the list into three sublists
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
