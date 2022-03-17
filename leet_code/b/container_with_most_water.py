# Runtime: 680 ms, faster than 97.95% of Python3 online submissions for Container With Most Water.
# Memory Usage: 27.6 MB, less than 26.78% of Python3 online submissions for Container With Most Water.


class Solution:
    def maxArea(self, height) -> int: 
        i = 0
        j = len(height) - 1
        area = -1

        while i < j:
            if height[i] < height[j]:
                new_area = height[i] * (j - i)
                if new_area > area:
                    area = new_area

            else:
                new_area = height[j] * (j - i)
                if new_area > area:
                    area = new_area

            if height[i] > height[j]:
                j-=1
            else :
                i+=1

        return area
