class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        first_occurrence=-1
        last_occurrence=-1
        low=0
        high=n-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                first_occurrence=mid
                high=mid-1
            elif nums[mid]>target:
                high=mid-1
            else:
                low=mid+1
        low=0
        high=n-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                last_occurrence=mid
                low=mid+1
            elif nums[mid]>target:
                high=mid-1
            else:
                low=mid+1
        return [first_occurrence,last_occurrence]