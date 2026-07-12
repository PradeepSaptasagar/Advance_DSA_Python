class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        insert_pos = 0
        n = len(nums)
        for i in range(0, n):
            if nums[i] != 0: 
               nums[insert_pos], nums[i] = nums[i], nums[insert_pos]
               insert_pos += 1
        