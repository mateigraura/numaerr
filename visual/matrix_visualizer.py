from visual.visualizer_base import BaseVisualizer
import matplotlib.pyplot as plt
import matplotlib.cm as cm


class MatrixVisualizer(BaseVisualizer):
    def __init__(self, inputs, labels,
                 strategy="nearest",
                 fig_size=(20, 20),
                 map_type=cm.Greys_r):
        self.inputs = inputs
        self.labels = labels
        self.strategy = strategy
        self.fig_size = fig_size
        self.map_type = map_type if map_type is cm.Greys_r \
            else plt.get_cmap(map_type)

    def show(self, rows=1, cols=1):
        cols = len(self.inputs) if cols is 1 else cols
        _, axes = plt.subplots(nrows=rows,
                               ncols=cols,
                               figsize=self.fig_size)

        if rows > 1:
            self._show_many_rows(axes)
        else:
            self._show_one_row(axes)
        super().set_window()

    def _show_one_row(self, axes):
        for idx, ax in enumerate(axes):
            self._show_figure(idx, ax)

    def _show_many_rows(self, axes):
        for idx, ax in enumerate(axes):
            for sub_idx, sub_ax in enumerate(ax):
                self._show_nested_figure(idx, sub_idx, sub_ax)

    def _show_figure(self, idx, ax):
        ax.imshow(self.inputs[idx],
                  interpolation=self.strategy,
                  cmap=self.map_type)
        ax.set_title(self.labels[idx])
        ax.set_xlabel("Columns")
        ax.set_ylabel("Rows")

    def _show_nested_figure(self, idx, sub_idx, ax):
        ax.imshow(self.inputs[idx][sub_idx],
                  interpolation=self.strategy,
                  cmap=self.map_type)
        ax.set_title(self.labels[idx][sub_idx])
        ax.set_xlabel("Columns")
        ax.set_ylabel("Rows")
