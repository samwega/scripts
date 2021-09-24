#!/usr/bin/python3
# Made by SamVega - https://samvega.netlify.app
# for DiscoverTaiji.com
# This file is copyright free (public domain).

import time
import os
from pygame import mixer
# figlet is required for rendering the fonts
# currently only works on Linux

mixer.init()
mixer.music.load(os.path.dirname(__file__) + '/garuda_bowl.wav')
os.system('echo Press ENTER to begin default 5 minute timer. Enter a number of minutes and press ENTER otherwise. Press Ctrl-c to quit.')

duration = input()  # press ENTER to begin, number to set interval minutes

def interval():

    # round = 300  # 300 seconds is 5 minutes
    round = 180
    if duration != '':
        round = int(duration) * 60
    else:
        pass

    mixer.music.play()
    start = 0
    while start < round:
        mins, secs = divmod(start, 60)
        timer = '{:02d} : {:02d}'.format(mins, secs)
        os.system('clear')
        print(f'🔔 Round: {total} ☯')
        # available fonts: big, digital, bubble, script, smscript, lean, mini, banner, slant, shadow, smshadow, block
        os.system(f'figlet -f big Discover')
        os.system(f'figlet -f big {timer}')
        os.system(f'figlet -f big Timer')
        time.sleep(1)
        start += 1


total = 0
beginning = round(time.time())

try:
    while True:
        total += 1
        interval()
except KeyboardInterrupt:
    totalTime = round(time.time()) - beginning
    mins, secs = divmod(totalTime, 60)
    timer = '{:02d}:{:02d}'.format(mins, secs)
    os.system(f'echo _Finished. Total time: {timer}')
    mixer.music.stop()
