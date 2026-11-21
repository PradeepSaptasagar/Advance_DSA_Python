class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        odd_count = 0
        even_count = 1
        total_subarrays = 0
        current_sum = 0
        
        for num in arr:
            current_sum += num
            
            if current_sum % 2 != 0:  # If the current sum is odd
                total_subarrays += even_count
                odd_count += 1
            else:                     # If the current sum is even
                total_subarrays += odd_count 
                even_count += 1
                
        return total_subarrays % MOD

        