import os
import platform
from rich import print
from pathlib import Path


def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def rich_print(auto):
    print(auto)


def root_project() -> Path:
    return Path.cwd()

