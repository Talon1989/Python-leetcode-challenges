# 44. Wildcard Matching
# Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:
#     '?' Matches any single character.
#     '*' Matches any sequence of characters (including the empty sequence).
# The matching should cover the entire input string (not partial).


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        pass


# s, p = 'aa', 'a'
# s, p = 'aa', '*'
s, p = 'cb', '?a'


# IDEA: the 'big deal' is the '*' operator, given all others we could just iterate through the string
# and check if one fails returning False.
# let's then use a bruteforce approach with a recursive method that checks 'everything' once it encounters '*'


def func(s, p, last_star=False):
    if not s or not p:
        if s and not p:
            if last_star:
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




