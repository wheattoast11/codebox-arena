def wildcard_match(s, p):
    """
    Returns True if pattern p matches the entire string s.
    Supports '?' (any single char) and '*' (any sequence of chars).
    """
    m, n = len(s), len(p)
    
    # dp[i][j] means p[:j] matches s[:i]
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    
    # Empty pattern matches empty string
    dp[0][0] = True
    
    # Handle patterns that start with '*' which can match empty string
    for j in range(1, n + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]
        else:
            break  # Once we hit a non-'*', no further '*' can make it match empty string
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                # '*' can either:
                # 1. Match zero characters: dp[i][j-1]
                # 2. Match one or more characters: dp[i-1][j] (consume one char from s, keep '*')
                dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
            elif p[j - 1] == '?' or p[j - 1] == s[i - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = False
    
    return dp[m][n]
