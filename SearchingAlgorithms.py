import numpy as np


def linear_search(value, arr, out=False):
    for i in range(len(arr)):
        if value == arr[i]:
            if out:
                print(f'Value found at iteration {i:d}')
            return True
    return False


def log_search(value, arr, found=False):
    if len(arr) == 1:
        return True if arr[0] == value else False
    mid_point = len(arr) // 2
    if value == arr[mid_point]:
        return True
    elif value < arr[mid_point]:
        found = log_search(value, arr[:mid_point])
    elif value > arr[mid_point]:
        found = log_search(value, arr[mid_point:])
    return found


def log_search_iterative(value, arr):
    for _ in range(int(np.ceil(np.log2(len(arr))))):
        midpoint = len(arr) // 2
        if value == arr[midpoint]:
            return True
        elif value < arr[midpoint]:
            arr = arr[:midpoint]
        elif value > arr[midpoint]:
            arr = arr[midpoint:]
    return False
