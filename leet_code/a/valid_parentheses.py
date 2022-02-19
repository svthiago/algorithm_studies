"""
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
