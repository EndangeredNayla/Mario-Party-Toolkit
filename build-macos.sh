pyinstaller --onefile main.py --add-data "assets/*:assets/" --name="Mario Party Toolkit" --noconsole  --icon="assets/diceBlock.ico" --distpath="dist/arm64" --target-arch universal2
