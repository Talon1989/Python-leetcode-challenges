# Add Two Numbers
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in
# reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        current_node = l1
        number_1 = ''
        while current_node:
            number_1 += str(current_node.val)
            current_node = current_node.next
        if number_1 == '':
            number_1 = 0
        else:
            number_1 = int(number_1[::-1])
        current_node = l2
        number_2 = ''
        while current_node:
            number_2 += str(current_node.val)
            current_node = current_node.next
        if number_2 == '':
            number_2 = 0
        else:
            number_2 = int(number_2[::-1])
        result = list(str(number_1 + number_2))
        prev_node = None
        for r in result[::-1]:
            node = ListNode(int(r), prev_node)
            prev_node = node
        return node


l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))


# current_node = l1
# number_1 = ''
# while current_node:
#     number_1 += str(current_node.val)
#     current_node = current_node.next
# if number_1 == '':
#     number_1 = 0
# else:
#     number_1 = int(number_1[::-1])
# current_node = l2
# number_2 = ''
# while current_node:
#     number_2 += str(current_node.val)
#     current_node = current_node.next
# if number_2 == '':
#     number_2 = 0
# else:
#     number_2 = int(number_2[::-1])
# result = list(str(number_1 + number_2))
# prev_node = None
# for r in result:
#     node = ListNode(int(r), prev_node)
#     prev_node = node


def get_value_recursively(current_node: ListNode, value=''):
    if current_node.next is None:
        return current_node.val
    value += str(get_value_recursively(current_node.next, value))
    return value + str(current_node.val)


