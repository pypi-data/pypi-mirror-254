# %%
import numpy as np
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt
import tensorflow.experimental.numpy as tnp  # type:ignore

tnp.experimental_enable_numpy_behavior()

__all__ = ["DataWindow"]


class DataWindow:
    def __init__(
        self,
        input_width: int,
        hrzn_width: int,
        shift: int,
        train: pd.DataFrame,
        val: pd.DataFrame,
        test: pd.DataFrame,
        pred_cols: list[str],
        n_batch: int = 32,
    ):
        self._input_width, self._hrzn_width, self._shift = (
            input_width,
            hrzn_width,
            shift,
        )
        self.n_batch = n_batch
        self._pred_col_indices = {
            label: i for i, label in enumerate(pred_cols)
        }
        self._pred_cols = pred_cols
        self._col_indices = {
            column: i for i, column in enumerate(train.columns)
        }
        self._train, self._val, self._test = (
            np.array(train),
            np.array(val),
            np.array(test),
        )

        self._wnd_width = input_width + shift
        self._input_slice = slice(0, input_width)
        self._hrzn_slice = slice(self._wnd_width - hrzn_width, None)

    def _make_dataset(self, data: np.ndarray):
        def _input_hrzn_split(data):
            inputs, hrzns = (
                data[:, self._input_slice, :],
                data[
                    :,
                    self._hrzn_slice,
                    [self._col_indices[name] for name in self._pred_cols],
                ],
            )
            return inputs, hrzns

        ds = tf.keras.preprocessing.timeseries_dataset_from_array(  # type:ignore
            data=data,
            targets=None,
            sequence_length=self._wnd_width,
            sequence_stride=1,
            shuffle=True,
            batch_size=self.n_batch,
        )
        return ds.map(_input_hrzn_split)

    def plot(
        self, plot_col: str, model=None, n_subplot=3, xlabel="", ylabel=""
    ):
        input_indices = np.arange(self._wnd_width)[self._input_slice]
        label_indices = np.arange(self._wnd_width)[self._hrzn_slice]
        inputs, hrzns = next(iter(self.train))

        fig, ax = plt.subplots(nrows=n_subplot, ncols=1, figsize=(12, 8))
        for i in range(n_subplot):
            ax[i].plot(
                input_indices,
                inputs[i, :, self._col_indices[plot_col]],
                label="Inputs",
                marker=".",
                zorder=-10,
            )
            ax[i].scatter(
                label_indices,
                hrzns[i, :, self._pred_col_indices[plot_col]],
                edgecolors="k",
                marker="s",
                label="Labels",
                c="green",
                s=64,
            )
            if model is not None:
                preds = model(inputs)
                ax[i].scatter(
                    label_indices,
                    preds[i, :, self._pred_col_indices[plot_col]],
                    marker="X",
                    edgecolors="k",
                    label="Predictions",
                    c="red",
                    s=64,
                )
            ax[i].set_ylabel(ylabel)
        plt.legend(loc="best")
        plt.xlabel(xlabel)
        plt.tight_layout()
        return fig

    @property
    def train(self):
        return self._make_dataset(self._train)

    @property
    def val(self):
        return self._make_dataset(self._val)

    @property
    def test(self):
        return self._make_dataset(self._test)
