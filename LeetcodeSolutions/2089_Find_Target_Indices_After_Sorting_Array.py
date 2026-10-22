class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        # 1. Sort the array
        nums.sort()
        
        # 2. Find and return indices where the element matches the target
        return [i for i, num in enumerate(nums) if num == target]

class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        less_than_count = 0
        target_count = 0
        
        # Count elements less than and equal to the target
        for num in nums:
            if num < target:
                less_than_count += 1
            elif num == target:
                target_count += 1
        return [less_than_count + i for i in range(target_count)]
    