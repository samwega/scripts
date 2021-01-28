#!/usr/bin/python3
# add to path to launch with rofi/dmenu
# mc - Saves and loads pieces of text to the clipboard.

# Usage: python mc s <keyword> - Saves clipboard to keyword.
#        python mc <keyword> - Loads keyword to clipboard.
#        python mc ls - Loads all keywords to clipboard.
#        python mc rm <keyword> - Removes keyword.
import shelve
import pyperclip
import sys

mcShelf = shelve.open('mcb')

# Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 's':
    mcShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'rm':
    del mcShelf[sys.argv[3]]
elif len(sys.argv) == 2:
    # List keywords and load content.
    if sys.argv[1].lower() == 'ls':
        pyperclip.copy(str(list(mcShelf.keys())))
    elif sys.argv[1] in mcShelf:
        pyperclip.copy(mcShelf[sys.argv[1]])

mcShelf.close()
