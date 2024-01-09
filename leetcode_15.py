# 24. Swap Nodes in Pairs
# Given a linked list, swap every two adjacent nodes and return its head.
# You must solve the problem without modifying the values
# in the list's nodes (i.e., only nodes themselves may be changed.)


# https://leetcode.com/problems/swap-nodes-in-pairs/description/


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        counter = 1
        current_node = head
        while current_node:
            if counter % 2 == 0:
                previous_node.val, current_node.val = current_node.val, previous_node.val
            previous_node, current_node = current_node, current_node.next
            counter += 1
        return head


# head = [1, 2, 3, 4]
# node = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
# node = None


# counter = 1
# current_node = node
# while current_node:
#     if counter % 2 == 0:
#         previous_node.val, current_node.val = current_node.val, previous_node.val
#     previous_node, current_node = current_node, current_node.next
#     counter += 1











