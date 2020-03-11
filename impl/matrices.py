from scipy import random
import numpy as np


def hilbert_matrix(size=3):
    M = np.zeros(shape=(size, size), dtype=np.float64)
    for i in range(size):
        for j in range(size):
            M[i][j] = 1.0 / ((i + 1) + (j + 1) - 1.0)
    return M


def positive_definite_matrix(size=3, alpha=1.0):
    """

    :param size: size of matrix
    :param alpha: arbitrary positive number
    :return: A positive definite matrix

    For alpha > 0 the eigenvalues should be >= alpha,
    which makes the returned matrix a PDM (I hope)

    """
    M = random.rand(size, size)
    I = np.dot(np.identity(size), alpha)
    return np.dot(M, M.T) + I


def rand_matrix(size=3):
    return random.rand(size, size)
