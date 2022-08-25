import os
import platform
from rich import print as richPrinter
from pathlib import Path

def clearScreen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
def richPrint(auto):
    return richPrinter(auto)

def rootProject() -> Path:
    return str(Path(__file__).parent.parent)