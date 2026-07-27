from pathlib import Path

replacements = {
    Path('lib/app/local_demo_engine.dart'): """  double _riskFraction(String type) {\n    final normalized = type.toLowerCase();\n    if (normalized.contains('hft')) return 0.0015;\n    if (normalized.contains('grid')) return 0.002;\n    if (normalized.contains('dca')) return 0.0025;\n    return 0.002;\n  }\n\n""",
    Path('lib/app/v56_native_shell.dart'): """String _brokerMark(String name) {\n  final words = name\n      .replaceAll('_', ' ')\n      .split(RegExp(r'\\s+'))\n      .where((value) => value.isNotEmpty)\n      .toList();\n  if (words.isEmpty) {\n    return 'BX';\n  }\n  if (words.length == 1) {\n    return words.first\n        .substring(0, math.min(2, words.first.length))\n        .toUpperCase();\n  }\n  return '${words.first[0]}${words[1][0]}'.toUpperCase();\n}\n\n""",
}

for path, block in replacements.items():
    text = path.read_text()
    if block not in text:
        raise SystemExit(f'Expected cleanup block not found: {path}')
    path.write_text(text.replace(block, '', 1))

# A separate, actively used broker-logo helper has the same private name.
# Rename it only to keep the release guard precise; behavior is unchanged.
identity_path = Path('lib/app/market_identity_logo.dart')
identity = identity_path.read_text()
rename_count = identity.count('_brokerMark(')
if rename_count < 2:
    raise SystemExit('Expected active market broker-mark helper/calls not found')
identity_path.write_text(identity.replace('_brokerMark(', '_marketBrokerMark('))

# Align the inherited market smoke test with the founder-approved tap-only chart flow.
test_path = Path('test/v56_ui_smoke_test.dart')
test_text = test_path.read_text()
old_market_test = """  testWidgets('Market keeps the XM-sized chart surface', (tester) async {\n    await pumpGuestShell(tester, size: const Size(390, 844));\n    await tester.tap(find.byKey(const ValueKey('v56_nav_market')));\n    await tester.pump(const Duration(milliseconds: 250));\n\n    final chart = find.byKey(const ValueKey('v56_market_chart'));\n    expect(chart, findsOneWidget);\n    expect(tester.getSize(chart).height, 300);\n    expect(find.text('Trend'), findsOneWidget);\n    expect(find.text('Volatility'), findsOneWidget);\n    expect(find.text('Regime'), findsWidgets);\n  });\n"""
new_market_test = """  testWidgets(\n    'Market keeps the XM-sized chart surface closed until a pair is tapped',\n    (tester) async {\n      await pumpGuestShell(tester, size: const Size(390, 844));\n      await tester.tap(find.byKey(const ValueKey('v56_nav_market')));\n      await tester.pump(const Duration(milliseconds: 250));\n\n      expect(find.byKey(const ValueKey('v56_market_chart')), findsNothing);\n      expect(\n        find.byKey(const ValueKey('v56_market_pair_EURUSD')),\n        findsOneWidget,\n      );\n      expect(\n        find.text('Tap a market pair to open its chart and AI analysis.'),\n        findsOneWidget,\n      );\n    },\n  );\n"""
if old_market_test not in test_text:
    raise SystemExit('Expected inherited market smoke test block not found')
test_text = test_text.replace(old_market_test, new_market_test, 1)
old_chart_open = """    expect(find.byKey(const ValueKey('v56_market_chart')), findsNothing);\n    await tester.tap(find.byKey(const ValueKey('v56_market_pair_EURUSD')));\n    await tester.pump(const Duration(milliseconds: 250));\n    await tester.tap(find.byKey(const ValueKey('v56_market_chart')));\n"""
new_chart_open = """    expect(find.byKey(const ValueKey('v56_market_chart')), findsNothing);\n    await tester.tap(find.byKey(const ValueKey('v56_market_pair_EURUSD')));\n    await tester.pump(const Duration(milliseconds: 250));\n    final chart = find.byKey(const ValueKey('v56_market_chart'));\n    expect(chart, findsOneWidget);\n    expect(tester.getSize(chart).height, 300);\n    await tester.tap(chart);\n"""
if old_chart_open not in test_text:
    raise SystemExit('Expected TradingView market test sequence not found')
test_path.write_text(test_text.replace(old_chart_open, new_chart_open, 1))

shell = Path('lib/app/v56_native_shell.dart').read_text()
engine = Path('lib/app/local_demo_engine.dart').read_text()
identity = identity_path.read_text()
updated_tests = test_path.read_text()
assert 'String _brokerMark(' not in shell
assert 'double _riskFraction(' not in engine
assert '_brokerMark(' not in identity
assert '_marketBrokerMark(' in identity
assert 'Market keeps the XM-sized chart surface closed until a pair is tapped' in updated_tests
assert "testWidgets('Market keeps the XM-sized chart surface'," not in updated_tests
print('Applied exact analyze cleanup and tap-only market test alignment; app UI behavior unchanged.')
