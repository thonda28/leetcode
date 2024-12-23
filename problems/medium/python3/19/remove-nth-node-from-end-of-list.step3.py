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
        dummy_head = ListNode(next=head)
        fast = dummy_head
        slow = dummy_head
        for _ in range(n):
            if fast.next is None:
                raise RuntimeError(f"{n} is greater than the length of the ListNode.")
            fast = fast.next
        while fast.next is not None:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy_head.next
# @lc code=end
