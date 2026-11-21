class Solution:
    def digitSum(self, s: str, k: int) -> str:
        # Loop continues as long as the string length is greater than k
        while len(s) > k:
            new_s = ""
            
            # Step through the string in chunks of size k
            for i in range(0, len(s), k):
                # Slice the group (handles the remainder naturally if len(s) % k != 0)
                chunk = s[i:i+k]
                
                # Sum the integer values of the characters in the chunk
                chunk_sum = sum(int(digit) for digit in chunk)
                
                # Append the string representation of the sum to the new string
                new_s += str(chunk_sum)
                
            # Replace the old string with the newly formed one for the next round
            s = new_s
            
        return s
        
        