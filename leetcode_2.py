

def reverse_array(arr):  # nested data has to have the same shape
    dimensions = []
    while True:
        try:
            dimensions.append(len(arr))
            arr = arr[0]
        except TypeError:
            break
    tot = []
    for dim in range(len(dimensions)):
        cop = arr[::-1]


def nested_loop(n, size=5, current=0):
    if n == current:
        return
    for j in range(size):
        print(j)
    nested_loop(n, size, current+1)


def recursion_fibonacci(current=0, i=0, i_=1, end=10):
    if current == end:
        return
    print(i)
    i, i_ = i_, (i + i_)
    recursion_fibonacci(current+1, i, i_, end)


my_list = [
    [
        [1, 2, 3], [2, 4, 8]
    ],
    [
        [5, 6, 8], [11, 22, 33]
    ],
    [
        [6, 7, 11], [54, 77, 88]
    ]
]



