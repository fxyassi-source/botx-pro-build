from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

from .contracts import ModelClass, ModelRoute

@dataclass(frozen=True)
class ModelCapability:
    model_id: str
    model_class: ModelClass
    capabilities: frozenset[str]
    healthy: bool = True
    cost_units: float = 0.0
    latency_ms: int = 0
    priority: int = 100

class ModelRouter:
    """Deterministic routing policy; it never performs inference itself."""

    def __init__(self, capabilities: Iterable[ModelCapability] = ()) -> None:
        self._capabilities = list(capabilities)

    def register(self, capability: ModelCapability) -> None:
        self._capabilities = [c for c in self._capabilities if c.model_id != capability.model_id]
        self._capabilities.append(capability)

    def route(self, task: str, *, max_latency_ms: int | None = None) -> ModelRoute:
        candidates = [c for c in self._capabilities if c.healthy and task in c.capabilities]
        if max_latency_ms is not None:
            candidates = [c for c in candidates if c.latency_ms <= max_latency_ms]
        if not candidates:
            raise LookupError(f"NO_MODEL_ROUTE:{task}")
        selected = min(candidates, key=lambda c: (c.cost_units, c.latency_ms, c.priority))
        return ModelRoute(
            model_id=selected.model_id,
            model_class=selected.model_class,
            reason=f"capability={task};cost={selected.cost_units};latency={selected.latency_ms}ms",
            estimated_cost_units=selected.cost_units,
            max_latency_ms=selected.latency_ms,
        )
