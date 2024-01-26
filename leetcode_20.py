import math

# 60. Permutation Sequence
# The set [1, 2, 3, ..., n] contains a total of n! unique permutations.
# By listing and labeling all of the permutations in order, we get the following sequence for n = 3:
#     "123"
#     "132"
#     "213"
#     "231"
#     "312"
#     "321"
# Given n and k, return the kth permutation sequence.


n = 3


# n-ary numerical system, won't deal with permutation
def build_numerical_system(n, end=8):
    assert n >= 1
    d = {}
    current = ''
    for i in range(end):
        current += str('0')
    d[1] = current
    for number in range(2, (n**end + 1)):
        last_index = -1
        while True:
            if (int(current[last_index]) + 1) % n == 0:
                last_index -= 1
            else:
                last_vals = ''
                for _ in range(abs(last_index + 1)):
                    last_vals += '0'
                if last_index != 0:
                    current = current[0:last_index] + str(int(current[last_index])+1) + last_vals
                else:
                    current = str(int(current[last_index]) + 1) + last_vals
                d[number] = current
                break
    return d


d = build_numerical_system(2)
