import torch
from typing import Generic, TypeVar, Dict, Any

from torch import Tensor

StateDict = Dict[str, Any]
T = TypeVar("T", bound=torch.nn.Module, covariant=True)


class ModelDescriptor(Generic[T]):
    def __init__(
            self,
            model: T,
            state_dict: StateDict,
            architecture: str,
            scale: int,
            input_channels: int,
            output_channels: int
    ):
        self.model: T = model

        self.architecture = architecture
        self.scale = scale
        self.input_channels = input_channels
        self.output_channels = output_channels

        self.model.load_state_dict(state_dict)

    def to(self, device: torch.device):
        self.model.to(device)
        return self

    def eval(self):
        self.model.eval()
        return self

    def train(self, mode: bool = True):
        self.model.train(mode)
        return self

    def __call__(self, image: Tensor) -> Tensor:
        output = self.model(image)
        assert isinstance(
            output, Tensor
        ), f"Expected {type(self.model).__name__} model to returns a tensor, but got {type(output)}"
        return output
