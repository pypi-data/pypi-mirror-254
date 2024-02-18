from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Dict

from ..utilities.canonicalize import canonicalize_state_dict
from .model_descriptor import ModelDescriptor, StateDict


class UnsupportedModelError(Exception):
    pass


@dataclass(frozen=True)
class ArchSupport:
    id: str
    keys: list[str]
    load: Callable[[StateDict], ModelDescriptor]


class ArchRegistry:
    def __init__(self):
        self._architectures: Dict[str, ArchSupport] = {}

    def __contains__(self, id: str) -> bool:
        return id in self._architectures

    def __getitem__(self, id: str) -> ArchSupport:
        return self._architectures[id]

    def get(self, id: str) -> ArchSupport | None:
        return self._architectures.get(id, None)

    def load(self, state_dict: StateDict) -> ModelDescriptor:
        state_dict = canonicalize_state_dict(state_dict)

        for id in self._architectures:
            arch = self._architectures[id]
            if all(key in state_dict for key in arch.keys):
                return arch.load(state_dict)

        raise UnsupportedModelError

    def add(self, *architectures: ArchSupport):
        for arch in architectures:
            self._architectures[arch.id] = arch
