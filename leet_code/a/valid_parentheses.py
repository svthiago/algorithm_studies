# Runtime: 28 ms, faster than 94.11% of Python3 online submissions for Valid Parentheses.
# Memory Usage: 14 MB, less than 71.98% of Python3 online submissions for Valid Parentheses.

"""
Test cases
"(])"
")(){}"
"([)"
"()"
"){"
"]"
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        cases = {'(': ')', '[': ']', '{': '}'}
        
        for c in s:
            if c in cases.keys():
                stack.append(c)
            elif stack and (c in cases[stack[-1]]):
                    stack.pop()
            else:
                return False

        return not stack
