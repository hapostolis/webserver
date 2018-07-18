#!/usr/bin/env python
import os, subprocess, easygui
from Tkinter import *
def main():
    def scanexit():
        root.destroy()
    def scan_local():
        host = x1.get()
        port = int(x2.get())
        if port > 65535:
            easygui.msgbox(msg="Max port is 65535", title="Attention!")
            scan.destroy()
            main()
        else:
            pass
        if port < 65535:
            port = port + 1
        else:
            port = port
        #if port == 65535:
        #    port = port - 1
        file=open("scan.txt", "w")
        file.write("%s\n%d" % (host,port))
        file.close()
        subprocess.call("xterm -e ./scan.py", shell=True)
    def r():
        command = nmape.get()
        if 'nmap' in command:
            file=open("command.txt", "w")
            file.write(command)
            file.close()
            a=subprocess.check_output("xterm -e ./command.py", shell=True)
    def exit():
        scan.destroy()
    def scan_more():
        txt="You can scan a host for open ports using 2 tools.\n1. Nmap\n2. Local port scanner using python module 'socket'==> it may show false reports"
        easygui.msgbox(msg=txt, title="More ..")
    def scan_nmap():
        host = x1.get()
        port = int(x2.get())
        file=open("scan.ini", "w")
        file.write("[DEFAULT]\nhost: %s\nport: %d" % (host,port))
        file.close()
        subprocess.call("xterm -e ./scan_nmap.py", shell=True)
    root=Tk()
    root.geometry("550x250+300+100")
    root.resizable(width=False, height=False)
    root.title("Scan Alive hosts for open ports")
    l1=Label(root,text="Ip address of host:")
    l1.place(x=0,y=20)
    x1=Entry(root,width=12)
    x1.place(x=130,y=20)
    l2=Label(root,text="Max port to scan:")
    x2=Entry(root,width=5)
    l3=Label(root,text="Max. 65535")
    l2.place(x=0,y=60)
    x2.place(x=130,y=60)
    l3.place(x=190,y=60)
    menubar = Menu(root)
    start = Menu(menubar, tearoff=0)
    start.add_separator()
    start.add_command(label="Scan using project's local tool", command=scan_local)
    start.add_separator()
    start.add_command(label="Scan using nmap", command=scan_nmap)
    start.add_separator()
    menubar.add_cascade(label="Start", menu=start)
    more = Menu(menubar, tearoff=0)
    more.add_command(label="More about tools ...", command=scan_more)
    menubar.add_cascade(label="More", menu=more)
    quit = Menu(menubar, tearoff=0)
    quit.add_command(label="Exit scan window", command=scanexit)
    menubar.add_cascade(label="QUIT", menu=quit)
    nmapl=Label(root,text="Run your own shell command based on nmap(only) tool:")
    nmapl.place(x=0,y=150)
    nmape=Entry(root,width=50)
    nmape.place(x=0,y=180)
    nmapb=Button(root,text="Run", command=r)
    nmapb.place(x=0,y=210)
    root.config(menu=menubar)
    root.mainloop()
main()
