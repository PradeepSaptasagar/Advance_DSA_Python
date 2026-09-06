# 1. The Optimized Precomputation: This trades O(N) space to build a suffix array, allowing for instant lookups and achieving optimal linear time
# Time Complexity: O(N), Space Complexity: O(N)

class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        if n == 0: return -1
        
        right_mins = [0] * n
        right_mins[n-1] = nums[n-1]
        current_min = nums[n-1]
        
        for i in range(n-2, -1, -1):
            current_min = min(current_min, nums[i])
            right_mins[i] = current_min
            
        current_max = nums[0]
        for i in range(n):
            current_max = max(current_max, nums[i])
            if current_max - right_mins[i] <= k:
                return i
        return -1
        
# 2. The Brute Force (The Baseline): This is the foundational logic. It strictly follows the rules without any extra memory optimizations, calculating the maximum and minimum from scratch at every single step.
# Time Complexity: O(N^2), Space Complexity: O(N)

class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        for i in range(n):
            # Python slicing creates temporary arrays, scanning them takes O(N)
            current_max = max(nums[:i+1])
            current_min = min(nums[i:])
            
            if current_max - current_min <= k:
                return i
        return -1

# 3. Segment Tree (The Heavy-Duty Data Structure): This approach builds a tree mapping out all the minimums. It is overkill for a static array, but highly useful if the problem allowed the array elements to be updated dynamically mid-loop.
# Time Complexity: O(N log N), Space Complexity: O(N)

class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        tree = [0] * (2 * n)
        
        # Build the segment tree for range minimum queries
        for i in range(n):
            tree[n + i] = nums[i]
        for i in range(n - 1, 0, -1):
            tree[i] = min(tree[2 * i], tree[2 * i + 1])
            
        def query_min(left, right):
            left += n
            right += n + 1
            res = float('inf')
            while left < right:
                if left % 2 == 1:
                    res = min(res, tree[left])
                    left += 1
                if right % 2 == 1:
                    right -= 1
                    res = min(res, tree[right])
                left //= 2
                right //= 2
            return res

        current_max = nums[0]
        for i in range(n):
            current_max = max(current_max, nums[i])
            if current_max - query_min(i, n - 1) <= k:
                return i
        return -1