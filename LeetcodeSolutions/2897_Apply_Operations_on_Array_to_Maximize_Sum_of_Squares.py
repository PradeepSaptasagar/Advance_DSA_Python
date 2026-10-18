class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        count1 = [0] * 32
        
        # Phase 1: The Collection Phase
        # Bank every 1-bit from all numbers across their 32 positions
        for num in nums:
            for j in range(32):
                if (num >> j) & 1:
                    count1[j] += 1
                    
        ans = 0
        
        # Phase 2: The Building Phase
        # Construct the k largest possible numbers and sum their squares
        for _ in range(k):
            val = 0
            for j in range(32):
                if count1[j] > 0:
                    val |= (1 << j)  # Slot the 1-bit into the j-th position
                    count1[j] -= 1   # Deduct from the bank
                    
            ans = (ans + val * val) % MOD
            
        return ans
    