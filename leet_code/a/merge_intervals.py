# TESTCASES
# [[1,3],[2,6],[8,10],[15,18]]
# [[2,3],[4,5],[6,7],[8,9],[1,10]]
# [[1,4],[0,2],[3,5]]
# [[1,4],[5,6]]
# [[1,4],[0,4]]


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        
        result = []
        result.append(intervals[0])
        
        for i in range(1, len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]
            
            if start <= result[-1][1]:
                res_start = result[-1][0]
                res_end = result[-1][1]
                
                result.pop()
                result.append([res_start, max(end, res_end)])
                
            else:
                result.append(intervals[i])

        return result
