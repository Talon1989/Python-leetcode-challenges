# 42. Trapping Rain Water
# Given n non-negative integers representing
# an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        while left < right:
            left_max, right_max = max(height[left], left_max), max(height[right], right_max)
            if left_max <= right_max:
                water += left_max - height[left]
                left += 1
            else:
                water += right_max - height[right]
                right -= 1
        return water


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# height = [4, 2, 0, 3, 2, 5]
# height = [4, 2, 3]


# IDEA: maybe naive approach, count possible water area until next >= block
# THIS DOESN'T WORK


# water_units = 0
# idx = 0
# while idx < len(height):
#     counter = 1
#     temp_unit = 0
#     starter = height[idx]
#     for y in range(idx+1, len(height)):
#         if height[y] >= starter:
#             print(f'breaking {idx} at {y} , counter {counter}')
#             break
#         current_water = abs(starter - height[y])
#         temp_unit += current_water
#         print(f'unit {y} , value {current_water}')
#         counter += 1
#         if y == len(height) - 1:
#             counter = 1
#             temp_unit = 0
#             break
#     water_units += temp_unit
#     idx += counter


# IDEA: get index of max block height then start going left and right
# check for max value of block height then stop, get values in between with max(pivot, current) - height[i]
# max value of height becomes new pivot, repeat until each successive iteration is <= previous or out of index
# THIS WORKS BUT IT'S SLOW


# pivot = height.index(max(height))
# # LEFT
# left_pivot = pivot
# left_water = 0
# while True:
#     max_value = 0
#     max_index = None
#     previous_value = height[left_pivot]  # to check decreasing values
#     flag = True  # flag indicating decreasing values
#     old_pivot = left_pivot
#     for idx in range(0, left_pivot)[::-1]:
#         if height[idx] > previous_value:  # if one block is longer than previous we are not falling down
#             flag = False
#         if height[idx] > max_value:
#             max_index = idx
#             max_value = height[idx]
#         previous_value = height[idx]
#     if flag:
#         break
#     else:
#         left_pivot = max_index
#     print(f'old pivot {old_pivot} | left pivot {left_pivot}')
#     # summate waters
#     for idx in range(left_pivot+1, old_pivot):
#         left_water += abs(max_value - height[idx])
#     if left_pivot == 0:
#         break
# # RIGHT
# right_pivot = pivot
# right_water = 0
# while True:
#     max_value = 0
#     max_index = None
#     previous_value = height[right_pivot]  # to check decreasing values
#     flag = True  # flag indicating decreasing values
#     old_pivot = right_pivot
#     for idx in range(right_pivot+1, len(height)):
#         if height[idx] > previous_value:  # if one block is longer than previous we are not falling down
#             flag = False
#         if height[idx] > max_value:
#             max_index = idx
#             max_value = height[idx]
#         previous_value = height[idx]
#     if flag:
#         break
#     else:
#         right_pivot = max_index
#     print(f'old pivot {old_pivot} | right pivot {right_pivot}')
#     # summate waters
#     for idx in range(old_pivot+1, right_pivot):
#         right_water += abs(max_value - height[idx])
#     if right_pivot == len(height) - 1:
#         break
# # summate the total left water and right water with respect to higher block
# total_water = left_water + right_water


# IDEA: starting from left and right the max height will always be max between the two because there's no container
# (there might be inside). Then we check which of the two has less maximum value, store the total max - current height
# and increase (left) or decrease (right) the index.
# repeat until left >= right breaking the iteration since all heights have been passed
# THIS WORKS WITH GOOD SPEED


# water = 0
# left, right = 0, len(height) - 1
# left_max, right_max = height[left], height[right]
# while left < right:
#     left_max, right_max = max(height[left], left_max), max(height[right], right_max)
#     if left_max <= right_max:
#         water += left_max - height[left]
#         left += 1
#     else:
#         water += right_max - height[right]
#         right -= 1


