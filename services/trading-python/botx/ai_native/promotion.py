from __future__ import annotations

from dataclasses import dataclass

@dataclass(frozen=True)
class PromotionEvidence:
    backtest_passed: bool
    walk_forward_passed: bool
    stress_passed: bool
    shadow_passed: bool
    risk_approved: bool
    evidence_ids: tuple[str, ...] = ()

class PromotionGate:
    """Conservative research-to-production gate; never places orders."""

    REQUIRED = ("backtest_passed", "walk_forward_passed", "stress_passed", "shadow_passed", "risk_approved")

    def evaluate(self, evidence: PromotionEvidence) -> tuple[bool, tuple[str, ...]]:
        failed = tuple(name for name in self.REQUIRED if not getattr(evidence, name))
        if failed:
            return False, failed
        if not evidence.evidence_ids:
            return False, ("evidence_ids_required",)
        return True, ()
