def count_pairs_with_sum(arr, target):
    count = 0
    freq = {}
    for num in arr:
        complement = target - num
        if complement in freq:
            count += freq[complement]
        freq[num] = freq.get(num, 0) + 1
    return count
