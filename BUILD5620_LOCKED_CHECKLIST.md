# BotX Pro V56.0.3 Build5620 — Locked Consolidated Checklist

Authority: signed Build5619 source. No older HTML/runtime or rejected migration may be restored.

1. Keep only Blue, Elite and Gold theme families, each Dark and Light (6 total).
2. Preserve Blue and Gold palettes; darken Elite Light green accent/text/button tokens for readability.
3. Remove the Terminal Hub bottom-right accidental glass flare without changing card geometry.
4. In paper/demo mode show `Paper mode`, not `BotX Demo` or `BotX Paper Broker`, in Terminal broker readout.
5. Keep Settings cardless: no enclosing plan/theme cards, no divider after every row, divider only between sections.
6. AI Help Desk must remain a flat row, not a separate card.
7. Restore broker/logo readability: slightly larger broker row logo and broker Settings icon without oversized cards.
8. Dashboard monitor must use one ledger: all currently open filled positions plus period-filtered closed trades; pending excluded; flat trades excluded from win-rate denominator.
9. Bot pair selection must show market icon, canonical symbol, proper name and category and provide search.
10. Preserve all existing bot/deploy/custom strategy/Kronos/TradingView/broker routes.
11. Add separate institutional configuration contracts for AI Institutional, HFT, DCA, Grid and Create My Own Bot.
12. Common risk gates: capital, <=2% risk/trade, max positions, daily loss, emergency drawdown, ATR stop, reward:risk, news filter, trailing exit and reject kill switch.
13. AI: confidence, correlation, confirmation-count and regime-confidence gates.
14. HFT: spread, slippage, ACK latency and order-rate gates; no AI in hot path.
15. DCA: averaging deviation, level cap, volume scale and step scale with cumulative exposure gate.
16. Grid: levels, spacing, range width and max inventory exposure with stop-outside-range gate.
17. Custom bot: minimum backtest days/trades, maximum drawdown, minimum profit factor and out-of-sample requirement.
18. Do not enable real-money execution; preserve ALLOW_LIVE_MODE=false.
19. Do not include signing keys, key.properties, caches or generated build folders in source delivery.
20. Final release only after format, analyze, full non-visual tests, signed APK, apksigner, archive integrity and checksum gates all pass.
