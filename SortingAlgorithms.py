import numpy as np


# O(n) = unbounded
def bogo_sort(arr):
    import random
    while True:
        random.shuffle(arr)
        flag = True
        for idx in range(len(arr) - 1):
            if arr[idx] > arr[idx+1]:
                flag = False
                break
        if flag:
            return


# O(n) = n^2
def bubble_sort(arr):
    while True:
        flag = True
        for idx in range(1, len(arr)):
            if arr[idx-1] > arr[idx]:
                arr[idx], arr[idx-1] = arr[idx-1], arr[idx]
                flag = False
        if flag:
            return


# O(n) = (n^2) - n
def selection_sort(arr):
    current_idx = 0
    for idx in range(current_idx, len(arr)):
        min_idx = current_idx
        for j in range(idx, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[idx], arr[min_idx] = arr[min_idx], arr[idx]
        current_idx += 1


# O(n) = n^2, avg O(n)= nlog_2(n)
def quick_sort(arr):  # not in-place
    if len(arr) <= 1:
        return arr
    pivot = arr.pop()
    low = [n for n in arr if n <= pivot]
    high = [n for n in arr if n > pivot]
    return quick_sort(low) + [pivot] + quick_sort(high)


# O(n) = nlog_2(n)
def merge_sort(arr):  # not in-place

    def merge(left, right):
        l, r, result = 0, 0, []
        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                result.append(left[l])
                l += 1
            elif left[l] > right[r]:
                result.append(right[r])
                r += 1
        if l < len(left):
            result = result + left[l:]
        elif r < len(right):
            result = result + right[r:]
        return result

    if len(arr) < 2:
        return arr[:]
    middle = len(arr) // 2
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])
    print()
    return merge(left, right)


# O(n) = nlog_2(n)
def merge_sort2(arr):  # not in-place

    def merge(left, right):
        l, r, result = 0, 0, []
        while l < len(left) or r < len(right):
            if left[l] <= right[r]:
                result.append(left[l])
                l += 1
                try:
                    left[l]
                except IndexError:
                    result = result + right[r:]
                    r = len(right)
            elif left[l] > right[r]:
                result.append(right[r])
                r += 1
                try:
                    right[r]
                except IndexError:
                    result = result + left[l:]
                    l = len(left)
        return result

    if len(arr) < 2:
        return arr[:]
    middle = len(arr) // 2
    left = merge_sort2(arr[:middle])
    right = merge_sort2(arr[middle:])
    print()
    return merge(left, right)


arr = np.random.normal(0, 10, 12)
