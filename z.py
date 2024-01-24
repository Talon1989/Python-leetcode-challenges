import numpy as np
import time


# Given any A ⊆ {1, 2, 3, . . . , 100} for which |A| = 10, there
# exist two different subsets X ⊆ A and Y ⊆ A for which the sum of the elements
# in X is equal to the sum of the elements in Y .


# A = np.random.randint(1, 100, 10)
# while True:
#     X = np.random.choice(A, size=5, replace=False)
#     Y = np.random.choice(A, size=5, replace=False)
#     if not np.all(X == Y):
#         break


def fibonacci(n, n_1=0, n_2=1, iteration=1):
    assert iteration > 0
    assert iteration <= n
    if iteration == n:
        return n_2
    n_1, n_2 = n_2, n_1 + n_2
    return fibonacci(n, n_1, n_2, iteration + 1)


def fib_1(n):
    if n <= 1:
        return 1
    return fib_1(n-2) + fib_1(n-1)


def fib_2(n, d={}):
    if n in d:
        return d[n]
    if n <= 1:
        value = n
    else:
        value = fib_2(n - 1, d) + fib_2(n - 2, d)
    d[n] = value
    return value


t = time.time()
fib_1(35)
print(f'35 fibonacci with default implementation | time: {time.time() - t: .6f} seconds')

t = time.time()
fib_2(35)
print(f'35 fibonacci with faster implementation | time: {time.time() - t: .6f} seconds')

t = time.time()
fibonacci(35)
print(f'35 fibonacci with custom implementation | time: {time.time() - t: .6f} seconds')
