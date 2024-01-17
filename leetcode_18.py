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


# height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# height = [4, 2, 0, 3, 2, 5]
height = [4, 2, 3]


# IDEA: maybe naive approach, count possible water area until next >= block


water_units = 0
idx = 0
while idx < len(height):
    counter = 1
    temp_unit = 0
    starter = height[idx]
    for y in range(idx+1, len(height)):
        if height[y] >= starter:
            print(f'breaking {idx} at {y} , counter {counter}')
            break
        current_water = abs(starter - height[y])
        temp_unit += current_water
        print(f'unit {y} , value {current_water}')
        counter += 1
        if y == len(height) - 1:
            counter = 1
            temp_unit = 0
            break
    water_units += temp_unit
    idx += counter




