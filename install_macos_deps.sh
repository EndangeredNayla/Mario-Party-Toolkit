arch -arm64 brew install python@3.12 python-tk@3.12
arch -x86_64 brew install python@3.12 python-tk@3.12

arch -arm64 /opt/homebrew/Cellar/python@3.12/3.12.1/bin/pip3.12 install -r requirements.txt --break-system-packages
arch -x86_64 /usr/local/Cellar/python@3.11/3.12.1/bin/pip3.12 install -r requirements.txt --break-system-packages
