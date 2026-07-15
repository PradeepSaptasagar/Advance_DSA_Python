class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            partner=target-nums[i]
            if partner in nums[i+1:]:
                partner_index=nums.index(partner,i+1)
                return [i,partner_index]