import examples as ex

ch = "time"

if __name__ == "__main__":
    if ch == "time":
        ex.impl_vs_numpy_timeit()
    else:
        ex.impl_vs_numpy()
