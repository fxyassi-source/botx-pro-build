"""AI-native research layer for BOTX PRO.

This package is deliberately isolated from live execution. AI-generated strategy
artifacts must pass the existing deterministic strategy compiler and downstream
validation before they can enter paper/shadow promotion workflows.
"""

from .contracts import ModelRoute, StrategyGenome, StrategyResearchRequest
from .model_router import ModelRouter
from .vibe_lab import VibeStrategyLab

__all__ = ["ModelRoute", "ModelRouter", "StrategyGenome", "StrategyResearchRequest", "VibeStrategyLab"]
