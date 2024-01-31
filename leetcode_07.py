# 11. Container With Most Water
# You are given an integer array height of length n. There are n vertical lines drawn such that
# the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.


# https://leetcode.com/problems/container-with-most-water/


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        i, j = 0, len(height) - 1
        while i != j:
            print('%d %d' % (i, j))
            if height[i] <= height[j]:
                area = height[i] * abs(i-j)
                i += 1
            else:
                area = height[j] * abs(i-j)
                j -= 1
            if area > max_area:
                max_area = area
        return max_area


# height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
# height = [1, 1]
# height = [0, 2]
# height = [6, 5, 3, 1, 2, 7, 8]
# height = [1, 3, 2, 5, 25, 24, 5]


# max_area = 0
# for i in range(len(height)):
#     for j in range(i+1, len(height)):
#         h_1 = min(height[i], height[j])
#         area = h_1 * abs(i-j)
#         if area > max_area:
#             max_area = area
# print(max_area)


# max_area = 0
# for i in range(len(height)):
#     if height[i] == 0:
#         continue
#     for j in range(i+1, len(height))[::-1]:
#         print(j)
#         if max_area / height[i] > abs(i - j):
#             print('impossible improvement')
#             break
#         if height[j] == height[i]:
#             area = height[i] * abs(i - j)
#             if area > max_area:
#                 max_area = area
#             print('max height checked')
#             break
#         area = min(height[i], height[j]) * abs(i - j)
#         if area > max_area:
#             max_area = area
# print(max_area)


# max_area = 0
# i, j = 0, len(height) - 1
# while i != j:
#     print('%d %d' % (i, j))
#     if height[i] <= height[j]:
#         area = height[i] * abs(i-j)
#         i += 1
#     else:
#         area = height[j] * abs(i-j)
#         j -= 1
#     if area > max_area:
#         max_area = area
# print(max_area)
