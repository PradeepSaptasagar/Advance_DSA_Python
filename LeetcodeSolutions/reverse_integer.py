class Solution:
    def reverse(self, x: int) -> int:
        n=x<0
        if n: x=-x
        r=0
        while x>0:
            r=(r*10)+(x%10)
            x//=10
        if n: r=-r
        if r<-2**31 or r>2**31-1: return 0
        return r

# Time complexity=O(log N), Space complexity=O(1)

class Solution:
    def reverse(self, x: int) -> int:
        is_negative = False
        if x < 0:
            is_negative = True
            x = x * -1
        result = 0
        while x > 0:
            i = x % 10
            result = (result * 10) + i
            x = x // 10
        if is_negative:
            result = result * -1
        if result < -2**31 or result > (2**31 - 1):
            return 0
            
        return result
        
# Time complexity=O(log N), Space complexity=O(1)        
        