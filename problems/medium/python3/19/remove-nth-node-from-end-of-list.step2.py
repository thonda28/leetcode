#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_head = ListNode(0, head)
        first = dummy_head
        for _ in range(n):
            if first is None:
                raise RuntimeError(f"{n} is greater than the length of the ListNode.")
            first = first.next
        second = dummy_head
        while first and first.next:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy_head.next
# @lc code=end
