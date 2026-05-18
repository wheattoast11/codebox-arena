def edit_distance(s1, s2):
    m = len(s1)
    n = len(s2)
    
    # Create a DP table with (m+1) rows and (n+1) columns
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Base cases: converting empty string to/from s2/s1
    for i in range(m + 1):
        dp[i][0] = i  # deletions
    for j in range(n + 1):
        dp[0][j] = j  # insertions
    
    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  # No operation needed
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],      # Deletion
                    dp[i][j - 1],      # Insertion
                    dp[i - 1][j - 1]   # Substitution
                )
    
    return dp[m][n]

def damerau_distance(s1, s2):
    m = len(s1)
    n = len(s2)
    
    # Create a DP table with (m+1) rows and (n+1) columns
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Base cases: converting empty string to/from s2/s1
    for i in range(m + 1):
        dp[i][0] = i  # deletions
    for j in range(n + 1):
        dp[0][j] = j  # insertions
    
    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  # No operation needed
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],      # Deletion
                    dp[i][j - 1],      # Insertion
                    dp[i - 1][j - 1]   # Substitution
                )
            
            # Check for transposition (Damerau-Levenshtein optimal string alignment)
            if i >= 2 and j >= 2 and s1[i - 1] == s2[j - 2] and s1[i - 2] == s2[j - 1]:
                dp[i][j] = min(dp[i][j], dp[i - 2][j - 2] + 1)
    
    return dp[m][n]
