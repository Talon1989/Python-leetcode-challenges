import numpy as np


# Given any A ⊆ {1, 2, 3, . . . , 100} for which |A| = 10, there
# exist two different subsets X ⊆ A and Y ⊆ A for which the sum of the elements
# in X is equal to the sum of the elements in Y .


A = np.random.randint(1, 100, 10)
while True:
    X = np.random.choice(A, size=5, replace=False)
    Y = np.random.choice(A, size=5, replace=False)
    if not np.all(X == Y):
        break


