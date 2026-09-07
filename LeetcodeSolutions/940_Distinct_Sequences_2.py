class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        ends_with = [0] * 26
        
        for char in s:
            idx = ord(char) - ord('a')
            
            # Count all subsequences currently in existence
            current_total = sum(ends_with)
            
            # Overwrite this letter's slot to erase old duplicates
            ends_with[idx] = (current_total + 1) % MOD
            
        # The final answer is the sum of all valid sequences ending in any letter
        return sum(ends_with) % MOD