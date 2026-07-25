# BotX Pro Master V14 Android Build Trigger

This branch triggers the verified GitHub Actions build for technical version 15.0.7.

Expected gates:
- Download build input from the temporary Drive bridge
- Verify SHA-256 511bb612a157cdf03cf73d093dd158603b2d15dde16c2dad361ae3f96f3502a7
- Flutter 3.44.7 / Java 21
- flutter pub get
- flutter analyze --fatal-infos
- flutter test
- flutter build apk --debug
- package/version/signature verification
- APK artifact upload

Diagnostic rerun: capture analyzer, test, and build logs while preserving final gate enforcement.
