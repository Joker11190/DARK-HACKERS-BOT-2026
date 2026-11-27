import os
import socket
import subprocess

os.system("clear")

print("\033[91m")
print("================================")
print("       DARK HACKERS")
print("       NETWORK SCANNER")
print("================================")
print("\033[92m")

hostname = socket.gethostname()

try:
    ip = socket.gethostbyname(hostname)
except:
    ip = "غير معروف"

print("[+] اسم الجهاز:", hostname)
print("[+] عنوان IP:", ip)

print("\n[+] فحص اتصال الإنترنت...")

try:
    socket.create_connection(("1.1.1.1", 53), timeout=3)
    print("\033[92m[ONLINE] الإنترنت متصل")
except:
    print("\033[91m[OFFLINE] لا يوجد اتصال")

print("\n\033[96m[+] انتهى الفحص")
print("\033[91mDARK HACKERS TEAM")
print("\033[0m")
