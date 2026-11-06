class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)
        
        # 1. Skip leading whitespaces
        while i < n and s[i] == " ":
            i += 1
            
        # 2. Handle the sign
        sign = 1
        if i < n and (s[i] == "-" or s[i] == "+"):
            if s[i] == "-":
                sign = -1
            i += 1  # Move past the sign
            
        # 3. The Math Loop (automatically handles leading zeros!)
        result = 0
        while i < n and s[i].isdigit():
            result = (result * 10) + int(s[i])
            i += 1
            
        # 4. Apply the sign
        result = result * sign
        
        # 5. The 32-bit Boundary Clamp
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        
        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX
            
        return result

# Time complexity=O(N), Space complesity=O(1)

class Solution:
    def myAtoi(self, s: str) -> int:
        i, n = 0, len(s)
        while i < n and s[i] == " ":  # Ignore leading spaces only.
            i += 1
        sign = 1
        if i < n and s[i] in "+-":  # Read an optional sign.
            sign = -1 if s[i] == "-" else 1
            i += 1
        number = 0
        while i < n and s[i].isdigit():  # Stop at the first non-digit.
            number = number * 10 + int(s[i])
            i += 1
        number *= sign
        # Clamp to the signed 32-bit range.
        return max(-(2**31), min(2**31 - 1, number))