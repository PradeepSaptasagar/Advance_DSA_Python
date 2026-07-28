class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n=len(nums)
        left=0
        right=n-1
        lb=n
        while left<=right:
            mid=(left+right)//2
            if nums[mid]>=target:
                lb=mid
                right=mid-1
            else:
                left=mid+1
        return lb