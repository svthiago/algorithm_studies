# Runtime: 97 ms, faster than 24.80% of Python3 online submissions for Linked List Cycle.
# Memory Usage: 18 MB, less than 11.60% of Python3 online submissions for Linked List Cycle.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None  

class Solution:
    def hasCycle(self, head):
        if head is None:
            return False

        d = {id(head): head}
        
        itr = head.next
        while itr:
            if id(itr) in d.keys():
                return True
            else:
                d[id(itr)] = itr.val
                itr = itr.next
        
        return False