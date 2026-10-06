class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_tokens = 0
        additions_needed = 0
        
        for char in s:
            if char == "(":
                open_tokens += 1
            elif char == ")":
                if open_tokens > 0:
                    open_tokens -= 1
                else:
                    additions_needed += 1
                    
        return additions_needed + open_tokens

# Time Complexity=O(N), Space Complexity=O(1)

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        
        for char in s:
            if char == ")" and stack and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(char)
                
        return len(stack)

# Time Complexity=O(N), Space Complexity=O(N)

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        while "()" in s:
            s = s.replace("()", "")
            
        return len(s)

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_count = 0
        invalid_close = 0
        for char in s:
            if char == "(":
                open_count += 1
            elif char == ")":
                if open_count > 0:
                    open_count -= 1
                else:
                    invalid_close += 1
        close_count = 0
        invalid_open = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ")":
                close_count += 1
            elif s[i] == "(":
                if close_count > 0:
                    close_count -= 1
                else:
                    invalid_open += 1
                    
        return invalid_close + invalid_open

# Time Complxity=O(N), Space Complexity=O(1)