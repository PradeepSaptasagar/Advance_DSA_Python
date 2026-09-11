class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        n = len(digits)
        unique_numbers = set()
        for i in range(n):
            if digits[i] == 0:
                continue
            for j in range(n):
                if i == j:
                    continue
                for k in range(n):
                    if k == i or k == j:
                        continue
                    if digits[k] % 2 != 0:
                        continue
                    num = (digits[i] * 100) + (digits[j] * 10) + digits[k]
                    unique_numbers.add(num)
        return len(sorted(list(unique_numbers)))

# Time complexity=O(N^3), Space complexity=O(450)

class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        inventory = [0] * 10
        for d in digits:
            inventory[d] += 1
        count = 0
        for num in range(100, 1000, 2):
            temp = num 
            ones = temp % 10
            temp = temp // 10
            tens = temp % 10
            temp = temp // 10
            hundreds = temp % 10
            inventory[ones] -= 1
            inventory[tens] -= 1
            inventory[hundreds] -= 1
            if inventory[ones] >= 0 and inventory[tens] >= 0 and inventory[hundreds] >= 0:
                count += 1
            inventory[ones] += 1
            inventory[tens] += 1
            inventory[hundreds] += 1
        return count

# Time complexity=O(N), Space complexity=O(1)
