class Solution:
    def minOperations(self, s: str) -> int:
        # Case 0: Linear scan to check if already sorted
        is_sorted = True
        for i in range(len(s) - 1):
            if s[i] > s[i + 1]:
                is_sorted = False
                break
        if is_sorted:
            return 0
            
        # Impossible case
        if len(s) == 2:
            return -1
            
        min_char = min(s)
        max_char = max(s)
        
        # Case 1: Smallest is already at the front OR largest is at the back
        if s[0] == min_char or s[-1] == max_char:
            return 1
            
        # Case 3: Strictly trapped ONLY if the single max is at index 0 
        # AND the single min is at index -1
        if s[0] == max_char and s[-1] == min_char:
            # Check if there are duplicate mins/maxes we can use to escape
            if min_char not in s[:-1] and max_char not in s[1:]:
                return 3
            
        # Case 2: Everything else can be solved in 2 operations
        return 2
    