# 44. Wildcard Matching
# Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:
#     '?' Matches any single character.
#     '*' Matches any sequence of characters (including the empty sequence).
# The matching should cover the entire input string (not partial).
import time


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        self.memo = {}
        # if len(s) == 0 and len(p) > 0:  # check for empty s cases
        #     return self.is_p_full_star(p)
        # return self.func(s, p)
        return self.func_dict(s, p)

    # def func(self, s, p, last_star=False):
    #     if not s or not p:  # ending cases
    #         if s and not p:
    #             if last_star:
    #                 return True
    #             else:
    #                 return False
    #         elif not s and p:
    #             return self.is_p_full_star(p)
    #         else:
    #             return True
    #     if p[0] == '*':  # let's start to check every possibility
    #         if self.func(s, p[1:], last_star=True):
    #             return True
    #         for idx in range(len(s)):
    #             if self.func(s[idx:], p[1:], last_star=True):
    #                 return True
    #         return False
    #     elif p[0] == '?':
    #         return self.func(s[1:], p[1:], last_star=False)
    #     elif s[0] == p[0] and self.func(s[1:], p[1:], last_star=False):
    #         return True
    #     else:
    #         return False

    def func_dict(self, s, p):
        if (s, p) in self.memo:
            return self.memo[(s, p)]
        if not p:
            return not s  # returns True if empty string
        if not s:
            return len(p) == p.count('*')  # returns True if all elements of p are '*'
        if p[0] == '*':  # let's start to check every possibility
            self.memo[(s, p)] = (self.func_dict(s, p[1:]) or
                                 (len(s) > 0 and self.func_dict(s[1:], p)))  # for '*' matching later characters of s
        elif p[0] == '?' or s[0] == p[0]:  # keep going
            self.memo[(s, p)] = len(s) > 0 and self.func_dict(s[1:], p[1:])
        else:
            self.memo[(s, p)] = False
        return self.memo[(s, p)]

    # def is_p_full_star(self, p):
    #     for c in p:
    #         if c != '*':
    #             return False
    #     return True


# FASTER SOLUTION (not mine)
# class Solution:
#     def isMatch(self, s: str, p: str) -> bool:
#         dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
#         dp[-1][-1] = True
#         for i in range(len(s), -1, -1):
#             for j in range(len(p) - 1, -1, -1):
#                 match = i < len(s) and (s[i] == p[j] or p[j] == '?')
#                 if p[j] == '*':
#                     dp[i][j] = dp[i][j+1] or (i < len(s) and dp[i+1][j])
#                 else:
#                     dp[i][j] = match and (i < len(s) and dp[i+1][j+1])
#         return dp[0][0]


# s, p = 'aa', 'a'
s, p = 'aa', '*'
# s, p = 'cb', '?a'
# s, p = 'abcdefg', 'ab*fg'
# s, p = 'abcd', 'ab****wewe'
# s, p = "", "*****"
# s, p = '', '*a*'
# s, p = 'ho', 'ho**'
# s, p = "bbbaaabbababbaabbabbbbba", "*ab*****b"
# s, p = "aaabbbaabaaaaababaabaaabbabbbbbbbbaabababbabbbaaaaba", "a*******b"


# IDEA: the 'big deal' is the '*' operator, given all others we could just iterate through the string
# and check if one fails returning False.
# let's then use a bruteforce approach with a recursive method that checks 'everything' once it encounters '*'
# THIS IS COMPUTATIONALLY TOO EXPENSIVE (TIME WISE) PROBABLY NEED TO USE SOME RECURSION + MEMOIZATION


def func(s, p, last_star=False):
    if not s or not p:  # ending cases
        if s and not p:
            if last_star:
                return True
            else:
                return False
        elif not s and p:
            if p == '*':
                return True
            else:
                return False
        else:
            return True
    if p[0] == '*':  # let's start to check every possibility
        if func(s, p[1:], last_star=True):
            return True
        for idx in range(len(s)):
            if func(s[idx:], p[1:], last_star=True):
                return True
        return False
    elif p[0] == '?':
        return func(s[1:], p[1:], last_star=False)
    elif s[0] == p[0] and func(s[1:], p[1:], last_star=False):
        return True
    else:
        return False


# t = time.time()
print(Solution().isMatch(s, p))
# print(f'{time.time() - t: .3f} seconds')
