# 2333. Minimum Sum of Squared Difference

class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        n = len(nums1)
        k = k1 + k2
        
        # Step 1: Calculate initial gaps
        gaps = []
        for i in range(n):
            gaps.append(abs(nums1[i] - nums2[i]))
            
        # Step 2: Check if we can zero everything out
        if sum(gaps) <= k:
            return 0
            
        # Step 3: Build the frequency dictionary
        m = {}
        for gap in gaps:
            if gap > 0:
                m[gap] = m.get(gap, 0) + 1
                
        # Step 4: Shave down the peaks
        max_gap = max(m.keys())
        for current_gap in range(max_gap, 0, -1):
            if current_gap not in m or m[current_gap] == 0:
                continue
                
            count = m[current_gap]
            reduce_amount = min(k, count)
            
            # Spend operations
            k -= reduce_amount
            
            # Move reduced gaps down by 1
            next_gap = current_gap - 1
            if next_gap > 0:
                m[next_gap] = m.get(next_gap, 0) + reduce_amount
                
            # Remove them from the current level
            m[current_gap] -= reduce_amount
            
            if k == 0:
                break
                
        # Step 5: Calculate the final sum of squares
        return sum((gap ** 2) * count for gap, count in m.items())

# Time Complexity=O(N+M), Space COmplexity=O(N)