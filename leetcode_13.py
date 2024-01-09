# 23. Merge k Sorted Lists
# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
# Merge all the linked-lists into one sorted linked-list and return it.


# https://leetcode.com/problems/merge-k-sorted-lists/description/


# Definition for singly-linked list. sorted in ascending order
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # if not lists:
        #     return None
        # if not lists[0]:
        #     return ListNode(None)
        arr_of_arr = []
        for node in lists:
            node_numbers = []
            while node:
                node_numbers.append(node.val)
                node = node.next
            arr_of_arr.append(node_numbers)
        numbers = [n for arr in arr_of_arr for n in arr]
        if len(numbers) == 0:
            return None
        numbers.sort()
        node = ListNode(numbers[0])
        current = node
        for n in numbers[1:]:
            current.next = ListNode(n)
            current = current.next
        return node


# not using linked list
# def mergeKLists(self, lists):
#     """
#     :type lists: List[ListNode]
#     :rtype: ListNode
#     """


node_1 = ListNode(1, ListNode(4, ListNode(5)))
node_2 = ListNode(1, ListNode(3, ListNode(4)))
node_3 = ListNode(2, ListNode(6))
# arr_of_nodes = [node_1, node_2, node_3]
arr_of_nodes = []


if len(arr_of_nodes) == 0:
    print('[]')
arr_of_arr = []
for node in arr_of_nodes:
    node_numbers = []
    while node:
        node_numbers.append(node.val)
        node = node.next
    arr_of_arr.append(node_numbers)

arr_list = [n for arr in arr_of_arr for n in arr]
arr_list.sort()
node = ListNode(arr_list[0])
current = node
for n in arr_list[1:]:
    current.next = ListNode(n)
    current = current.next



# list = [n for arr in lists for n in arr]
# list.sort()
