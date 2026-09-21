class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        result = [0] * k
        for start in range(n):
            for end in range(start + 1, n + 1):
                subarray = nums[start:end]
                product = 1
                for num in subarray:
                    product = (product * num) % k
                result[product] += 1
        return result

# Time Complexity=O(N^3), Space Complexity=O(N)

class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        result = [0] * k
        for start in range(n):
            running_product = 1
            for end in range(start, n):
                running_product = (running_product * nums[end]) % k
                result[running_product] += 1
        return result

# Time Complexity=O(N^2), Space Complexity=O(1)

class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        result = [0] * k
        dp = [0] * k
        for num in nums:
            current_dp = [0] * k
            rem = num % k
            current_dp[rem] += 1
            for old_rem in range(k):
                if dp[old_rem] > 0:
                    new_rem = (old_rem * num) % k
                    current_dp[new_rem] += dp[old_rem]
            for r in range(k):
                result[r] += current_dp[r]
            dp = current_dp
        return result

# Time Complexity=O(N*k), Space Complexity=O(k)