class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k=k%n
        if k==0:
            return nums
        count=0
        start_index=0
        while count<n:
            current=start_index
            prev_value=nums[start_index]
            while True:
                next_index=(current+k)%n
                temp=nums[next_index]
                nums[next_index]=prev_value
                prev_value=temp
                count+=1
                current=next_index
                if current==start_index:
                    break
            start_index+=1