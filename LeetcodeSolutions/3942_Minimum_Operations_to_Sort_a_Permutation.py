class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        
        # 1. Locate the position of the minimum element (0)
        k = nums.index(0)
        
        # 2. Check if the array is circularly increasing
        is_increasing = all(nums[(k + i) % n] == i for i in range(n))
        
        # 3. Check if the array is circularly decreasing
        is_decreasing = all(nums[(k - i + n) % n] == i for i in range(n))
        
        if not is_increasing and not is_decreasing:
            return -1
        
        ans = float('inf')
        
        if is_increasing:
            # Shift left k times
            ans = min(ans, k)
            # Reverse, shift (k + 1) times, reverse back
            # (or shift right: reverse -> shift -> reverse)
            if k > 0:
                ans = min(ans, (n - k) + 2)
            
        if is_decreasing:
            # Option 1: Reverse first, then shift left (n - 1 - k) times
            ans = min(ans, 1 + (n - 1 - k))
            # Option 2: Shift left (k + 1) times, then reverse
            ans = min(ans, (k + 1) + 1)
            
        return ans

# Time Complexity=O(N), Space Complexity=O(1)