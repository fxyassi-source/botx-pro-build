from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from typing import Any, Protocol

from botx.custom.compiler import CompiledStrategy, StrategyCompiler
from botx.custom.schema import StrategyValidationError
from .contracts import StrategyResearchRequest

class StrategyResearchProvider(Protocol):
    async def generate_candidates(self, request: StrategyResearchRequest) -> list[dict[str, Any]]:
        ...

@dataclass(frozen=True)
class StrategyCandidate:
    candidate_id: str
    compiled: CompiledStrategy
    source: str
    artifact_hash: str
    warnings: tuple[str, ...]

class VibeStrategyLab:
    """Safe Vibe-style research boundary.

    Generated code/specs are untrusted. Only structured strategy specs accepted
    by BOTX's deterministic compiler become candidates. No broker or live
    execution dependency is exposed here.
    """

    def __init__(self, provider: StrategyResearchProvider | None = None) -> None:
        self.provider = provider
        self.compiler = StrategyCompiler()

    async def research(self, request: StrategyResearchRequest) -> list[StrategyCandidate]:
        if self.provider is None:
            raise RuntimeError("VIBE_PROVIDER_NOT_CONFIGURED")
        if not 1 <= request.max_candidates <= 100:
            raise ValueError("MAX_CANDIDATES_OUT_OF_RANGE")
        raw_candidates = await self.provider.generate_candidates(request)
        return [
            self.validate_candidate(spec, request, source=f"vibe:{index}")
            for index, spec in enumerate(raw_candidates[: request.max_candidates])
        ]

    def validate_candidate(
        self,
        spec: dict[str, Any],
        request: StrategyResearchRequest,
        *,
        source: str,
    ) -> StrategyCandidate:
        try:
            compiled = self.compiler.compile(
                json.loads(json.dumps(spec)),
                symbol=request.symbol,
                timeframe_seconds=request.timeframe_seconds,
            )
        except (StrategyValidationError, ValueError, TypeError) as exc:
            raise StrategyValidationError(f"VIBE_CANDIDATE_REJECTED:{exc}") from exc
        canonical = json.dumps(spec, sort_keys=True, separators=(",", ":"), default=str).encode()
        artifact_hash = hashlib.sha256(canonical).hexdigest()
        return StrategyCandidate(
            candidate_id=f"vibe-{artifact_hash[:16]}",
            compiled=compiled,
            source=source,
            artifact_hash=artifact_hash,
            warnings=compiled.warnings,
        )
