from impl.matrices import positive_definite_matrix
from impl.cholesky import cholesky_decomposition
import numpy as np
import visual as vs


def impl_vs_numpy(m_size=100):
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


def impl_vs_numpy_timeit(m_size=40):
    matrix = positive_definite_matrix(size=m_size)
    funcs = [cholesky_decomposition, np.linalg.cholesky]
    labels = ("Implemented Cholesky", "Numpy Cholesky")
    visualizer = vs.TimeVisualizer(funcs=funcs,
                                   data=matrix,
                                   labels=labels)
    visualizer.show()
