def word_ladder(begin, end, word_list):
    if end not in word_list:
        return 0
    
    word_set = set(word_list)
    
    # BFS
    from collections import deque
    queue = deque([(begin, 1)])
    visited = {begin}
    
    while queue:
        current_word, length = queue.popleft()
        
        if current_word == end:
            return length
        
        # Generate all possible one-letter mutations
        for i in range(len(current_word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                if c == current_word[i]:
                    continue
                next_word = current_word[:i] + c + current_word[i+1:]
                
                if next_word in word_set and next_word not in visited:
                    visited.add(next_word)
                    queue.append((next_word, length + 1))
    
    return 0
