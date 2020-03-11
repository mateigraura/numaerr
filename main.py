import examples as ex
import argparse

execs = {
    "mat_v": ex.impl_vs_numpy,
    "time_v": ex.impl_vs_numpy_timeit,
    "ch_fail": ex.cholesky_fail,
    "ch_solve": ex.cholesky_solve,
}

parser = argparse.ArgumentParser(description="args from terminal, cool stuff")
parser.add_argument("--m_size", default=100, type=int,
                    help="Size of the input matrix")
parser.add_argument("--opt", default="mat_v", type=str,
                    help="Type of visualization",
                    choices=["mat_v", "time_v", "ch_fail", "ch_solve"])
args = parser.parse_args()

opt = args.opt
m_size = args.m_size

if __name__ == "__main__":
    execs[opt](m_size)
