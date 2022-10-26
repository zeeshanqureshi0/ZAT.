#!/usr/bin/python3
#!/writter : ZEESHAN ALTAF
import os
import time
import sys

os.system("clear")

print('''\033[1;37m
                   
       d88888D  .d8b.  d888888b 
       YP  d8' d8' `8b `~~88~~' 
          d8'  88ooo88    88    
         d8'   88~~~88    88    
        d8' db 88   88    88    
       d88888P YP   YP    YP    
                                                                                                                                                                              
CREATED BY ZEESHAN ALTAF
''')
def slowprint(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(5. / 100)

print (''' \033[1;31m
+--------------------------------------+
| This Tool Install All Termux  Basic Packages |
+--------------------------------------+
| Coded By ZEESHAN ALTAF |version : 1.1  |
+--------------------------------------+''')

slowprint(''' \033[1;32m
[01] python
[02] python2
[03] python-dev
[04] python3
[05] php
[06] java
[07] git
[08] perl
[09] bash
[10] nano
[11] curl
[12] openssl
[13] openssh
[14] wget
[15] clang
[16] nmap
[17] w3m
[18] hydra
[19] ruby
[20] macchanger
[21] host
[22] dnsutils
[23] coreutils
[24] fish
[25] zip
[27] tor
[28] hydra
[29] figlet 
[30] cowsay
[31] tar
[32] unzip
[33] vim
[34] ruby
[35] wcalc
[36] bmon
[37] unrar
[38] proot
[39] golang''')
slowprint('''\033[1;37m
This Command for access Storage in Termux
[00] termux-setup-storage''')
print ("                                            ")
choice = input("\033[1;36mmDo You Want to Install All Packages [y/n] : ")
if choice == 'n' : sys.exit()
if choice == 'y' : os.system ("apt update")
os.system ("apt upgrade -y")
os.system ("apt install python -y")
os.system ("apt install python2 -y")
os.system ("apt install php -y")
os.system ("apt install python-dev -y")
os.system ("apt install python3 -y")
os.system ("apt install java -y")
os.system ("apt install git -y")
os.system ("apt install perl -y")
os.system ("apt install bash")

print ("wait for second and start hacking")

os.system ("apt install nano -y")
os.system ("apt install curl -y")
os.system ("apt install openssl -y")
os.system ("apt install openssh -y")
os.system ("apt install wget -y")
os.system ("apt install clang -y")
os.system ("apt install nmap -y")
os.system ("apt install w3m -y")
os.system ("apt install hydra -y")


print ("""
subscribe Zeeshan Altaf tricks""")

os.system ("apt install ruby -y")
os.system ("apt install macchanger -y")
os.system ("apt install host -y")
os.system ("apt install dnsutils -y")
os.system ("apt install coreutils -y")
os.system ("apt install fish -y")
os.system ("apt install zip -y")
os.system ("apt install hydra -y")
os.system ("apt install figlet -y")
os.system ("apt install cowsay -y")
os.system ("apt install unzip -y")
os.system ("apt install vim -y")
os.system ("apt install ruby -y")
os.system ("apt install wcalc -y")
os.system ("apt install bmon -y")
os.system ("apt install unrar -y")
os.system ("apt install proot -y")
os.system ("apt install golang -y")
print ("Allow the Button For Access the Storage in Termux")


os.system ("termux-setup-storage")
  
def slowprint(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(8. / 100)
print("\033[1;37m+-------------------------------------------------+")
slowprint('''\033[1;37m|  Welcome To Zeeshan Altaf tricks           |
|           Subscribe Our YouTube Channel         |
| Watch Ours Tutorials For Learn Zeeshan Altaf tricks  |''')
print("+-------------------------------------------------+")


input("\n\nPress the enter key to exit : ")
