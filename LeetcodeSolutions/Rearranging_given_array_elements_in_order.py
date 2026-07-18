class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positives=[]
        negatives=[]
        result=[]
        for i in range(0,len(nums)):
            if nums[i]<0:
                negatives.append(nums[i])
            else:
                positives.append(nums[i])
        for i,pos_elem in enumerate(positives):
            result.append(pos_elem)    
            result.append(negatives[i])
        return result