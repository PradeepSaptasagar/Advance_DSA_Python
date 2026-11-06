class Solution:
    def maxArea(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        best = 0
        while left < right:
            width = right - left
            best = max(best, width * min(height[left], height[right]))  # Area is limited by the shorter wall.
            if height[left] < height[right]:
                left += 1   # The shorter wall limits area, so try a taller left wall.
            else:
                right -= 1  # Try a taller right wall.
        return best