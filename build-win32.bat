pyinstaller --onefile .\main.py --add-data "assets/*;assets/" --add-data "dependencies/win32/*;dependencies/win32/" --add-data "dependencies/bin/*;dependencies/win32/bin/"  --name="Mario Party Toolkit" -w --icon="assets/icons/diceBlock.ico"
