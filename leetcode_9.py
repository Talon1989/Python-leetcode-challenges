# 15. 3Sum
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k,
# and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.


# https://leetcode.com/problems/3sum/


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                summation = nums[i] + nums[left] + nums[right]
                if summation == 0:
                    results.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1  # possible issue with these 2
                    try:
                        while nums[left] == nums[left - 1]:
                            left += 1
                    except IndexError:
                        continue
                    try:
                        while nums[right] == nums[right + 1]:
                            right -= 1
                    except IndexError:
                        continue
                elif summation < 0:
                    left += 1
                elif summation > 0:
                    right -= 1
        return results


# nums = [-1, 0, 1, 2, -1, -4]
# nums = [-2, 0, 0, 2, 2]
# nums = [0, 1, 1]
# nums = [0, 0, 0]


# for i in range(len(nums) - 2):
#     summation = sum(nums[i:i+3])


# results = []
# nums.sort()
# for i in range(len(nums) - 2):
#     if i > 0 and nums[i] == nums[i - 1]:
#         continue
#     left, right = i + 1, len(nums) - 1
#     while left < right:
#         summation = nums[i] + nums[left] + nums[right]
#         if summation == 0:
#             results.append([nums[i], nums[left], nums[right]])
#             left += 1
#             right -= 1  # possible issue with these 2
#             try:
#                 while nums[left] == nums[left - 1]:
#                     left += 1
#             except IndexError:
#                 continue
#             try:
#                 while nums[right] == nums[right + 1]:
#                     right -= 1
#             except IndexError:
#                 continue
#         elif summation < 0:
#             left += 1
#         elif summation > 0:
#             right -= 1
