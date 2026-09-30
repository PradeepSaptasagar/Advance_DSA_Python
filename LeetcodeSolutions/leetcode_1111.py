## 1. Depth Counter Parity Method

class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        res = []
        depth = 0
        for char in seq:
            if char == '(':
                res.append(depth % 2)
                depth += 1
            else:
                depth -= 1
                res.append(depth % 2)
        return res


# Time Complexity: O(n), Space Complexity: O(1)

------------------------------
## 2. Cut-in-Half Target Method (Two-Pass)

class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        max_depth = 0
        current_depth = 0
        for char in seq:
            if char == '(':
                current_depth += 1
                max_depth = max(max_depth, current_depth)
            else:
                current_depth -= 1
        target = max_depth // 2
        res = []
        current_depth = 0
        for char in seq:
            if char == '(':
                current_depth += 1
                res.append(0 if current_depth <= target else 1)
            else:
                res.append(0 if current_depth <= target else 1)
                current_depth -= 1
        return res


# Time Complexity: O(n), Space Complexity: O(1)

------------------------------
## 3. String Index Bitwise Method (One-Liner)

class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        return [i & 1 if c == '(' else 1 - (i & 1) for i, c in enumerate(seq)]


# Time Complexity: O(n), Space Complexity: O(1)

------------------------------
## 4. Explicit Stack Method

class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        res = []
        stack = []
        for char in seq:
            if char == '(':
                res.append(len(stack) % 2)
                stack.append('(')
            else:
                stack.pop()
                res.append(len(stack) % 2)
        return res


# Time Complexity: O(n), Space Complexity: O(n)

