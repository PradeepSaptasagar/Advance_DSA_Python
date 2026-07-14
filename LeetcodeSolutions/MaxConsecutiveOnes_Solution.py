class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        largest=0
        count=0
        n=len(nums)
        for i in range(0,n):
            if nums[i]==1:
                count+=1
            else:
                if count>largest:
                    largest=count
                count=0
        return max(count,largest)
        