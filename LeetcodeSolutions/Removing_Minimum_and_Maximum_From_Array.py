class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n=len(nums)
        min_idx=nums.index(min(nums))
        max_idx=nums.index(max(nums))
        low=min(min_idx, max_idx)
        high=max(min_idx, max_idx)
        front_cost=high + 1
        back_cost=n - low
        both_cost=(low+1)+(n-high)
        if front_cost<=back_cost and front_cost<=both_cost:
            return front_cost
        elif back_cost<=both_cost:
            return back_cost
        else:
            return both_cost
        