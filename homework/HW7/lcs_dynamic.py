import time

def lcs_dp(str_a, str_b):
    m, n = len(str_a), len(str_b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str_a[i - 1] == str_b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                
    return dp[m][n]

if __name__ == "__main__":
    str_a = "ABCBDABQWERTYUIOP"
    str_b = "BDCABQWERTYUIOP"
    
    print(f"Comparing strings of length {len(str_a)} and {len(str_b)}")
    
    start_time = time.perf_counter()
    result = lcs_dp(str_a, str_b)
    end_time = time.perf_counter()
    
    print(f"LCS Length = {result}")
    print(f"DP Execution Time: {end_time - start_time:.6f} seconds")