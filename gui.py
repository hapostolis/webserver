import os, socket, time, subprocess
from Tkinter import *
def more():
    def r():
        more.destroy()
    def ex():
        more.destroy()
        server.destroy()
    def rer():
        more.destroy()
        server.destroy()
        subprocess.call("python gui.py", shell=True)
    more=Tk()
    more.title("More options")
    more.geometry("250x250+550+50")
    a=Button(more, text="Go back", command=r)
    a.pack(fill=BOTH, expand=1)
    b=Button(more, text="Exit", command=ex)
    b.pack(fill=BOTH, expand=1)
    c=Button(more, text="Re-run window", command=rer)
    c.pack(fill=BOTH, expand=1)
server = Tk()
server.geometry("1200x700")
server.title("Web[server/client]")
termf = Frame(server, height=250, width=400)
termf.pack(fill=BOTH, expand=1, side=LEFT)
wid = termf.winfo_id()

os.system("xterm -into %d -sb -leftbar -geometry 100x54 -e ./server.py &" % wid)
#os.system("xterm -into %d -sb -geometry 100x54 &" % wid)
termf2 = Frame(server, height=250, width=300)
termf2.pack(fill=BOTH, expand=1, side=RIGHT)
wid2 = termf2.winfo_id()

os.system("xterm -into %d -sb -leftbar -geometry 100x54 -e ./client.py &" % wid2)
#os.system("xterm -into %d -sb -geometry 100x54 &" % wid2)
b = Button(server, text="Options", command=more)
b.place(x=640,y=0)
server.mainloop()
#http://effbot.org/tkinterbook/menubutton.htm
