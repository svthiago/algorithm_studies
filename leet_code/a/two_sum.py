
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, n in enumerate(nums):
            f =  target - n
            if f in d.keys():
                return [i, d[f]]
            else:
                d[n] = i
