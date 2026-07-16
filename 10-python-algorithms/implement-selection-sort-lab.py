def selection_sort(arr):
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
        # Find the minimum element in the remaining unsorted array
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
                
        # Swap the found minimum element with the first unsorted element
        # Only perform the swap if the minimum is not already in the correct position
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            
