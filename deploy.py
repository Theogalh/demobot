#!/usr/bin/python
from subprocess import Popen

while True:
    print("\nStarting app.py")
    p = Popen("python " + "boy.py", shell=True)
    p.wait()
