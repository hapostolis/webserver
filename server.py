#!/usr/bin/env python
import os, sys, socket, threading, subprocess, easygui, configparser, time
shell = 0
file = open("shell_check.txt", "w")
file.write("no")
file.close()
if os.path.exists("details.ini"):
    pass
else:
    subprocess.call("./starter.py", shell=True)
config = configparser.ConfigParser()
config.read("details.ini")
host = config["DEFAULT"]["server"]
port  = config["DEFAULT"]["sport"]
def server():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((host,int(port)))
        s.listen(5)
        os.system("clear")
        print "Listening for upcoming messages on %s:%d" % (host,int(port))
        def res(client):
            global shell
            r = client.recv(4098)
            try:
                l = subprocess.check_output(r,stderr=subprocess.STDOUT, shell=True)
            except:
                l = "Failed to execute the command [\033[91m%s\033[0m]" % r
            if len(r) == 0:
                print("Host closed the connection")
                shell=0
            if "shell=open code=3024" in r and shell==0:
                print("\nConnected host in trying to get shell access")
                ans=raw_input("Give access to shell on connected host?[y/n]: ")
                if ans=="y":
                    inp = os.getcwd()
                    client.send("shell=open -yes")
                    shell = 1
                else:
                    shell = 0
                    client.send("Permission denied!")
            if "shell=open code=3024" in r and shell==1:
                client.send("Shell is already opened!")
            #if "shell=open ask=no pass=a2542002" in r:
            #    shell=1
            #    client.send("noask")
            if shell == 1 and "shell=exit" in r:
                shell = 0
                print("\033[91mShell closed\033[0m")
            if shell == 1 and "print cwd" in r:
                j = os.getcwd()
                print j
                client.send(j)
            if shell == 1 and "ls" in r:
                r = r + ' ' + os.getcwd()
            if shell == 1:
                if not "shell=open code=3024" in l:
                    client.send(l + '\n\033[0m.....................')
            if shell == 1 and "cd " in r:
                os.chdir(r[3:])
                print r + " [%s]" % os.getcwd()
            print r
            if shell == 1:
                time.sleep(3)
                file = open("shell_check.txt", "r")
                fi = file.read()
                if "yes" in fi:
                    shell = 0
                    client.send("shell=closed")
                file.close()
            #else:
                #print r
            file=open("server_log.txt", "a")
            file.write('\n' + r)
            file.close()
            client.close()
        while True:
            client,addr = s.accept()
            a = threading.Thread(target=res, args=(client,))
            a.start()
    except KeyboardInterrupt:
        s.close()
        sys.exit()
    except Exception, e:
        print e
        easygui.msgbox(msg=e, title="Exception!")
        sys.exit()
server()
#os.chdir("..") continue on shell commands :)
