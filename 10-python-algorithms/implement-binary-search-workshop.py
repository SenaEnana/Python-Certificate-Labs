def binary_search(search_list, value):
    path_to_target = []
    low = 0
    high = len(search_list) - 1
    
    while low <= high:
        mid = (low + high) // 2
        value_at_middle = search_list[mid]
        path_to_target.append(value_at_middle)
        
        if value == value_at_middle:
            return path_to_target
        elif value > value_at_middle:
            low = mid + 1
        else:
            high = mid - 1
    
    return []

print(binary_search([1, 2, 3, 4, 5], 3))
print(binary_search([1, 2, 3, 4, 5, 9], 4))