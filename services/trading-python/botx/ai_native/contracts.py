from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Literal

ModelClass = Literal["local_ml", "timeseries", "fast_llm", "reasoning_llm", "coding_llm"]

@dataclass(frozen=True)
class ModelRoute:
    model_id: str
    model_class: ModelClass
    reason: str
    estimated_cost_units: float = 0.0
    max_latency_ms: int = 0

@dataclass(frozen=True)
class StrategyResearchRequest:
    objective: str
    symbol: str
    timeframe_seconds: int
    max_candidates: int = 10
    allowed_regimes: tuple[str, ...] = ()
    context: dict[str, Any] = field(default_factory=dict)

@dataclass(frozen=True)
class StrategyGenome:
    strategy_id: str
    parent_id: str | None
    entry_genes: tuple[tuple[str, Any], ...]
    filter_genes: tuple[tuple[str, Any], ...]
    exit_genes: tuple[tuple[str, Any], ...]
    risk_genes: tuple[tuple[str, Any], ...]
    session_genes: tuple[str, ...] = ()
    regime_genes: tuple[str, ...] = ()

    def as_dict(self) -> dict[str, Any]:
        return {
            "strategy_id": self.strategy_id,
            "parent_id": self.parent_id,
            "entry_genes": dict(self.entry_genes),
            "filter_genes": dict(self.filter_genes),
            "exit_genes": dict(self.exit_genes),
            "risk_genes": dict(self.risk_genes),
            "session_genes": list(self.session_genes),
            "regime_genes": list(self.regime_genes),
        }
