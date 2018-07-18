#!/usr/bin/env python
import subprocess
file=open("command.txt")
subprocess.call(file.read(), shell=True)
ans=raw_input("\nHit <enter> to exit")
sys.exit()
