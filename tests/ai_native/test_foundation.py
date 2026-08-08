from __future__ import annotations

import asyncio
from botx.ai_native.contracts import StrategyResearchRequest
from botx.ai_native.model_router import ModelCapability, ModelRouter
from botx.ai_native.vibe_lab import VibeStrategyLab

class StubProvider:
    async def generate_candidates(self, request):
        return [{
            "schema_version": "1.2",
            "version": "vibe-1",
            "universe": {"symbols": [request.symbol], "timeframes": ["5m"]},
            "entry": {"logic": "ALL", "direction": "BUY", "rules": [
                {"feature": "rsi", "indicator": "RSI", "operator": "LT", "value": 30, "timeframe": "5m"}
            ]},
            "filters": [],
            "risk": {"risk_per_trade_pct": 0.5, "max_positions": 1},
            "exit": {"type": "ATR", "stop_atr": 1.5, "take_atr": 3.0},
        }]

def test_model_router_prefers_cheapest_healthy_model():
    router = ModelRouter([
        ModelCapability("kronos-base", "timeseries", frozenset({"forecast"}), cost_units=0, latency_ms=40),
        ModelCapability("expensive-ts", "timeseries", frozenset({"forecast"}), cost_units=10, latency_ms=20),
    ])
    assert router.route("forecast").model_id == "kronos-base"

def test_vibe_candidate_is_compiled_not_executed():
    request = StrategyResearchRequest("discover", "XAUUSD", 300)
    candidates = asyncio.run(VibeStrategyLab(StubProvider()).research(request))
    assert len(candidates) == 1
    assert candidates[0].candidate_id.startswith("vibe-")
    assert candidates[0].artifact_hash
