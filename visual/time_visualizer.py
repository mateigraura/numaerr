from visual.visualizer_base import BaseVisualizer
import matplotlib.pyplot as plt
import numpy as np
import time
import os


class TimeVisualizer(BaseVisualizer):
    def __init__(self, funcs, data, labels, iterations):
        self.funcs = []
        self.data = data
        self.labels = labels
        self.iterations = iterations
        for idx, func in enumerate(funcs):
            self.funcs.append(func)

    def show(self):
        ts = {key: None for key in range(len(self.funcs))}

        for key, func in enumerate(self.funcs):
            ts[key] = self._timeit(key)

        self._plot(ts)
        super().set_window()

    def _timeit(self, idx):
        t = []
        for _ in range(self.iterations):
            t0 = time.time()
            self.funcs[idx](self.data)
            t1 = time.time()
            t.append(int((t1 - t0) * 10 ** 9))
        return t

    def _plot(self, ts):
        fig, axes = plt.subplots(nrows=len(ts), ncols=1)
        fig.tight_layout(pad=4.0)
        for key, ax in enumerate(axes):
            ax.plot(ts[key],
                    label="Data",
                    linestyle="--")
            ax.plot([np.mean(ts[key]) for _ in ts[key]],
                    label="Average",
                    marker='*')
            ax.legend(loc='upper right')
            ax.set_title(self.labels[key])
            ax.set_xlabel("Iterations")
            ax.set_ylabel("Nanoseconds")
