#!/usr/bin/python

import time
import argparse
import os
import config
import progressbar

parser = argparse.ArgumentParser()
parser.add_argument("--time", help="minutes", type=int)
args = parser.parse_args()

timer = args.time
bar = progressbar.ProgressBar(maxval=timer, \
    widgets=[progressbar.Bar('#', '[', ']'), ' ', progressbar.Percentage()])
bar.start()
file = config.sound['file']

for i in range(1, timer+1):
    time.sleep(1)
    bar.update(i)

os.system("mpg123 " + file)
exit()
