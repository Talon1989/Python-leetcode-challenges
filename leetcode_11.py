# 20. Valid Parentheses
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.


# https://leetcode.com/problems/valid-parentheses/


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 == 1:
            return False
        stack = []
        for t in s:
            if t == '(':
                stack.append(')')
            elif t == '[':
                stack.append(']')
            elif t == '{':
                stack.append('}')
            else:
                if len(stack) == 0:
                    return False
                elif t == ')' and stack[-1] == ')':
                    stack.pop()
                elif t == ']' and stack[-1] == ']':
                    stack.pop()
                elif t == '}' and stack[-1] == '}':
                    stack.pop()
                else:
                    return False
        if len(stack) > 0:
            return False
        return True


# s = "()[]{}"
s = "()[]{}{{{[([[]])]}}}"


n_round, n_square, n_curly = 0, 0, 0
dominant = ''


# for t in s:
#     if t == '(':
#         n_round += 1
#     elif t == ')':
#         n_round -= 1
#     elif t == '[':
#         n_square += 1
#     elif t == ']':
#         n_square -= 1
#     elif t == '{':
#         n_curly += 1
#     elif t == '}':
#         n_curly -= 1


# if len(s) % 2 == 1:
#     print('False')
# stack = []
# for t in s:
#     if t == '(':
#         stack.append(')')
#     elif t == '[':
#         stack.append(']')
#     elif t == '{':
#         stack.append('}')
#     else:
#         if len(stack) == 0:
#             print(False)
#         elif t == ')' and stack[-1] == ')':
#             stack.pop()
#         elif t == ']' and stack[-1] == ']':
#             stack.pop()
#         elif t == '}' and stack[-1] == '}':
#             stack.pop()
#         else:
#             print(False)
# print(True)




