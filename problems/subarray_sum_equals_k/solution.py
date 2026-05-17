def count_subarrays_with_sum(arr, k):
    """
    Returns the number of contiguous subarrays whose sum equals k.
    Uses prefix sum + hashmap for O(n) time complexity.
    """
    count = 0
    current_sum = 0
    # Map from prefix sum to its frequency
    prefix_sum_counts = {0: 1}
    
    for num in arr:
        current_sum += num
        # If (current_sum - k) exists in the map, it means there are
        # subarrays ending at current position with sum k
        if (current_sum - k) in prefix_sum_counts:
            count += prefix_sum_counts[current_sum - k]
        
        # Update the frequency of current prefix sum
        prefix_sum_counts[current_sum] = prefix_sum_counts.get(current_sum, 0) + 1
    
    return count
