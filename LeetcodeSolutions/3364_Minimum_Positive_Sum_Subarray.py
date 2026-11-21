class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        min_sum = float('inf')
        
        for start in range(len(nums)):
            current_sum = 0
            
            # Start expanding the end pointer directly
            for end in range(start, min(start + r, len(nums))):
                current_sum += nums[end]
                
                # Calculate the length of our current window
                length = end - start + 1
                
                # Only check the conditions if the length is within our target bounds
                if l <= length <= r:
                    if current_sum > 0 and current_sum < min_sum:
                        min_sum = current_sum
                        
        if min_sum != float('inf'):
            return min_sum
        else:
            return -1
            
        