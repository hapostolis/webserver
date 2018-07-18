#!/usr/bin/env python
import socket, sys, os, time, subprocess, easygui
def main():
    try:
        if os.path.exists("scan.txt"):
            pass
        else:
            subprocess.call("./final.py", shell=True)
        file=open("scan.txt")
        host = file.readline()
        port = file.readline(5)
        os.system("clear")
        h = socket.gethostbyname(host)
        print("\033[92mtarget:\033[1m %s\033[0m" % h)
        print("\033[92mmax_port:\033[1m %s\033[0m" % port)
        t1 = time.time()
        print("\033[91mStarting at %s\n " % time.strftime("%Y-%m-%d %H:%M:%S\033[0m", time.gmtime()))
        for i in range(1, int(port)):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #        s.settimeout(10)
            a = s.connect_ex((host, i))
            if a == 0:
                print("\033[93m[==>]\033[0m \033[96mFount open port\033[0m    \033[1m%d\033[0m" % i)
            s.close()
        print("\n\033[91mStopped at %s\n " % time.strftime("%Y-%m-%d %H:%M:%S\033[0m", time.gmtime()))
        t2 = time.time()
        #print("\033[0mFinished in %s seconds\n\033[0m" % float(t2-t1))
        raw_input("\nHit <enter> to exit")
        sys.exit()
    except KeyboardInterrupt:
        print("User canceled!\n[*] Abord..")
        sys.exit()
    except Exception, e:
        easygui.msgbox(msg=e, title="Exception!")
main()
