class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        score = 0
        depth = 0
        for i in range(len(s)):
            if s[i] == '(':
                depth += 1
            else:
                depth -= 1
            # If we find an immediate pair (), add 2^depth
                if s[i-1] == '(':
                    score += (1 << depth)
                
        return score

# Time Complexity=O(N), Space Complexity=O(1)

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        def helper(i, j):
            score = 0
            balance = 0
            start = i
        
            for k in range(i, j):
                if s[k] == '(':
                    balance += 1
                else:
                    balance -= 1
                
            # When balance hits 0, we found a complete independent block
                if balance == 0:
                    if k - start == 1:
                        score += 1  # It's an immediate '()'
                    else:
                        score += 2 * helper(start + 1, k)  # It's wrapped like '(A)'
                    start = k + 1
            return score
        return helper(0, len(s))

# Time Complexity=O(N^2), Space Complexity=O(1)

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]  # Base container
        for char in s:
            if char == '(':
                stack.append(0)  # Start a new nested level
            else:
                inner_score = stack.pop()
            # If inner_score is 0 (meaning '()'), score is 1. Otherwise, double it.
                current_score = max(1, 2 * inner_score)
                stack[-1] += current_score  # Add to the outer level
        return stack[0]

# Time Complexity=O(N), Space Complexity=O(N)