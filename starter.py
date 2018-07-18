#!/usr/bin/env python
import sys, subprocess, socket, os, easygui, threading, time, base64, configparser
from Tkinter import *
def ifconfigg():
    if sys.platform == "win32":
        a = subprocess.check_output("ipconfig /all",stderr=subprocess.STDOUT, shell=True)
    else:
        a = subprocess.check_output("ifconfig",stderr=subprocess.STDOUT, shell=True)
    easygui.codebox(msg="Ifconfig information", title="IFCONFIG/IPCONFIG", text=a)
def main():
    def exit():
        sys.exit()
    def scann():
        subprocess.call("python scangui.py", shell=True)
    def startup():
        try:
            server = t1.get()
            sport = int(t2.get())
            client = t3.get()
            cport = int(t4.get())
            name = l5.get()
            file=open("details.ini","w")
            file.write("[DEFAULT]\nserver: %s\nsport: %d\nclient: %s\ncport: %d\nname: %s" % (server,sport,client,cport,name))
            file.close()
            if len(server) > 0 and len(client) > 0:
                go1 = "yes"
            else:
                easygui.msgbox(msg="I need a server and client")
            if len(name) > 1:
                go2 = "yes"
            else:
                easygui.msgbox(msg="Please enter a name")
            if sport and cport > 0 and sport and cport < 65535:
                pass
            else:
                easygui.msgbox(msg="Ports should be between 1-65535")
            if go1 and go2 == "yes":
                subprocess.call("python gui.py", shell=True)
        except ValueError:
            easygui.msgbox(msg="You missed an entry or port is not number")
    def ready():
            subprocess.call("python gui.py", shell=True)
    root = Tk()
    root.geometry("800x600+300+90")
    root.title("Server-Client Tool - " + time.strftime("%x %H:%M"))
    a = Label(root,text="Server startup")
    a.place(x=250,y=25)
    a2=Label(root,text="Start server on:")
    a2.place(x=0, y=45)
    l1 = Label(root,text="Host:")
    l1.place(x=20,y=80)
    t1 = Entry(root, width=15)
    t1.place(x=230,y=80)
    l2 = Label(root,text="Port:")
    l2.place(x=20,y=110)
    t2 = Entry(root, width=6)
    t2.place(x=230,y=110)
    b = Label(root,text="Client connect")
    b.place(x=250,y=180)
    l3 = Label(root,text="connect to:")
    l3.place(x=20, y=220)
    t3 = Entry(root, width=15)
    t3.place(x=190, y=220)
    l4 = Label(root,text="on Port:")
    l4.place(x=20, y=260)
    t4 = Entry(root, width=6)
    t4.place(x=190, y=260)
    t5 = Label(root,text="Name for the chat:")
    t5.place(x=20,y=300)
    l5 = Entry(root,width=15)
    l5.place(x=190,y=300)
    t6 = Label(root,text="Ipv4 or Ipv6 [4/6]")
    t6.place(x=20,y=340)
    l6 = Entry(root,width=1)
    l6.place(x=190, y=340)
    menubar = Menu(root)
    start = Menu(menubar, tearoff=0)
    start.add_command(label="Start server and client", command=startup)
    menubar.add_cascade(label="Start", menu=start)
    scan = Menu(menubar, tearoff=0)
    scan.add_command(label="Scan a host for open ports", command=scann)
    menubar.add_cascade(label="Scan", menu=scan)
    ifconfig = Menu(menubar, tearoff=0)
    ifconfig.add_command(label="Show ifconfig information", command=ifconfigg)
    menubar.add_cascade(label="Ifconfig", menu=ifconfig)
    pref = Menu(menubar, tearoff=0)
    pref.add_command(label="change your Preferences")
    menubar.add_cascade(label="Preferences", menu=pref)
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="More details...")#!!!!
    menubar.add_cascade(label="Help", menu=helpmenu)
    exit = Menu(menubar, tearoff=0)
    exit.add_command(label="Exit the tool", command=root.quit)
    menubar.add_cascade(label="QUIT", menu=exit)
    root.config(menu=menubar)
    root.mainloop()
main()
