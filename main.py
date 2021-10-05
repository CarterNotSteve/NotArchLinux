import time
import ctools
import os
import shutil
"""
ctools.util.print("Booting kernel processes...\n")
time.sleep(4)
ctools.util.print("starting core processes...\n")
time.sleep(0.5)

ctools.util.print("Starting init calls...\n")


ctools.util.print("kernel processes: ")
time.sleep(0.7)
ctools.util.print("[\033[94mOK!\033[0m]\n")
time.sleep(2)

ctools.util.print("Welcome to \033[94mNotArch\033[0m!\n")
time.sleep(2)
os.system('clear')
"""

reg=open('unypw.reg','r+')
usr=reg.readlines()
guest = True
PATH="root"
lia = "" # logged in as

while guest:
    un=input("Username: ")
    pw=input("Password: ")

    u=usr[0][3:]
    p=usr[1][3:]

    # account: un // pw
    accounts = {
        u:p
    }

    if un+"\n" == u and pw == p:
        ctools.util.print("Logged in!")
        time.sleep(3)
        os.system('clear')
        guest = False

    else:
        os.system('clear')
        ctools.util.print("[Denied]\n")
        continue

while not guest:
    cmd = input(PATH+" $ ")
    allcmd = cmd.split(" ")
    if cmd == "ls":
        print("  ".join(os.listdir("filesystem/"+PATH)))
        #ctools.util.print(" ".join(["".join(f[2]) for f in os.walk('filesystem/'+PATH)] )+" \n")

    elif cmd == "pwd":
        print(PATH)

    elif allcmd[0] == "cat":
        with open("filesystem/"+PATH+allcmd[1], "r") as o:
            if allcmd[1] in os.listdir("filesystem/"+PATH):
                k=o.readlines()
                
                for i in k:
                    ctools.util.print(i)
                print()

    elif allcmd[0] == "cd" and len(allcmd) > 1:
        if allcmd[1] in os.listdir("filesystem/"+PATH):
            PATH = PATH + "/" + allcmd[1] + "/"

        elif allcmd[1] == "..":
            tp = list(PATH)
            if tp != list("root/"):
                tp.reverse()
                tp.pop(0)
                while tp[0] != "/":
                    tp.pop(0)

                tp.pop(0)
                
                tp.reverse()
                PATH = "".join(tp)
                del(tp)

        else:
            ctools.util.print("No file or directory with that title exists!\n")

    elif allcmd[0] == "mkdir":
        os.mkdir("filesystem/"+PATH+"/"+allcmd[1])

    elif allcmd[0] == "touch":
        with open("filesystem/"+PATH+"/"+allcmd[1], "w+") as i:
            continue

    elif allcmd[0] == "mv":
        try:
            if allcmd[2] != "..":
                shutil.move("filesystem/"+PATH+allcmd[1], "filesystem/"+PATH+allcmd[2])
                ctools.util.print("filesystem/"+PATH+allcmd[2]+"\n")

        except:
            ctools.util.print("dev messed up here!\n")

    elif cmd == "exit":
        ctools.util.print("Goodbye.")
        break

    elif cmd == "clear":
        os.system('clear')

    elif cmd == 'pw':
        with open("unypw.reg", "r+") as f:
            k = ctools.util.load("unypw.reg")
            k.pop(1)
            k.append("pw=")
            x = input("New Password:")
            if (input("Confirm new: ") == x):
                k.append(x)

            else:
                print("Passwords do not match.")

            for i in k:
                f.write(i)

            del x
            del k
