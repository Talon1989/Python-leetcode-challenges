# 41. First Missing Positive
# Given an unsorted integer array nums, return the smallest missing POSITIVE integer.
# You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        num_dict = {i: False for i in range(1, (len(nums) * 2) + 1)}
        for n in nums:
            try:
                num_dict[n] = True
            except KeyError:
                continue
        for n, b in num_dict.items():
            if not b:
                return n


# nums = [7, 8, 9, 11, 12]
# nums = [3, 4, -1, 1]
nums = [1, 2, 0]


# idea is to populate a dictionary with numbers in nums as keys and False booleans
# then go through nums list and turn present numbers into True booleans of respective number in dict
# as soon as we find a False we return it


# num_dict = {i: False for i in range(1, (len(nums) * 2) + 1)}
# min_val = 0
# flag = False  # flag to set the first min positive integer
# for n in nums:
#     if n > 0 and not flag:  # set the first min positive integer
#         min_val = n
#         flag = True
#     if 0 < n < min_val and flag:
#         min_val = n
#     try:
#         num_dict[n] = True
#     except KeyError:
#         continue
# if min_val == 0:
#     print(1)
# for n, b in num_dict.items():
#     if not b and n > min_val:
#         print(n)


num_dict = {i: False for i in range(1, (len(nums) * 2) + 1)}
for n in nums:
    try:
        num_dict[n] = True
    except KeyError:
        continue
for n, b in num_dict.items():
    if not b:
        print(n)
