def n_queens_count(n):
    if n <= 0:
        raise ValueError("n must be positive")
    
    count = 0
    cols = set()
    diag1 = set()  # row - col
    diag2 = set()  # row + col
    
    def backtrack(row):
        nonlocal count
        if row == n:
            count += 1
            return
        
        for col in range(n):
            d1 = row - col
            d2 = row + col
            if col in cols or d1 in diag1 or d2 in diag2:
                continue
            cols.add(col)
            diag1.add(d1)
            diag2.add(d2)
            backtrack(row + 1)
            cols.remove(col)
            diag1.remove(d1)
            diag2.remove(d2)
    
    backtrack(0)
    return count
