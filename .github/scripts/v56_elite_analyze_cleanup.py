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

shell = Path('lib/app/v56_native_shell.dart').read_text()
engine = Path('lib/app/local_demo_engine.dart').read_text()
assert 'String _brokerMark(' not in shell
assert 'double _riskFraction(' not in engine
print('Removed exactly two unused private helpers; no UI or trading behavior changed.')
