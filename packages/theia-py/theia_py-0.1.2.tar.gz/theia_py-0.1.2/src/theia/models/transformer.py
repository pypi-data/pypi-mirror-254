"""Provides the `Transformer` for correcting bleedthrough images."""

import json
import pathlib

import numpy
import scipy.ndimage

__all__ = ["Transformer"]


class Transformer:
    """A thread-save transformer created from a trained Theia model.

    This is meant to only be created by Theia. It is used to correct bleedthrough
    images. It is thread-safe and can be used in a multi-threaded environment.
    """

    def __init__(
        self,
        *,
        num_channels: int,
        channel_overlap: int,
        beta: float,
        contribution_kernels: dict[tuple[int, int], numpy.ndarray],
        interactions_kernels: dict[tuple[int, int], numpy.ndarray],
    ) -> None:
        """Create a new Transformer.

        Args:
            num_channels: The number of channels in each image.
            channel_overlap: The number of adjacent channels to use for bleed-through
            estimation.
            beta: The beta parameter used for the interaction kernel.
            contribution_kernels: The fitted contribution kernels.
            interactions_kernels: The fitted interaction kernels.
        """
        self._num_channels = num_channels
        self._channel_overlap = channel_overlap
        self._beta = beta
        self._contribution_kernels = contribution_kernels
        self._interactions_kernels = interactions_kernels

    def save(self, json_path: pathlib.Path) -> None:
        """Save the Transformer to a json file.

        Args:
            json_path: The path to save the Transformer to.
        """
        params = {
            "num_channels": self._num_channels,
            "channel_overlap": self._channel_overlap,
            "beta": self._beta,
            "contribution_kernels": {
                f"{i}-{j}": self._kernel_to_list(v)
                for (i, j), v in self._contribution_kernels.items()
            },
            "interactions_kernels": {
                f"{i}-{j}": self._kernel_to_list(v)
                for (i, j), v in self._interactions_kernels.items()
            },
        }
        with json_path.open("w") as writer:
            json.dump(params, writer, indent=2)

    @staticmethod
    def _kernel_to_list(kernel: numpy.ndarray) -> list[float]:
        return list(map(float, kernel.flatten()))

    @staticmethod
    def load(json_path: pathlib.Path) -> "Transformer":
        """Load the Transformer from a saved json.

        Args:
            json_path: The path to load the Transformer from.
        """
        with json_path.open("r") as reader:
            params = json.load(reader)
        params["contribution_kernels"] = {
            tuple(map(int, k.split("-"))): Transformer._list_to_kernel(v)
            for k, v in params["contribution_kernels"].items()
        }
        params["interactions_kernels"] = {
            tuple(map(int, k.split("-"))): Transformer._list_to_kernel(v)
            for k, v in params["interactions_kernels"].items()
        }
        return Transformer(**params)

    @staticmethod
    def _list_to_kernel(kernel: list[float]) -> numpy.ndarray:
        h = int(numpy.sqrt(len(kernel)))
        kernel_array = numpy.asarray(kernel, numpy.float32)
        return numpy.reshape(kernel_array, newshape=(h, h))

    @property
    def num_channels(self) -> int:
        """The number of channels in each image."""
        return self._num_channels

    @property
    def channel_overlap(self) -> int:
        """The number of adjacent channels to use for bleed-through estimation."""
        return self._channel_overlap

    @property
    def contribution_kernels(self) -> dict[tuple[int, int], numpy.ndarray]:
        """Return the fitted contribution kernels.

        The keys are `(target, neighbor)` tuples, where `target` is the channel
        index of the target channel and `neighbor` is the channel index of the
        neighbor channel.

        The values are the fitted contribution kernels.
        """
        if len(self._contribution_kernels) == 0:
            message = "Please call `fit` before using this property."
            raise ValueError(message)
        return self._contribution_kernels

    @property
    def interaction_kernels(self) -> dict[tuple[int, int], numpy.ndarray]:
        """Return the fitted interaction kernels.

        The keys are `(target, neighbor)` tuples, where `target` is the channel
        index of the target channel and `neighbor` is the channel index of the
        neighbor channel.

        The values are the fitted contribution kernels.
        """
        if len(self._interactions_kernels) == 0:
            message = "Please call `fit` before using this property."
            raise ValueError(message)
        return self._interactions_kernels

    def bleedthrough_components(self, image: numpy.ndarray) -> numpy.ndarray:
        """Compute the channel-wise bleedthrough components for the image.

        Args:
            image: The image to compute the bleedthrough components for.

        Returns:
            The channel-wise bleedthrough components for the image.
        """
        bleedthrough = numpy.stack(
            [numpy.zeros_like(image) for _ in range(self.num_channels)],
            axis=-1,
        )

        for i_target in range(self.num_channels):
            neighbor_indices = self._neighbor_indices(i_target)

            neighbors = [image[:, :, i] for i in neighbor_indices]
            kernels = [
                self.contribution_kernels[(i_target, i)] for i in neighbor_indices
            ]

            bleedthrough[:, :, i_target, :] = self._compute_contributions(
                neighbor_indices,
                neighbors,
                kernels,
            )

        return bleedthrough

    def total_bleedthrough(self, image: numpy.ndarray) -> numpy.ndarray:
        """Compute the total bleedthrough components for the image.

        Args:
            image: The image to compute the bleedthrough components for.

        Returns:
            The total bleedthrough components for the image.
        """
        bleedthrough = self.bleedthrough_components(image)
        return numpy.sum(bleedthrough, axis=-1)

    def interactions_components(self, image: numpy.ndarray) -> numpy.ndarray:
        """Compute the interaction components for the image.

        Args:
            image: The image to compute the interaction components for.

        Returns:
            The interaction components for the image.
        """
        bleedthrough = numpy.stack(
            [numpy.zeros_like(image) for _ in range(self.num_channels)],
            axis=-1,
        )

        for i_target in range(self.num_channels):
            target = image[:, :, i_target]

            neighbor_indices = self._neighbor_indices(i_target)
            interactions = [
                self._compute_interaction(target, image[:, :, i])
                for i in neighbor_indices
            ]
            kernels = [
                self.interaction_kernels[(i_target, i)] for i in neighbor_indices
            ]

            bleedthrough[:, :, i_target, :] = self._compute_contributions(
                neighbor_indices,
                interactions,
                kernels,
            )

        return bleedthrough

    def total_interactions(self, image: numpy.ndarray) -> numpy.ndarray:
        """Compute the total interaction components for the image.

        Args:
            image: The image to compute the interaction components for.

        Returns:
            The total interaction components for the image.
        """
        interactions = self.interactions_components(image)
        return numpy.sum(interactions, axis=-1)

    def transform(
        self,
        image: numpy.ndarray,
        *,
        remove_interactions: bool = False,
    ) -> numpy.ndarray:
        """Transform the image by removing bleed-through and interactions.

        Args:
            image: The image to transform.
            remove_interactions: Whether to remove interactions between channels.

        Returns:
            The corrected image.
        """
        bleed_through = self.total_bleedthrough(image)

        if remove_interactions:
            bleed_through += self.total_interactions(image)

        return numpy.clip(image - bleed_through, a_min=0.0)

    def _neighbor_indices(self, i_target: int) -> list[int]:
        """Return the indices of the neighbors of the target channel."""
        min_i = max(i_target - self.channel_overlap, 0)
        max_i = min(i_target + self.channel_overlap, self.num_channels)
        return [i for i in range(min_i, max_i) if i != i_target]

    def _compute_interaction(
        self,
        target: numpy.ndarray,
        neighbor: numpy.ndarray,
    ) -> numpy.ndarray:
        """Compute the interaction between the target and neighbor channels.

        Args:
            target: The target channel.
            neighbor: The neighbor channel.

        Returns:
            The interaction between the target and neighbor channels.
        """
        interaction = numpy.power(neighbor, self._beta)
        interaction = numpy.multiply(target, interaction)
        interaction = numpy.power(interaction, 1 / (1 + self._beta))
        return interaction

    def _compute_contributions(
        self,
        indices: list[int],
        neighbors: list[numpy.ndarray],
        kernels: list[numpy.ndarray],
    ) -> numpy.ndarray:
        """Compute the contributions of the neighbors to the target channel.

        Args:
            indices: The indices of the neighbors.
            neighbors: The neighbor channels.
            kernels: The contribution kernels for the neighbors.

        Returns:
            The contributions of the neighbors to the target channel.
        """
        correlations = numpy.zeros(shape=(*neighbors[0].shape, self.num_channels))
        for i, n, k in zip(indices, neighbors, kernels):
            # noinspection PyUnresolvedReferences
            correlations[:, :, i] = scipy.ndimage.correlate(n, k)
        return correlations
