from collections import deque

class Solution:
    def countNonDecreasingSubarrays(self, nums: list[int], k: int) -> int:
        n = len(nums)
        ans = 0
        cost = 0
        j = n - 1
        
        # Using collections.deque for O(1) popleft()
        dq = deque() 
        
        # Traverse right-to-left
        for i in range(n - 1, -1, -1):
            
            # Phase 1: Bulldozer (Expand left)
            while dq and nums[i] > nums[dq[-1]]:
                popped_idx = dq.pop()
                
                if not dq:
                    width = j - popped_idx + 1
                else:
                    width = dq[-1] - popped_idx
                    
                cost += (nums[i] - nums[popped_idx]) * width
                
            dq.append(i)
            
            # Phase 2: Budget Check (Shrink right)
            while cost > k:
                cost -= (nums[dq[0]] - nums[j])
                
                if dq[0] == j:
                    dq.popleft()
                    
                j -= 1
                
            # Phase 3: Count Valid Subarrays
            ans += (j - i + 1)
            
        return ans
        
        