class Solution:
    def checkValidString(self, s: str) -> bool:
        
        min_open = 0
        max_open = 0
    
        for char in s:
            if char == '(':
                min_open += 1
                max_open += 1
            elif char == ')':
                min_open -= 1
                max_open -= 1
            else: # char == '*'
                min_open -= 1
                max_open += 1
            
        # If max_open drops below 0, we have too many ')' -> immediate fail
            if max_open < 0:
                return False
            
        # min_open can never be negative (can't have negative open brackets)
            if min_open < 0:
                min_open = 0
            
    # At the end, if min_open is 0, everything is balanced!
        return min_open == 0

# Time COmplexity=O(N), Space Complexity=O(1)