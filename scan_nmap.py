#!/usr/bin/env python
import subprocess, configparser
try:
    config = configparser.ConfigParser()
    config.read("scan.ini")
    host = config["DEFAULT"]["host"]
    port = config["DEFAULT"]["port"]
    print host,port
    subprocess.call("nmap -sS %s -p-%s" % (host,port), shell=True)
    ans=raw_input("\nHit <enter> to exit")
except:
    pass
