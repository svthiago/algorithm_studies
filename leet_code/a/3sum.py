from itertools import combinations


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        n = len(nums)
        cases = []
        for i in range(n):

            if (i > 0) and (nums[i] == nums[i-1]):
                continue
            
            k = n-1
            j = i+1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s < 0:
                    j += 1

                elif s > 0:
                    k -= 1

                else:
                    cases.append([nums[i], nums[j], nums[k]])
                    
                    j += 1
                    while((j < k) and (nums[j] == nums[j-1])):
                        j += 1
                    
        return cases
