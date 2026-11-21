from functools import cache

class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        
        # 1. Precomputation: Build the cost matrix
        cost = [[float('inf')] * n for _ in range(n)]
        
        for i in range(n):
            for j in range(i + 1, n):
                L = j - i + 1
                min_changes = float('inf')
                
                # Find all proper divisors of L
                for d in range(1, L // 2 + 1):
                    if L % d == 0:
                        current_changes = 0
                        
                        # Count mismatches for this divisor
                        for start_offset in range(d):
                            left = i + start_offset
                            right = j - (L % d) + start_offset # Rightmost index in this group
                            
                            # Clean two-pointer calculation 
                            # (Adjusting the exact 'right' pointer to avoid generating a list)
                            curr_left = left
                            curr_right = j
                            
                            # A slightly faster way to do the two pointers without creating the intermediate list:
                            group_left = i + start_offset
                            group_right = j - (L - 1) % d + start_offset
                            if group_right > j: 
                                group_right -= d
                                
                            while group_left < group_right:
                                if s[group_left] != s[group_right]:
                                    current_changes += 1
                                group_left += d
                                group_right -= d
                                
                        min_changes = min(min_changes, current_changes)
                        
                cost[i][j] = min_changes

        # 2. DP Phase: Partitioning
        @cache
        def dp(i, p):
            # Base Case: Not enough characters left
            if n - i < 2 * p:
                return float('inf')
            
            # Base Case: Last partition takes the rest of the string
            if p == 1:
                return cost[i][n - 1]
            
            min_total = float('inf')
            
            # Try all valid cuts for the current partition
            for j in range(i + 1, n - 2 * (p - 1)):
                min_total = min(min_total, cost[i][j] + dp(j + 1, p - 1))
                
            return min_total

        return dp(0, k)
        
        