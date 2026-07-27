# BotX Pro V56 Elite Exact Source Lock

This branch must build only the latest Elite HTML-aligned native Flutter source.

- Public CI build-transfer ID: `1CpzzVCoTWhvo67LZ5fEty_UruvDzsy08`
- Exact source SHA-256: `d4f805b07b6cf8b683c788e7f0070865f7827de9e3745dbe41375ed3ccab3129`
- V56 Gold HTML authority SHA-256: `210647bdc447a55072fe16b6c7d348c7a316a0e0099c07c965f448dbf24112bd`
- App version: `56.0.0+5600`
- Android package: `pro.botx.app`
- Live mode: `ALLOW_LIVE_MODE=false`

## Mandatory latest UI markers

- Exact Elite palette (`#04130F`, `#0B241D`, `#46E6B0`, `#7CF5CE`)
- Flat Orders section without the rejected nested empty-state card
- Market chart opens only after tapping a pair
- New Bots UI and safe-area Start Bot placement
- Mandatory deployment configuration: currency pair, capital, risk, max positions, timeframe, direction and bot-specific controls
- Newly deployed bots append in creation order
- Settings contains App Sounds and Haptic Feedback
- Duplicate Settings Backtesting row is absent
- Offline deterministic broker/market identity rendering remains enabled

The GitHub Actions workflow downloads this exact SHA-locked latest source directly. It rejects the build if any mandatory marker is missing or if an old/rejected UI signature returns. The original locked 261 MB source archive and approved V56 HTML files remain untouched; only the CI build-transfer payload was advanced to this latest source.
