
# Improve that later

# Runtime: 3408 ms, faster than 5.01% of Python3 online submissions for Maximum Subarray.
# Memory Usage: 347.3 MB, less than 8.36% of Python3 online submissions for Maximum Subarray.


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        @cache
        def solve(i, must_pick):
            if i >= len(nums):
                return 0 if must_pick else -inf
            return max(nums[i] + solve(i+1, True), 0 if must_pick else solve(i+1, False))
        return solve(0, False)
