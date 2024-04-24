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
        center = self.get_center_pointer(head)
        front = head
        rear = center.next
        center.next = None
        reversed_rear = self.reverse(rear)
        self.connect_altenately(front, reversed_rear)

    def get_center_pointer(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            next = curr.next
            curr.next = prev
            prev, curr = curr, next
        return prev

    def connect_altenately(self, head1: Optional[ListNode], head2: Optional[ListNode]) -> None:
        while head1 and head2:
            next1 = head1.next
            next2 = head2.next
            head1.next = head2
            head2.next = next1
            head1 = next1
            head2 = next2
# @lc code=end
