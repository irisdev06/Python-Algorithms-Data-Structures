def merge_sort(arr):

    if len(arr) <= 1:
        return arr
# Divide the list into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
 # Recursively sort the two halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
# Merge the sorted halves
    sorted_arr = merge(left_half, right_half)
    return sorted_arr