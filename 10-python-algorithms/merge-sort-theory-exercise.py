# Questions

#1 What is the divide and conquer paradigm in computer science?

# A technique for detecting a cycle in function value iterations using just two iterators.

# An algorithm for comparing two elements and swapping them from smallest to largest if needed.

# A technique for recursively breaking down problems into smaller sub-problems.///correct

# An algorithm to compute the shortest connecting network for points in a plane.

#2 What is the time complexity for the merge sort algorithm?

# O(n log n)

# O(log n²)

# O(n³ log n)

# O(log n³)

#3 What is the space complexity for the merge sort algorithm?

# O(n²)

# O(1)

# O(n log n)

# O(n)


# /////////////

# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr

#     mid = len(arr) // 2
#     left = merge_sort(arr[:mid])
#     right = merge_sort(arr[mid:])

#     sorted_list = []
#     i = 0
#     j = 0

#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             sorted_list.append(left[i])
#             i += 1
#         else:
#             sorted_list.append(right[j])
#             j += 1

#     sorted_list.extend(left[i:])
#     sorted_list.extend(right[j:])

#     return sorted_list


# The time complexity for merge sort would be O(n log n) because the list is continuously divided in half (log n) and then merged together (O(n)). 
# Unlike other sorting algorithms like bubble sort, merge sort is not sorted in place and has a space complexity of O(n).