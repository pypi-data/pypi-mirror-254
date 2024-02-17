from tensorflow.keras import Model  # type:ignore
import tensorflow as tf
import tensorflow.experimental.numpy as tnp  # type:ignore

tnp.experimental_enable_numpy_behavior()

__all__ = ["Baseline", "MultiStepLastBaseline"]


class Baseline(Model):
    def __init__(self, pred_col_indices: list[int]):
        super().__init__()
        self.pred_col_indices = pred_col_indices

    def call(self, inputs):
        return inputs[:, :, self.pred_col_indices]


class MultiStepLastBaseline(Model):
    def __init__(self, pred_col_indices: list[int], hrzn: int):
        super().__init__()
        self.pred_col_indices = pred_col_indices
        self.hrzn = hrzn

    def call(self, inputs):
        return tf.tile(
            inputs[:, -1:, self.pred_col_indices], [1, self.hrzn, 1]
        )
