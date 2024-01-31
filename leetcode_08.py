# 12. Integer to Roman
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII,
# which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII.
# Instead, the number four is written as IV. Because the one is before the five we subtract it making four.
# The same principle applies to the number nine, which is written as IX.
# There are six instances where subtraction is used:
#     I can be placed before V (5) and X (10) to make 4 and 9.
#     X can be placed before L (50) and C (100) to make 40 and 90.
#     C can be placed before D (500) and M (1000) to make 400 and 900.
# Given an integer, convert it to a roman numeral.
# Constraints:    1 <= num <= 3999


# https://leetcode.com/problems/integer-to-roman/description/


class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        thousands = int(num / 1000) % 10
        hundreds = int(num / 100) % 10
        tens = int(num / 10) % 10
        ones = int(num / 1) % 10
        d_1000 = 'M' * thousands
        d_100 = ''
        d_10 = ''
        d_1 = ''
        if hundreds != 0:
            if hundreds <= 3:
                d_100 = 'C' * hundreds
            d_100 = 'CD' if hundreds == 4 else d_100
            d_100 = 'D' if hundreds == 5 else d_100
            d_100 = 'DC' if hundreds == 6 else d_100
            d_100 = 'DCC' if hundreds == 7 else d_100
            d_100 = 'DCCC' if hundreds == 8 else d_100
            d_100 = 'CM' if hundreds == 9 else d_100
        if tens != 0:
            if tens <= 3:
                d_10 = 'X' * tens
            d_10 = 'XL' if tens == 4 else d_10
            d_10 = 'L' if tens == 5 else d_10
            d_10 = 'LX' if tens == 6 else d_10
            d_10 = 'LXX' if tens == 7 else d_10
            d_10 = 'LXXX' if tens == 8 else d_10
            d_10 = 'XC' if tens == 9 else d_10
        if ones != 0:
            if ones <= 3:
                d_1 = 'I' * ones
            d_1 = 'IV' if ones == 4 else d_1
            d_1 = 'V' if ones == 5 else d_1
            d_1 = 'VI' if ones == 6 else d_1
            d_1 = 'VII' if ones == 7 else d_1
            d_1 = 'VIII' if ones == 8 else d_1
            d_1 = 'IX' if ones == 9 else d_1
        return d_1000 + d_100 + d_10 + d_1


# num = 1994
# num = 32
#
#
# thousands = int(num / 1000) % 10
# hundreds = int(num / 100) % 10
# tens = int(num / 10) % 10
# ones = int(num / 1) % 10
# d_1000 = 'M' * thousands
# d_100 = ''
# d_10 = ''
# d_1 = ''
# if hundreds != 0:
#     if hundreds <= 3:
#         d_100 = 'C' * hundreds
#     d_100 = 'CD' if hundreds == 4 else d_100
#     d_100 = 'D' if hundreds == 5 else d_100
#     d_100 = 'DC' if hundreds == 6 else d_100
#     d_100 = 'DCC' if hundreds == 7 else d_100
#     d_100 = 'DCCC' if hundreds == 8 else d_100
#     d_100 = 'CM' if hundreds == 9 else d_100
# if tens != 0:
#     if tens <= 3:
#         d_10 = 'X' * tens
#     d_10 = 'XL' if tens == 4 else d_10
#     d_10 = 'L' if tens == 5 else d_10
#     d_10 = 'LX' if tens == 6 else d_10
#     d_10 = 'LXX' if tens == 7 else d_10
#     d_10 = 'LXXX' if tens == 8 else d_10
#     d_10 = 'XC' if tens == 9 else d_10
# if ones != 0:
#     if ones <= 3:
#         d_1 = 'I' * ones
#     d_1 = 'IV' if ones == 4 else d_1
#     d_1 = 'V' if ones == 5 else d_1
#     d_1 = 'VI' if ones == 6 else d_1
#     d_1 = 'VII' if ones == 7 else d_1
#     d_1 = 'VIII' if ones == 8 else d_1
#     d_1 = 'IX' if ones == 9 else d_1
# number = d_1000 + d_100 + d_10 + d_1
#
#
# print(thousands)
# print(hundreds)
# print(tens)
# print(ones)












