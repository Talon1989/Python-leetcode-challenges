# 42. Trapping Rain Water
# Given n non-negative integers representing
# an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        water_units = 0
        idx = 0
        while idx < len(height):
            counter = 1
            temp_unit = 0
            starter = height[idx]
            # print(counter)
            for y in range(idx + 1, len(height)):
                if height[y] >= starter:
                    # print(f'breaking {idx} at {y} , counter {counter}')
                    break
                current_water = abs(starter - height[y])
                temp_unit += current_water
                # print(f'unit {y} , value {current_water}')
                counter += 1
                if y == len(height) - 1:
                    counter = 1
                    # print(counter)
                    temp_unit = 0
                    break
            water_units += temp_unit
            idx += counter
        return water_units


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# height = [4, 2, 0, 3, 2, 5]
# height = [4, 2, 3]


# IDEA: maybe naive approach, count possible water area until next >= block


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


pivot = height.index(max(height))
# LEFT
# going_down = 10**5
# maximum = height[pivot]
left_pivot = pivot
left_water = 0
while True:
    max_value = 0
    max_index = None
    previous_value = height[left_pivot]  # to check decreasing values
    flag = True  # flag indicating decreasing values
    old_pivot = left_pivot
    for idx in range(0, left_pivot)[::-1]:
        try:
            if height[idx] > previous_value:  # if one block is longer than previous we are not falling down
                flag = False
            if height[idx] > max_value:
                max_index = idx
                max_value = height[idx]
            previous_value = height[idx]
        except IndexError:
            break
        if flag:
            left_pivot = -1
        else:
            left_pivot = max_index
    if left_pivot == -1:
        break
    print(f'old pivot {old_pivot} | left pivot {left_pivot}')
    # summate waters
    for idx in range(left_pivot+1, old_pivot):
        left_water += abs(max_value - height[idx])
    if left_pivot == 0:
        break

# RIGHT
# going_down = 10**5
# maximum = height[pivot]
right_pivot = pivot
right_water = 0
while True:
    max_value = 0
    max_index = None
    previous_value = height[right_pivot]  # to check decreasing values
    flag = True  # flag indicating decreasing values
    old_pivot = right_pivot
    for idx in range(right_pivot+1, len(height)):
        try:
            if height[idx] > previous_value:  # if one block is longer than previous we are not falling down
                flag = False
            if height[idx] > max_value:
                max_index = idx
                max_value = height[idx]
            previous_value = height[idx]
        except IndexError:
            break
        if flag:
            right_pivot = -1
        else:
            right_pivot = max_index
    if right_pivot == -1:
        break
    print(f'old pivot {old_pivot} | right pivot {right_pivot}')
    # summate waters
    for idx in range(old_pivot+1, right_pivot):
        right_water += abs(max_value - height[idx])
    if right_pivot == len(height) - 1:
        break


total_water = left_water + right_water

