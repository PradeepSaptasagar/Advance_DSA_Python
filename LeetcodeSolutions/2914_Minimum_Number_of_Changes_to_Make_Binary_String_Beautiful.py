class Solution:
    def minChanges(self, s: str) -> int:
        counter = 0
        
        # Start at 0, go to the end of the string, taking steps of 2
        for i in range(0, len(s), 2):
            # If the character and the one immediately next to it don't match
            if s[i] != s[i+1]:
                counter += 1  # We need 1 change to make this pair beautiful
                
        return counter