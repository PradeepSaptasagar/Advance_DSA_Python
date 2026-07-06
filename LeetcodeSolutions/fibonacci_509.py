class Solution:
    def fib(self, n: int) -> int:
        def func(num):
            if num==0 or num==1:
                return num
            return func(num-1)+func(num-2)
        answer=func(n)
        return answer