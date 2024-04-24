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
        middle_node = self.get_middle_node(head)
        front_head = head
        back_head = middle_node.next
        middle_node.next = None
        reversed_back_head = self.reverse(back_head)
        self.interleave(front_head, reversed_back_head)

    def get_middle_node(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        When the number of nodes is even, return the last node of the front part
        """
        if not head:
            return head
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

    def interleave(self, head1: Optional[ListNode], head2: Optional[ListNode]) -> None:
        while head1 and head2:
            next1 = head1.next
            next2 = head2.next
            head1.next = head2
            head2.next = next1
            head1 = next1
            head2 = next2
# @lc code=end
