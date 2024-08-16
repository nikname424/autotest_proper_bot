# Установка библиотек, используемых в коде
import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Список библиотек для установки
libraries = [
    "selenium"
]

# Установка библиотек
for lib in libraries:
    install(lib)
