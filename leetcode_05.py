# 4. Median of Two Sorted Arrays
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).


# https://leetcode.com/problems/median-of-two-sorted-arrays/


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merged_arr = []
        idx_1, idx_2 = 0, 0
        while idx_1 < len(nums1) and idx_2 < len(nums2):
            if nums1[idx_1] <= nums2[idx_2]:
                merged_arr.append(nums1[idx_1])
                idx_1 += 1
            elif nums2[idx_2] < nums1[idx_1]:
                merged_arr.append(nums2[idx_2])
                idx_2 += 1
        if idx_1 < len(nums1):
            merged_arr += nums1[idx_1:]
        elif idx_2 < len(nums2):
            merged_arr += nums2[idx_2:]
        pos = len(merged_arr) / 2
        if pos % 1 == 0:
            pre = int(pos - 0.5)
            post = int(pos + 0.5)
            median = (merged_arr[pre] + merged_arr[post]) / 2
        else:
            median = merged_arr[int(pos - 0.5)]
        return median


# arr_1 = [i for i in range(5)]
# arr_2 = [2, 5, 9, 10]
# pos = len(arr_1) / 2
# pos_1 = len(arr_1) / 2
# pos_2 = len(arr_2) / 2
# if pos_1 % 1 == .5:
#     pre = int(pos_1 - 0.5)
#     post = int(pos_1 + 0.5)
#     print((arr_1[pre] + arr_1[post]) / 2)


# def merge_sorted_arrays(arr_1, arr_2):


# nums1, nums2 = [1,2], [3,4]
nums1, nums2 = [1, 3], [2]


# merged_arr = []
# idx_1, idx_2 = 0, 0
# while idx_1 < len(nums1) and idx_2 < len(nums2):
#     if nums1[idx_1] <= nums2[idx_2]:
#         merged_arr.append(nums1[idx_1])
#         idx_1 += 1
#     elif nums2[idx_2] < nums1[idx_1]:
#         merged_arr.append(nums2[idx_2])
#         idx_2 += 1
# if idx_1 < len(nums1):
#     merged_arr += nums1[idx_1:]
# elif idx_2 < len(nums2):
#     merged_arr += nums2[idx_2:]
# pos = len(merged_arr) / 2
# if pos % 1 == 0:
#     pre = int(pos - 0.5)
#     post = int(pos + 0.5)
#     median = (merged_arr[pre] + merged_arr[post]) / 2
# else:
#     median = merged_arr[int(pos - 0.5)]
# print(median)


merged_arr = []
idx_1, idx_2 = 0, 0
while idx_1 < len(nums1) and idx_2 < len(nums2):
    if nums1[idx_1] <= nums2[idx_2]:
        merged_arr.append(nums1[idx_1])
        idx_1 += 1
    elif nums2[idx_2] < nums1[idx_1]:
        merged_arr.append(nums2[idx_2])
        idx_2 += 1
if idx_1 < len(nums1):
    merged_arr += nums1[idx_1:]
elif idx_2 < len(nums2):
    merged_arr += nums2[idx_2:]
print(merged_arr)
pos = len(merged_arr) / 2.
if pos % 1 == 0:
    pre = int(pos - 0.5)
    post = int(pos + 0.5)
    median = (merged_arr[pre] + merged_arr[post]) / 2.
else:
    median = merged_arr[int(pos - 0.5)]
print(median)




