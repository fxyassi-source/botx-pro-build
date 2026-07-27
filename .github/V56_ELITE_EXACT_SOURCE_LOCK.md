# BotX Pro V56 Elite Exact Source Lock

This branch builds only the latest Elite HTML-aligned native Flutter source.

- Public CI build-transfer ID: `1CpzzVCoTWhvo67LZ5fEty_UruvDzsy08`
- Exact input SHA-256: `d4f805b07b6cf8b683c788e7f0070865f7827de9e3745dbe41375ed3ccab3129`
- V56 Gold HTML authority SHA-256: `210647bdc447a55072fe16b6c7d348c7a316a0e0099c07c965f448dbf24112bd`
- App version: `56.0.0+5600`
- Android package: `pro.botx.app`
- Live mode: `ALLOW_LIVE_MODE=false`
- Successful workflow run: `30233045503`
- Successful build commit: `e297c071da85c22bc7e4dba73bcc1e1b9b20ea1d`

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
- Isolated TradingView chart fails safely to the existing fallback when a platform WebView is unavailable

## Successful release gates

- Exact source SHA verified
- Old/rejected UI fallback guard passed
- Strict Flutter analyze passed with no issues
- Eleven isolated V56 UI tests passed
- Four bot lifecycle/deployment tests passed
- Market identity and chart-contract tests passed
- Seven screenshots generated
- Signed ARM64 APK and Android App Bundle built
- APK signature and secret-pattern checks passed

The original locked 261 MB source archive and approved V56 HTML files remain untouched. This draft branch/PR is a build and review vehicle and must not be merged blindly.
