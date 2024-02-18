"""Theia implemented using a CNN in Tensorflow."""
import pathlib
import typing

import numpy
import tensorflow
from tensorflow.python import keras
from tensorflow.python.keras import callbacks
from tensorflow.python.keras import layers
from tensorflow.python.keras import metrics

from ..data_gen import TileGenerator
from .base import Theia

__all__ = ["Neural"]


class Neural(Theia, keras.Model):  # type: ignore[misc]
    """Theia implemented using a CNN in Tensorflow.

    The architecture is a generalization of Siamese Networks, and performs the
    equivalent of LASSO regression.
    """

    def __init__(
        self,
        *,
        num_channels: int,
        channel_overlap: int,
        kernel_size: int,
        alpha: float,
        beta: float,
        tile_size: int,
    ) -> None:
        """Initialize a Theia model.

        This model will estimate the bleedthrough and interaction between channels
        in a multi-channel image. The bleedthrough terms are a measure of how much
        of each channel is present in the other channels. The interaction terms are
        a measure of how much is co-localized among a pair of channels.

        The interaction term is defined as:

            (target * neighbor^beta)^(1 / (1 + beta))

        Args:
            num_channels: The number of channels in the input image.
            channel_overlap: The number of channels to consider on either side of
            the current channel.
            kernel_size: The size of the convolutional kernels.
            alpha: The L1 regularization parameter.
            beta: The L2 regularization parameter.
            tile_size: The side-length of the square tiles to use as inputs to the
            network.
        """
        keras.Model.__init__(self)
        Theia.__init__(
            self,
            num_channels=num_channels,
            channel_overlap=channel_overlap,
            kernel_size=kernel_size,
            alpha=alpha,
            beta=beta,
        )

        self._callbacks: list[callbacks.Callback] = []

        self._tile_shape = (tile_size, tile_size, 1)
        self._sources = [
            layers.Input(self._tile_shape, name=f"source_{i}")
            for i in range(num_channels)
        ]

        self._kernel_names = []
        self._num_kernels: list[int] = []
        self._contributions: list[list[_TheiaConv]] = []
        self._aggregators: list[_Aggregator] = []

        for source_index, source in enumerate(self._sources):
            contributions: list[_TheiaConv] = []

            for offset in range(-self._channel_overlap, self._channel_overlap + 1):
                if offset == 0:
                    continue

                neighbor_index = source_index + offset
                if neighbor_index not in range(self._num_channels):
                    continue

                neighbor = self._sources[neighbor_index]
                contribution = _TheiaConv(
                    name=f"contribution_{source_index}_{neighbor_index}",
                    kernel_size=self._kernel_size,
                )(neighbor)
                self._kernel_names.append((True, source_index, neighbor_index))
                contributions.append(contribution)

                interaction_term = tensorflow.pow(neighbor, self._beta)
                interaction_term = tensorflow.multiply(interaction_term, source)
                interaction_term = tensorflow.pow(
                    interaction_term,
                    1 / (1 + self._beta),
                )
                interaction = _TheiaConv(
                    name=f"interactions_{source_index}_{neighbor_index}",
                    kernel_size=self._kernel_size,
                )(interaction_term)
                self._kernel_names.append((False, source_index, neighbor_index))
                contributions.append(interaction)

            self._num_kernels.append(len(contributions))
            self._contributions.append(contributions)
            self._aggregators.append(
                _Aggregator(name=f"aggregation_{source_index}")(
                    [source, *contributions],
                ),
            )

        self.inputs = self._sources
        self.outputs = self._aggregators

        self._model = keras.Model(
            inputs=self.inputs,
            outputs=self.outputs,
        )
        self.loss_tracker = metrics.Mean(name="theia_loss")

        super().build(
            [
                (None, self.tile_size, self.tile_size, 1)
                for _ in range(self.num_channels)
            ],
        )

    @property
    def tile_size(self) -> int:
        """Side-length of square tiles to use as inputs to the network."""
        return self._tile_shape[0]

    def fit_theia(  # type: ignore[override]
        self,
        *,
        train_gen: TileGenerator,
        valid_gen: TileGenerator,
        epochs: int,
        verbose: int,
    ) -> None:
        """Fit the Theia model.

        Args:
            train_gen: A generator that yields training data.
            valid_gen: A generator that yields validation data.
            epochs: The number of epochs to train for.
            verbose: The verbosity level.
        """
        self.fit(
            x=train_gen,
            epochs=epochs,
            verbose=verbose,
            callbacks=self._callbacks,
            validation_data=valid_gen,
        )

        random_inputs = [
            numpy.random.random((1, *self._tile_shape))
            for _ in range(self._num_channels)
        ]
        outputs = self(random_inputs)

        kernels: numpy.ndarray = numpy.squeeze(
            numpy.stack(
                [k for out in outputs for k in tensorflow.unstack(out[-1])],
                axis=0,
            ),
        ).astype(numpy.float32)
        named_kernels = {
            name: kernels[i, ...] for i, name in enumerate(self._kernel_names)
        }

        self._contribution_kernels = {
            (i, j): k for (b, i, j), k in named_kernels.items() if b
        }

        self._interactions_kernels = {
            (i, j): k for (b, i, j), k in named_kernels.items() if not b
        }

    def early_stopping(
        self,
        *,
        min_delta: float,
        patience: int,
        verbose: int,
        restore_best_weights: bool,
    ) -> None:
        """Add an early stopping callback to the model.

        Args:
            min_delta: The minimum change in the monitored quantity to qualify as
            an improvement.
            patience: The number of epochs with no improvement after which training
            will be stopped.
            verbose: The verbosity level.
            restore_best_weights: Whether to restore model weights from the epoch
            with the best value of the monitored quantity.
        """
        self._callbacks.append(
            callbacks.EarlyStopping(
                monitor="val_theia_loss",
                min_delta=min_delta,
                patience=patience,
                verbose=verbose,
                mode="min",
                restore_best_weights=restore_best_weights,
            ),
        )

    def add_callback(self, cb: callbacks.Callback) -> None:
        """Add a callback to the model."""
        self._callbacks.append(cb)

    def save(self, path: pathlib.Path) -> None:
        """Save the model to the given `path`."""
        raise NotImplementedError

    @staticmethod
    def load(path: pathlib.Path) -> "Neural":
        """Load the model from the given `path`."""
        raise NotImplementedError

    def call(
        self,
        inputs: list[tensorflow.Tensor],
        training: typing.Optional[  # noqa: ARG002
            typing.Union[bool, tensorflow.Tensor]
        ] = None,
        mask: typing.Optional[  # noqa: ARG002
            typing.Union[tensorflow.Tensor, list[tensorflow.Tensor]]
        ] = None,
    ) -> list[tuple[tensorflow.Tensor, tensorflow.Tensor]]:
        """Call the model on the given inputs.

        Args:
            inputs: A list of tensors, one for each channel.
            training: Whether the call is in training mode.
            mask: A mask or list of masks, one for each channel.
        """
        return self._model(inputs)  # type: ignore[no-any-return]

    def train_step(self, inputs: list[tensorflow.Tensor]) -> dict[str, float]:
        """Take one step of training the model.

        Args:
            inputs: A list of tensors, one for each channel.

        Returns:
            A dictionary mapping metric names to their values.
        """
        with tensorflow.GradientTape() as tape:
            losses = self._compute_loss(inputs)

        trainable_weights = self._model.trainable_weights
        gradients = tape.gradient(losses, trainable_weights)
        self.optimizer.apply_gradients(zip(gradients, trainable_weights))

        self.loss_tracker.update_state(tensorflow.reduce_mean(losses))
        return {self.loss_tracker.name: self.loss_tracker.result()}

    def test_step(self, inputs: list[tensorflow.Tensor]) -> dict[str, float]:
        """Take one step of testing/validating the model.

        Args:
            inputs: A list of tensors, one for each channel.

        Returns:
            A dictionary mapping metric names to their values.
        """
        losses = self._compute_loss(inputs)
        self.loss_tracker.update_state(tensorflow.reduce_mean(losses))
        return {self.loss_tracker.name: self.loss_tracker.result()}

    def _compute_loss(self, inputs: list[tensorflow.Tensor]) -> list[tensorflow.Tensor]:
        """Compute the loss for the given inputs.

        Args:
            inputs: A list of tensors, one for each channel.

        Returns:
            A list of losses, one for each channel.
        """
        losses = []

        for n, (corrected, kernels) in zip(self._num_kernels, self._model(inputs)):
            sq_error = tensorflow.reduce_mean(tensorflow.square(corrected))

            kernel_stack = tensorflow.abs(tensorflow.stack(kernels))
            l1_penalty = self._alpha * tensorflow.reduce_mean(kernel_stack)

            loss = tensorflow.maximum(sq_error + l1_penalty, 0.0)
            losses.extend([loss] * n)

        return losses

    @property
    def metrics(self) -> list[metrics.Metric]:
        """Return the model's metrics."""
        return [self.loss_tracker]

    def get_config(self) -> None:
        """Return the model's configuration."""
        raise NotImplementedError

    def _serialize_to_tensors(self) -> None:
        raise NotImplementedError

    def _restore_from_tensors(
        self,
        restored_tensors: dict[str, tensorflow.Tensor],
    ) -> None:
        raise NotImplementedError


