pyinstaller --onefile .\main.py --add-data "assets/*;assets/" --add-data "dependencies/CTkColorPicker/*;CTkColorPicker/" --add-data "dependencies/win32/*;dependencies/" --add-data "dependencies/bin/*;dependencies/bin/" --name="Mario Party Toolkit" -w --icon="assets/diceBlock.ico"
