# 22. Generate Parentheses
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.


# https://leetcode.com/problems/generate-parentheses/description/


class Solution(object):

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []

        def recursive_gen(p, left, right):
            if left:
                recursive_gen(p + '(', left - 1, right)
            if right > left:
                recursive_gen(p + ')', left, right - 1)
            if right == 0:  # regardless of recursion position, last parenthesis has to be closed
                result.append(p)
            return result
        return recursive_gen('', n, n)


# n = 3
#
#
# def recursive_gen(p, left, right, result=[]):
#     if left:
#         recursive_gen(p + '(', left - 1, right)
#     if right > left:
#         recursive_gen(p + ')', left, right - 1)
#     if right == 0:  # regardless of recursion position, last parenthesis has to be closed
#         result.append(p)
#     return result
#
#
# r = recursive_gen('', n, n)


# def generate_parentheses(n):
#     def backtrack(s, left, right):
#         # Base case
#         if len(s) == 2 * n:
#             result.append(s)
#             return
#
#         # Recursive steps
#         if left < n:
#             backtrack(s + '(', left + 1, right)
#         if right < left:
#             backtrack(s + ')', left, right + 1)
#
#     result = []
#     backtrack('', 0, 0)
#     return result












