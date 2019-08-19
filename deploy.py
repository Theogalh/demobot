#!/usr/bin/python
from subprocess import Popen

while True:
    print("\nStarting app.py")
    p = Popen("python " + "bot.py", shell=True)
    p.wait()
