class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        ans = -1
        for i in range(n):
            if nums[i] != i:
                if ans == -1:
                    ans = nums[i]
                else:
                    ans &= nums[i]
        return max(ans, 0)

# Time Complexity=O(N), Space Complexity=O(1)

class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        ans = None
        for i, x in enumerate(nums):
            if i != x:
                if ans is None:
                    ans = x
                else:
                    ans &= x            
        return ans if ans is not None else 0

# Time Complexity=O(N), Space Complexity=O(1)

class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        misplaced = [x for i, x in enumerate(nums) if i != x]
        if not misplaced:
             return 0
        return reduce(lambda a, b: a & b, misplaced)    

# Time Complexity=O(N), Space Complexity=O(N)
