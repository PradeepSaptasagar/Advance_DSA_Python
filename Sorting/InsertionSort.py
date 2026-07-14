nums=[] # contains n number of elements
n=len(nums)
for i in range(0,n):
    key=nums[i]
    while j>=0 and nums[j]>key:
        nums[j+1]=nums[j]
        j-=1
    nums[j+1]=key