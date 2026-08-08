from botx.ai_native.contracts import StrategyGenome
from botx.ai_native.genome import StrategyGenomeEngine
from botx.ai_native.promotion import PromotionEvidence, PromotionGate

def test_genome_mutation_is_bounded_and_has_parent():
    g = StrategyGenome("s1", None, (), (), (("stop_atr", 1.5),), (("risk_per_trade_pct", 0.5),))
    child = StrategyGenomeEngine().mutate(g, gene="stop_atr", value=2.0)
    assert child.parent_id == "s1"
    assert dict(child.exit_genes)["stop_atr"] == 2.0

def test_promotion_requires_all_gates_and_evidence():
    gate = PromotionGate()
    evidence = PromotionEvidence(True, True, True, True, True, ("bt-1", "wf-1"))
    assert gate.evaluate(evidence) == (True, ())
    assert gate.evaluate(PromotionEvidence(True, True, True, True, False, ("bt-1",)))[0] is False
