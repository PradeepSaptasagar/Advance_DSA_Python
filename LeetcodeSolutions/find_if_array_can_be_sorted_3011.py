class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        prev_max = float("-inf")
        curr_min = curr_max = nums[0]
        curr_bits = bin(nums[0]).count("1")
        for i in range(1, len(nums)):
            bits = bin(nums[i]).count("1")
            if bits == curr_bits:
                curr_min = min(curr_min, nums[i])
                curr_max = max(curr_max, nums[i])
            else:
                if prev_max > curr_min:
                    return False
                prev_max = curr_max
                curr_min = curr_max = nums[i]
                curr_bits = bits
        return prev_max <= curr_min
        
# Time complexity=O(N), Space complexity=O(1)

class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        def count_set_bits(num: int) -> int:
            count = 0
            while num > 0:
                num &= (num - 1)
                count += 1
            return count
        n = len(nums)
        for _ in range(n):
            swapped = False
            for i in range(n - 1):
                if nums[i] > nums[i + 1]:
                    if count_set_bits(nums[i]) == count_set_bits(nums[i + 1]):
                        nums[i], nums[i + 1] = nums[i + 1], nums[i]
                        swapped = True
                    else:
                        return False
            if not swapped:
                break
        return True

# Time complexity=O(N^2), Space complexity=O(1)

class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        def count_set_bits(num: int) -> int:
            count = 0
            while num > 0:
                count += num & 1
                num >>= 1
            return count
        n = len(nums)
        for _ in range(n):
            swapped = False
            for i in range(n - 1):
                if nums[i] > nums[i + 1]:
                    if count_set_bits(nums[i]) == count_set_bits(nums[i + 1]):
                        nums[i], nums[i + 1] = nums[i + 1], nums[i]
                        swapped = True
                    else:
                        return False
            if not swapped:
                break
        return True

# Time complexity=O(N^2), Space complexity=O(1)

class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        n = len(nums)
        for _ in range(n):
            for i in range(0, n - 1):
                if nums[i] > nums[i + 1]:
                    if bin(nums[i]).count("1") == bin(nums[i + 1]).count("1"):
                        nums[i], nums[i + 1] = nums[i + 1], nums[i]
                    else:
                        return False
        return True

# Time complexity=O(N^2), Space complexity=O(1)
