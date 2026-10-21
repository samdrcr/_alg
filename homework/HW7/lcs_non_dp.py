import time

def is_subsequence(sub, text):
    i, j = 0, 0
    while i < len(sub) and j < len(text):
        if sub[i] == text[j]:
            i += 1
        j += 1
    return i == len(sub)

def lcs_brute_force(str_a, str_b):
    short_str, long_str = (str_a, str_b) if len(str_a) <= len(str_b) else (str_b, str_a)
    max_len = 0
    
    def backtrack(index, current_sub):
        nonlocal max_len
        if index == len(short_str):
            if is_subsequence(current_sub, long_str):
                max_len = max(max_len, len(current_sub))
            return
            
        backtrack(index + 1, current_sub + short_str[index])
        backtrack(index + 1, current_sub)
        
    backtrack(0, "")
    return max_len

if __name__ == "__main__":
    str_a = "ABCBDABQWERTYUIOP"
    str_b = "BDCABQWERTYUIOP"
    
    print(f"Comparing strings of length {len(str_a)} and {len(str_b)}")
    
    start_time = time.perf_counter()
    result = lcs_brute_force(str_a, str_b)
    end_time = time.perf_counter()
    
    print(f"LCS Length = {result}")
    print(f"Non-DP Execution Time: {end_time - start_time:.6f} seconds")