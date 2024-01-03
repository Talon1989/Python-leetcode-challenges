# 7. Reverse Integer
# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes
# the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).


# https://leetcode.com/problems/reverse-integer/


class Solution(object):  # TOP 9%
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x_str = str(x)
        sign = ''
        if x_str[0] == '-':
            x_str = x_str[1:]
            sign = '-'
        value = int(sign + x_str[::-1])
        if not -2 ** 31 <= value <= (2 ** 31 - 1):
            return 0
        return value






