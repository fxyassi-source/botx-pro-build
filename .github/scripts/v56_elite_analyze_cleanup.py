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

shell = Path('lib/app/v56_native_shell.dart').read_text()
engine = Path('lib/app/local_demo_engine.dart').read_text()
identity = identity_path.read_text()
assert 'String _brokerMark(' not in shell
assert 'double _riskFraction(' not in engine
assert '_brokerMark(' not in identity
assert '_marketBrokerMark(' in identity
print('Removed exactly two unused helpers and renamed one active private logo helper; behavior unchanged.')
