# BotX Pro Master V14 Android Build Trigger

This branch triggers the verified GitHub Actions build for technical version 15.0.7.

Expected gates:
- Download patched build input from the temporary Drive bridge
- Verify SHA-256 aa3e034d6199a15f021332e9adf6e8164a9cc37db8fb846b984c59f37d48678d
- Flutter 3.44.7 / Java 21
- flutter pub get
- flutter analyze --fatal-infos
- flutter test
- flutter build apk --debug
- package/version/signature verification
- APK artifact upload

Rerun after bounded Dart 3.12 compatibility and test-contract fixes.
