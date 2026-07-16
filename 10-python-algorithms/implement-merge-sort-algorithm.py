def merge_sort(array):
    
    middle_point = len(array) // 2
    left_part = array[:middle_point]
    right_part = array[middle_point:]
    merge_sort(left_part)
    merge_sort(right_part)
    left_array_index = 0
    right_array_index = 0
    sorted_index = 0 