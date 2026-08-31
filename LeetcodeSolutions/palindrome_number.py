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