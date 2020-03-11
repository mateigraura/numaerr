from impl.matrices import (
    positive_definite_matrix
)
from impl.cholesky import cholesky_decomposition
from impl.lineq_solver import solve_cholesky
import numpy as np
import visual as vs


def impl_vs_numpy(m_size):
    M = positive_definite_matrix(size=m_size)
    L = cholesky_decomposition(M)
    L_NP = np.linalg.cholesky(M)

    mv = vs.MatrixVisualizer(inputs=((M, L, L.T, np.dot(L, L.T)),
                                     (M, L_NP, L_NP.T, np.dot(L_NP, L_NP.T))),
                             labels=(("Initial Matrix",
                                      "Lower triangular - L",
                                      "Transpose - L'",
                                      "Recomposed matrix (L*L')"),
                                     ("Initial Matrix",
                                      "Numpy - Lower triangular - L",
                                      "Numpy - Transpose - L'",
                                      "Recomposed matrix (L*L')")),
                             map_type="flag")
    mv.show(rows=2, cols=4)


def impl_vs_numpy_timeit(m_size):
    matrix = positive_definite_matrix(size=m_size)
    funcs = [cholesky_decomposition, np.linalg.cholesky]
    labels = ("Implemented Cholesky", "Numpy Cholesky")
    tv = vs.TimeVisualizer(funcs=funcs,
                           data=matrix,
                           labels=labels,
                           iterations=200)
    tv.show()


def cholesky_fail(m_size):
    matrix = rand_matrix(m_size)
    try:
        cholesky_decomposition(matrix)
    except Exception as e:
        print(e)

    mv = vs.MatrixVisualizer(inputs=matrix,
                             labels="Random matrix",
                             map_type="plasma")
    mv.show()


def cholesky_solve(m_size):
    matrix = [[4, 12, -16], [12, 37, -43], [-16, -43, 98]]
    coef = np.array([2, 5, 3]).reshape((3, 1))
    L = cholesky_decomposition(matrix)
    x = solve_cholesky(matrix, coef)
    mv = vs.MatrixVisualizer(inputs=(matrix, L, L.T, x),
                             labels=("Matrix", "Lower triangular",
                                     "Transpose - L'", "X solution"),
                             map_type="plasma")
    mv.show(rows=1, cols=4)
    print("Matrix A")
    print(matrix)
    print("B coefficient: ")
    print(coef)
    print("X solution: ")
    print(x)