class _TheiaConv(layers.Conv2D):  # type: ignore[misc]
    """A convolutional layer that returns the kernel as well as the output."""

    def __init__(
        self,
        *,
        name: str,
        kernel_size: int,
    ) -> None:
        """Initialize the layer.

        Args:
            name: The name of the layer.
            kernel_size: The size of the kernel.
        """
        super().__init__(
            name=name,
            filters=1,
            padding="same",
            kernel_size=kernel_size,
            use_bias=False,
            kernel_constraint=tensorflow.keras.constraints.NonNeg(),
        )

    def call(
        self,
        bleedthrough_term: tensorflow.Tensor,
    ) -> tuple[tensorflow.Tensor, tensorflow.Tensor]:
        """Call the layer on the given inputs.

        Args:
            bleedthrough_term: The bleedthrough term.

        Returns:
            A tuple of the output and the kernel.
        """
        conv = super().call(bleedthrough_term)
        return conv, self.kernel

    def _serialize_to_tensors(self) -> None:
        raise NotImplementedError

    def _restore_from_tensors(
        self,
        restored_tensors: dict[str, tensorflow.Tensor],
    ) -> None:
        raise NotImplementedError


class _Aggregator(layers.Layer):  # type: ignore[misc]
    """A layer that aggregates the bleedthrough terms."""

    def __init__(self, *, name: str) -> None:
        """Initialize the layer.

        Args:
            name: The name of the layer.
        """
        super().__init__(name=name)

    def get_config(self) -> typing.Any:  # noqa: ANN401
        """Return the layer's configuration."""
        return super().get_config()

    # noinspection PyMethodOverriding
    def call(
        self,
        inputs: list[tensorflow.Tensor],
    ) -> tuple[tensorflow.Tensor, tensorflow.Tensor]:
        """Call the layer on the given inputs.

        Args:
            inputs: A list of tensors, one for each channel.

        Returns:
            A tuple of the output and the kernels.
        """
        [source, *contributors] = inputs

        kernels = tensorflow.stack([k for _, k in contributors])
        filtered = [f for f, _ in contributors]

        bleed_through = tensorflow.add_n(filtered)

        corrected = tensorflow.subtract(source, bleed_through)
        return corrected, kernels

    def _serialize_to_tensors(self) -> None:
        raise NotImplementedError

    def _restore_from_tensors(
        self,
        restored_tensors: dict[str, tensorflow.Tensor],
    ) -> None:
        raise NotImplementedError
