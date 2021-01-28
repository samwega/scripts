#!/usr/bin/python3
# "r" (run) is a simple launcher, when added to path one can use "r [command line alias]" with dmenu or rofi and a command aliased will be launched. Edit terminal name to suit you.

from sys import argv, exit
import os

# User settings:
term = 'alacritty'
editor = 'kak'
# term = 'st'
# editor = 'vim'

# add/replace command-alias and text document to launch:
text_files = {
    'alacritty.yml': '~/.config/alacritty/alacritty.yml',
    'kakrc': '~/.config/kak/kakrc',
    'rc.lua': '~/.config/awesome/rc.lua',
    'theme.lua': '~/.config/awesome/themes/legio/theme.lua',
    'zshrc': '~/.zshrc',
    'r': '~/.local/bin/r',
}

# add/replace command-alias and console application to launch
terminal_application = {
    'news'  : 'newsboat -r',
    'ranger': 'ranger',
    'py'    : 'ipython --profile=samvega',
    'timer': 'python /home/samvega/.config/Timer/intervalTimer.py',
}

# argv[1] is the alias, given as the only argument to r, and equal to a key in one of the above dictionaries.
if argv[1] in text_files:
    os.system(f'exec {term} -e {editor} "{text_files[argv[1]]}"')
elif argv[1] in terminal_application:
    os.system(f'exec {term} -e {terminal_application[argv[1]]}')
# elif argv[1] == 's':
#     os.system(f'exec {term} -e elinks ddg:{argv[2:]}')
else:
    # if alias not in either dictionary, it is possible to launch any terminal command directly using 'r [args]'
    os.system(f'exec {term} -e {argv[1:]}')

