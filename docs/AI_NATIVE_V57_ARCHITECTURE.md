# BOTX PRO — AI-NATIVE V57 FOUNDATION

## Status

This branch is an integration foundation only. It MUST NOT be treated as production-live trading certification.

## Baseline

Base branch: `codex/v56-0-3-kronos-edge-to-edge-20260729`

The public repository currently exposes a build/placeholder surface rather than the complete 1-August source package. Therefore this document defines the integration contracts without pretending that hidden production modules have been modified.

## Non-negotiable boundaries

1. V55/V56 UI remains locked.
2. Shared Risk Engine is authoritative.
3. Deterministic Execution Engine is the only component permitted to submit approved orders.
4. LLMs/agents/Kronos must never directly place broker orders.
5. Existing Kronos/offline ML models are preserved and accessed through adapters.
6. No broker secrets are exposed to models, prompts, agents, strategy code, logs, or mobile clients.
7. Vibe-Trading is an optional research capability/reference implementation, not a hard dependency.
8. Generated strategy code runs only inside an isolated research sandbox and cannot access broker credentials or live execution APIs.

## Target flow

```text
Market Data
   |
   +--> Offline ML / Kronos ----+
   |                            |
   +--> Regime Engine ----------+--> Model Router --> Neural Brain
   |                            |                       |
   +--> News / Macro -----------+                       v
   |                                           Strategy / Portfolio / Critic
   |                                                   |
   |                                                   v
   |                                             Shared Risk Engine
   |                                                   |
   |                                                   v
   |                                        Deterministic Execution
   |                                                   |
   +----------------------------------------------- Broker

Research path:

Research Request
  -> Vibe/Research Agent
  -> Strategy Specification
  -> Strategy Genome / Mutation
  -> Restricted Strategy DSL
  -> Backtest
  -> Walk Forward
  -> Monte Carlo / Cost Stress
  -> Critic
  -> Shadow
  -> Promotion Gate
  -> Strategy Registry
```

## Vibe Strategy Lab contract

The BotX-owned abstraction must support:

- research requests
- structured strategy specifications
- strategy genome representation
- controlled mutations
- code generation into a restricted strategy DSL
- static validation
- backtest orchestration
- walk-forward validation
- Monte Carlo stress tests
- realistic spread/commission/slippage assumptions
- regime analysis
- critic evaluation
- shadow deployment
- promotion/rollback

Generated code must not be allowed to import arbitrary networking, filesystem, subprocess, broker, credential, or execution APIs.

## Model Router contract

The router selects an already-registered model based on:

- task
- latency budget
- cost budget
- capability
- availability
- reliability

Preferred order:

1. deterministic logic
2. offline ML/Kronos
3. lightweight model
4. fast external model
5. strong reasoning model

A future Kronos Large release must be addable as a new registered model without changing downstream strategy/risk/execution contracts.

## Promotion gates

No model or strategy may become production-active solely because of backtest profit.

Required evidence should include, where applicable:

- out-of-sample performance
- walk-forward stability
- drawdown
- downside/ruin analysis
- cost sensitivity
- regime coverage
- prediction calibration
- execution quality
- shadow performance
- drift baseline

## Security architecture

Broker credentials belong in a dedicated secret-management boundary. AI components receive opaque account identifiers only. Execution services retrieve credentials through tightly scoped authorization.

Required controls include:

- least privilege
- tenant isolation
- short-lived application credentials/tokens where supported
- audit logs
- credential access logs
- withdrawal/fund-transfer permissions disabled where broker capabilities permit
- global/user/bot/model/strategy/broker kill switches
- replay protection and idempotency for critical requests

## Implementation phases

### Phase A — Research foundation
- Vibe abstraction
- strategy contracts
- strategy genome
- sandbox boundary
- promotion contract

### Phase B — Intelligence foundation
- model registry adapter
- model router
- regime engine adapter
- agent contracts

### Phase C — Evaluation loop
- backtest orchestration
- walk-forward
- Monte Carlo
- shadow comparison
- trade autopsy
- market memory
- drift

### Phase D — Advanced intelligence
- event intelligence graph
- time-series model adapters
- autonomous trading scientist
- digital twin
- MCP-safe tool layer

### Phase E — Production integration
- connect contracts to actual existing modules
- regression tests
- performance tests
- security tests
- staged deployment

## Important implementation rule

Do not create duplicate Risk, Execution, Backtest, Model Registry, or Strategy Registry implementations when an equivalent production subsystem exists. Integration must happen through adapters/interfaces after the actual source tree is available.
