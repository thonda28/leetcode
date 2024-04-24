#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        curr = slow.next
        slow.next = None
        while curr:
            next = curr.next
            curr.next = prev
            prev, curr = curr, next

        front = head
        rear = prev
        while rear:
            f_next = front.next
            r_next = rear.next
            front.next = rear
            rear.next = f_next
            front = f_next
            rear = r_next
# @lc code=end
