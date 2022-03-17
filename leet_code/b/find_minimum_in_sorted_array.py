# Runtime: 68 ms, faster than 32.01% of Python3 online submissions for Find Minimum in Rotated Sorted Array.
# Memory Usage: 14.2 MB, less than 42.61% of Python3 online submissions for Find Minimum in Rotated Sorted Array.


class Solution:
    def findMin(self, nums) -> int:
        
        prev = nums[0]
        min = nums[0]
        for n in range(1, len(nums)):
            if prev > nums[n]:
                return nums[n]
            else:
                prev = nums[n]
                if prev < min:
                    min = prev

        return min