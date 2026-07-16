max_sum = nums[0]
    current_sum = 0
    
    for num in nums:
        current_sum += num
        
        if current_sum > max_sum:
            max_sum = current_sum
            
        if current_sum <= 0:
            current_sum = 0
            
    return max_sum

def maxSubArray(nums: list[int]) -> int:
    def maxCrossingSum(nums: list[int], low: int, mid: int, high: int) -> int:
        left_max=float('-inf')
        current_sum=0
        for i in range(mid,low-1,-1):
            current_sum+=nums[i]
            if current_sum>left_max:
                left_max=current_sum

        right_max=float('-inf')
        current_sum=0
        for j in range(mid+1,high+1):
            current_sum+=nums[j]
            if current_sum>right_max:
                right_max=current_sum

        return left_max + right_max

    def maxSubArrayHelper(nums: list[int], low: int, high: int)->int:
        if low==high:
            return nums[low]

        mid=(low + high)//2

        left_sum=maxSubArrayHelper(nums, low, mid)
        right_sum=maxSubArrayHelper(nums, mid + 1, high)
        crossing_sum=maxCrossingSum(nums,low,mid,high)

        return max(left_sum, right_sum,crossing_sum)

    return maxSubArrayHelper(nums, 0, len(nums) - 1)