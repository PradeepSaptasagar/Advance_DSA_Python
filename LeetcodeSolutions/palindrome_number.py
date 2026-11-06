class Solution:
    def isPalindrome(self, x: int) -> bool:
        a=str(x)
        n=len(a)
        left=0
        right=n-1
        while left<right:
            if a[left]!=a[right]:
                return False
            left+=1
            right-=1
        return True

# Time complexity=O(N), Space complexity=O(N)

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False  # Negative values and nonzero trailing-zero values cannot be palindromes.
        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10  # Append the last digit.
            x //= 10  # Remove the last digit from the original half.
        # For odd digit counts, discard the middle digit from reversed_half.
        return x == reversed_half or x == reversed_half // 10