class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {")": "(", "]": "[", "}": "{"}  # Closing -> expected opening bracket.
        stack = []
        for ch in s:
            if ch in "([{":
                stack.append(ch)  # Save opening brackets until their matching closer appears.
            else:
                if not stack or stack.pop() != pairs[ch]:
                    return False  # Missing or mismatched opening bracket.
        return not stack  # No unmatched opening brackets may remain.