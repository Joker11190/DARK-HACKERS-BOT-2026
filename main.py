import os
import time

R = "\033[91m"
G = "\033[92m"
C = "\033[96m"
Y = "\033[93m"
W = "\033[0m"

def menu():
    os.system("clear")
    print(R + """
    ██████╗  █████╗ ██████╗ ██╗  ██╗
    ██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝
    ██║  ██║███████║██████╔╝█████╔╝
    ██║  ██║██╔══██║██╔══██╗██╔═██╗
    ██████╔╝██║  ██║██║  ██║██║  ██╗
    """ + W)

    print(C + "       DARK HACKERS BOT" + W)
    print(G + "================================")
    print("[1] Network Scanner")
    print("[2] Device Information")
    print("[3] Python Information")
    print("[4] About DARK HACKERS")
    print("[0] Exit")
    print("================================" + W)

    choice = input(Y + "\nChoose: " + W)

    if choice == "1":
        os.system("python network_scan.py")
    elif choice == "2":
        os.system("uname -a")
        input("\nPress Enter...")
    elif choice == "3":
        os.system("python --version")
        input("\nPress Enter...")
    elif choice == "4":
        print(G + "\nWelcome to DARK HACKERS!")
        input("\nPress Enter...")
    elif choice == "0":
        print(R + "Goodbye!")
        return
    else:
        print(R + "Wrong Choice!")
        time.sleep(1)

    menu()

menu()

