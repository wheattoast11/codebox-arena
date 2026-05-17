def count_inversions(arr):
    """
    Count the number of inversions in the input list using a modified merge sort.
    An inversion is a pair (i, j) such that i < j and arr[i] > arr[j].
    Time complexity: O(n log n)
    """
    if not arr or len(arr) <= 1:
        return 0
    
    # Helper function for merge sort that returns (sorted_arr, inversion_count)
    def merge_sort(arr):
        n = len(arr)
        if n <= 1:
            return arr, 0
        
        mid = n // 2
        left, left_count = merge_sort(arr[:mid])
        right, right_count = merge_sort(arr[mid:])
        
        merged = []
        i = 0
        j = 0
        inv_count = left_count + right_count
        
        # Merge the two sorted halves
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                # All remaining elements in left (from i to end) are greater than right[j]
                # because left is sorted. So each contributes an inversion with right[j].
                merged.append(right[j])
                j += 1
                inv_count += (len(left) - i)
        
        # Append any remaining elements
        merged.extend(left[i:])
        merged.extend(right[j:])
        
        return merged, inv_count
    
    _, count = merge_sort(arr)
    return count
