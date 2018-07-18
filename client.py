#!/usr/bin/env python
import os, sys, socket, easygui, threading, time, subprocess, base64, configparser, getpass
shell = 0
if os.path.exists("details.ini"):
    pass
else:
    subprocess.call("./starter.py", shell=True)
    sys.exit()
config = configparser.ConfigParser()
config.read("details.ini")
shost = config["DEFAULT"]["server"]
sport  = config["DEFAULT"]["sport"]
host = config["DEFAULT"]["client"]
port  = config["DEFAULT"]["cport"]
name   = config["DEFAULT"]["name"]
def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host,int(port)))
        while True:
            def send_message():
                global shell
                global txt
                #if shell == 1:
                    #txt = "\033[95mshell@send_command:# \033[0m"
                if shell == 0:
                    txt = "\033[0mSend message: "
                if shell == 1:
                    txt = "\033[95m\033[1mshell# \033[0m\033[93m"
                ans=raw_input(txt)
                if shell == 0 and ans=="shell=block":
                    s.connect(shost,int(sport))
                    s.send("shell=exit")
                    s.close()
                elif ans=="exit -y":
                    sys.exit()
                elif ans=="help":
                    def help():
                        print("Help commands")
                        print
                        print("Commands while shell is opened")
                        print("   shell=exit                --to close shell")
                        print("   file=upload file=<file>   --to upload a file")
                        print("   file=download file=<file> --to download a file")
                        print("   lls                       --ls for your files")
                        print("   ccd                       --change your working directory on your folders")
                        print("   cwd                       --print working directory on connected host")
                        print("   lcwd                      --print your current working directory")
                        print
                        print("Commands while shell is closed")
                        print("   shell=open code=3024             --to open shell")
                        print("   shell=open ask=no pass=<password --open shell with password, no ask for permission")
                        print
                        print("    exit -y                  --to exit tool. Works on both shell and message mode")
                        print("    help                     --print this")
                        print("* Program will look for commands in input. It will not try to match exactly the input with the commands")
                        main()
                    help()
                elif shell == 1 and ans=="lcwd":
                    print(os.getcwd())
                    main()
                elif shell == 1 and ans=="lls":
                    subprocess.call("ls", shell=True)
                    main()
                elif shell == 1 and ans=="ccd":
                    print("Hit enter to return")
                    f=raw_input("Path: ")
                    if len(f) > 0:
                        os.chdir(f)
                    main()
                elif shell == 1 and ans=="print cwd":
                    s.send("print cwd")
                    main()
                elif ans=="shell=exit":
                    shell = 0
                    s.send("shell=exit")
                    main()
#                elif ans == "file=upload file=":
#                    print(ans)
#                    if os.path.exists(ans[19:]):
#                        file=open(ans[19:], "r")
#                        f=file.read()
#                        file.close()
#                        file=open(ans[19:] + ".ini", "w")
#                        file.write("[FILE]\nname: %s\ntxt: %s" & (ans[18], f))
#                        f=file.read()
#                        file.close()
#                        s.send("file=upload text=%s" % f)
#                        subprocess.call("rm %s.ini" % ans[19], shell=True)
                if shell == 1 and ans=="exit":
                    shell = 0
                    s.send("shell=exit")
                if shell == 1:
                    s.send(ans)
                else:
                    s.send("[%s](%s): %s " % (time.strftime("%H:%M:%S"),name,ans))
                r = s.recv(4098)
                if "Failed to execute the command" and "shell=open code=3024" in r:
                    show = 0
                if "shell=open -yes" in r:
                    shell = 1
                if "shell=closed" in r:
                    shell = 0
                    txt = "\033[0mSend message: "
                if "noask" in r:
                    shell = 1
                else:
                    if r:
                        print(r)
                    else:
                        if shell == 1:
                            print("\033[91mShell closed\033[0m")
                        shell = 0
                    #if not "1" in r:
                    #    print(time.strftime("%H:%M:%S"),r)
                main()
            send_message()
    except KeyboardInterrupt:
        print("Cant use KeyboardInterrupt. Use exit -y to exit")
        main()
    except socket.error:
        print("socket.error < Trying to return... [Host seems offline]")
        time.sleep(5)
        main()
        """
    except Exception, e:
        print e
    #    easygui.msgbox(msg=e, title="Exception!")
        sys.exit()
        """
main()
