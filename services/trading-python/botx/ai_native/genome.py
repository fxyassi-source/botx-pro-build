from __future__ import annotations

from dataclasses import replace
from hashlib import sha256
import json
from typing import Any
from .contracts import StrategyGenome

class StrategyGenomeEngine:
    """Deterministic, bounded strategy mutations for research only."""

    def mutate(self, genome: StrategyGenome, *, gene: str, value: Any) -> StrategyGenome:
        if gene == "risk_per_trade_pct":
            if not 0.05 <= float(value) <= 2.0:
                raise ValueError("RISK_GENE_OUT_OF_RANGE")
            risk = dict(genome.risk_genes)
            risk[gene] = float(value)
            return replace(genome, parent_id=genome.strategy_id, risk_genes=tuple(sorted(risk.items())))
        if gene == "stop_atr":
            if not 0.1 <= float(value) <= 10:
                raise ValueError("STOP_ATR_OUT_OF_RANGE")
            exits = dict(genome.exit_genes)
            exits[gene] = float(value)
            return replace(genome, parent_id=genome.strategy_id, exit_genes=tuple(sorted(exits.items())))
        raise ValueError(f"UNSUPPORTED_GENE:{gene}")

    @staticmethod
    def fingerprint(genome: StrategyGenome) -> str:
        payload = json.dumps(genome.as_dict(), sort_keys=True, separators=(",", ":"), default=str)
        return sha256(payload.encode()).hexdigest()
