# BOTX Vibe Strategy Lab

This is the BotX-owned integration boundary for Vibe-Trading-style strategy research.

## Rule

This module is research-only. It must never have direct broker execution access.

## Pipeline

`research request -> strategy spec -> genome -> restricted DSL -> validation -> backtest -> walk-forward -> stress -> critic -> shadow -> promotion`

## Integration contract

The implementation must call existing BotX strategy/backtest/risk registries through adapters once the complete production source tree is available.

Do not duplicate an existing strategy compiler, backtester, model registry, risk engine, or execution engine.

## Sandbox requirements

Generated strategy artifacts must be treated as untrusted input. The eventual runtime must deny:

- network access
- broker APIs
- secret stores
- credential access
- arbitrary subprocess execution
- unrestricted filesystem access
- direct order placement

Only approved strategy primitives and explicitly provided market-data interfaces may be exposed.

## Future adapters

Potential research providers include HKUDS Vibe-Trading-style workflows, OpenAI/Codex, Claude, and future agent frameworks. Providers must implement the BotX abstraction rather than becoming hard dependencies of the trading core.
