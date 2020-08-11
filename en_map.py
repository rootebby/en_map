import time
import os


print("""
                 _    ____       _     _
 _ __ ___   ___ | |_ / __ \  ___| |__ | |__  _   _ 
| '__/ _ \ / _ \| __/ / _` |/ _ \ '_ \| '_ \| | | |
| | | (_) | (_) | || | (_| |  __/ |_) | |_) | |_| |
|_|  \___/ \___/ \__\ \__,_|\___|_.__/|_.__/ \__, |
                     \____/                  |___/ 
""")

time.sleep(2)

print("""
  ___ _ __      _ __ ___   __ _ _ __       
 / _ \ '_ \    | '_ ` _ \ / _` | '_ \      
|  __/ | | |   | | | | | | (_| | |_) |     
 \___|_| |_|___|_| |_| |_|\__,_| .__/      
          |_____|              |_|  
""")
print("Auto NMAP tool for linux !!!")

time.sleep(2)

"""
EXAMPLES:
  nmap -v -A scanme.nmap.org
  nmap -v -sn 192.168.0.0/16 10.0.0.0/8
  nmap -v -iR 10000 -Pn -p 80
"""

print("""
1. Website
2. Ip Address
""")
cho = int(input("Option : "))

if cho == 1:
  url = input("URL : ")
  os.system("nmap -A {}".format(url))

elif cho == 2:
  ip = input("Ip : ")
  os.system("nmap {}".format(ip))

else:
  print("Select 1 or 2 ! ")