class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return 0
        nums.sort()
        n=len(nums)
        a=nums[n-1]-nums[2]
        b=nums[n-3]-nums[0]
        c=nums[n-2]-nums[1]
        return min(a, b, c)

class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return 0

        inf = float('inf')
        min1 = min2 = min3 = inf
        max1 = max2 = max3 = -inf

        for x in nums:
        # Update the 3 smallest values
            if x <= min1:
                min3 = min2
                min2 = min1
                min1 = x
            elif x <= min2:
                min3 = min2
                min2 = x
            elif x < min3:
                min3 = x

        # Update the 3 largest values
            if x >= max1:
                max3 = max2
                max2 = max1
                max1 = x
            elif x >= max2:
                max3 = max2
                max2 = x
            elif x > max3:
                max3 = x

        drop_two_smallest = max1 - min3
        drop_two_largest = max3 - min1
        drop_one_each = max2 - min2

        return min(drop_two_smallest, drop_two_largest, drop_one_each)
    