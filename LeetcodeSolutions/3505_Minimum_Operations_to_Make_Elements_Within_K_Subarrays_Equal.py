from typing import List
import heapq

class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)
        cost = [0] * (n - x + 1)
        
        low = []   # Max-heap: stores (-val, idx)
        high = []  # Min-heap: stores (val, idx)
        sum_low = 0
        sum_high = 0
        size_low = 0
        size_high = 0
        
        # Tracking for robust O(1) state updates
        in_low = [False] * n
        deleted = [False] * n
        
        def prune_low():
            while low and deleted[low[0][1]]:
                heapq.heappop(low)
                
        def prune_high():
            while high and deleted[high[0][1]]:
                heapq.heappop(high)
                
        def add(i):
            nonlocal sum_low, sum_high, size_low, size_high
            val = nums[i]
            prune_low()
            
            if not low or val <= -low[0][0]:
                heapq.heappush(low, (-val, i))
                sum_low += val
                size_low += 1
                in_low[i] = True
            else:
                heapq.heappush(high, (val, i))
                sum_high += val
                size_high += 1
                in_low[i] = False
                
        def remove(i):
            nonlocal sum_low, sum_high, size_low, size_high
            deleted[i] = True
            
            if in_low[i]:
                sum_low -= nums[i]
                size_low -= 1
            else:
                sum_high -= nums[i]
                size_high -= 1
                
        def balance():
            nonlocal sum_low, sum_high, size_low, size_high
            # FIX: Dynamically target the median of *active* elements, not static `x`
            target_low = (size_low + size_high + 1) // 2
            
            while size_low < target_low:
                prune_high()
                val, i = heapq.heappop(high)
                sum_high -= val
                size_high -= 1
                
                heapq.heappush(low, (-val, i))
                sum_low += val
                size_low += 1
                in_low[i] = True
                
            while size_low > target_low:
                prune_low()
                neg_val, i = heapq.heappop(low)
                val = -neg_val
                sum_low -= val
                size_low -= 1
                
                heapq.heappush(high, (val, i))
                sum_high += val
                size_high += 1
                in_low[i] = False

        # Phase 1: Build the sliding window costs
        for i in range(n):
            add(i)
            if i >= x:
                remove(i - x)
            balance()
            
            if i >= x - 1:
                prune_low()
                median = -low[0][0]
                
                if x % 2 == 0:
                    cost[i - x + 1] = sum_high - sum_low
                else:
                    cost[i - x + 1] = sum_high - sum_low + median

        # Phase 2: Dynamic Programming
        INF = float('inf')
        dp = [[INF] * (k + 1) for _ in range(n + 1)]
        
        for i in range(n + 1):
            dp[i][0] = 0
            
        for i in range(1, n + 1):
            for j in range(1, k + 1):
                ans = dp[i-1][j]
                if i >= x:
                    ans = min(ans, dp[i-x][j-1] + cost[i-x])
                dp[i][j] = ans
                
        return dp[n][k]