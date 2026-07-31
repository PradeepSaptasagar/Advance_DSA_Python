n=len(nums)
left=0
right=n-1
floor_val=-1
ceil_val=-1
while left<=right:
    mid=(left+right)//2
    if nums[mid]==target:
        return [nums[mid],nums[mid]]
    if nums[mid]>=target:
        ceil_val=nums[mid]
        right=mid-1
    if nums[mid]<=target:
        floor_val=nums[mid]
        left=mid+1
return [floor_val,ceil_val]