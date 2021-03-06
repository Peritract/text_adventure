"""Functions that deal with displaying information on the console."""

import os
import sys
from time import sleep


def display(message, delay=0.05):
    """Displays text as though it was being written."""
    for char in message + "\n":
        sys.stdout.write(char)
        sys.stdout.flush()
        sleep(delay)


def clear_screen():
    """Clears the console window."""
    if sys.platform == 'win32':
        os.system('cls')
    else:
        os.system('clear')
