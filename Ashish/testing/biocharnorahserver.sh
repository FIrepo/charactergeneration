#!/bin/bash
pidof Xorg || sudo Xorg &
sudo DISPLAY=:0 python2 ~/makehuman/makehuman/makehuman.py --headless --runserver $@ >/dev/null 2>&1
echo Done