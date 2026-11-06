class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        n = len(arr1)
        m = len(arr2)
        counter = 0
        for i in range(n):
            is_safe = True           # Assume safe at the start of each arr1 number
            for j in range(m):
                total = abs(arr1[i] - arr2[j])
                if total <= d:
                    is_safe = False # Trap triggered!
                    break           # Stop checking this arr1 number
             
    # Inner loop is done. Did it survive?
            if is_safe:
                counter += 1
        return counter
    