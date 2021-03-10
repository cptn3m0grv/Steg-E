import colorama
from colorama import Fore, Style
colorama.init(autoreset=True)
import time


def key_graphics(width):
    print(Style.BRIGHT+Fore.GREEN+"                                     ________     ".center(width))
    time.sleep(0.07)
    print(Style.BRIGHT+Fore.GREEN+"                                    / ______ \    ".center(width))
    time.sleep(0.07)
    print(Style.BRIGHT+Fore.GREEN+" __________________________________/ |      | \   ".center(width))
    time.sleep(0.07)
    print(Style.BRIGHT+Fore.GREEN+"/____________________________________|      |  |  ".center(width))
    time.sleep(0.07)
    print(Style.BRIGHT+Fore.GREEN+"\__     __  __     ________________  |      |  |  ".center(width))
    time.sleep(0.07)
    print(Style.BRIGHT+Fore.GREEN+"   \ | /  \/  \ | /                \ |______| /   ".center(width))
    time.sleep(0.07)
    print(Style.BRIGHT+Fore.GREEN+"    |||        |||                  \________/    ".center(width))
    time.sleep(0.07)
    print(Style.BRIGHT+Fore.GREEN+"    /|\        /|\                                ".center(width))
    time.sleep(0.07)
    print(Style.BRIGHT+Fore.GREEN+"    \_/        \┴/                                ".center(width))
    time.sleep(0.07)
    print("\n\n")
    

def lock(width):
    print("\n")
    print(Style.BRIGHT+Fore.YELLOW+"              ******           ".center(width))
    time.sleep(0.07)
    print(Style.BRIGHT+Fore.YELLOW+"         ***         ***        ".center(width))
    time.sleep(0.07)
    print(Style.BRIGHT+Fore.YELLOW+"      ((*               *))     ".center(width))
    time.sleep(0.07)
    print(Style.BRIGHT+Fore.YELLOW+"    ((*                   *))  ".center(width))
    time.sleep(0.07)
    print(Style.BRIGHT+Fore.YELLOW+"    ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄  ".center(width))
    time.sleep(0.07)
    print(Style.BRIGHT+Fore.YELLOW+"    ▓                       ▓  ".center(width))
    time.sleep(0.07)
    print(Style.BRIGHT+Fore.YELLOW+"    ▓                       ▓  ".center(width))
    time.sleep(0.07)
    print(Style.BRIGHT+Fore.YELLOW+"    ▓                       ▓  ".center(width))
    time.sleep(0.07)
    print(Style.BRIGHT+Fore.YELLOW+"    ▓          (*)          ▓  ".center(width))
    time.sleep(0.07)
    print(Style.BRIGHT+Fore.YELLOW+"    ▓          | |          ▓  ".center(width))
    time.sleep(0.07)
    print(Style.BRIGHT+Fore.YELLOW+"    ▓          |_|          ▓  ".center(width))
    time.sleep(0.07)
    print(Style.BRIGHT+Fore.YELLOW+"    ▓▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▓  ".center(width))


def banner():
    print()
    print(Fore.MAGENTA+"███████╗████████╗███████╗ ██████╗               ███████╗".center(150))
    print(Fore.MAGENTA+"██╔════╝╚══██╔══╝██╔════╝██╔════╝               ██╔════╝".center(150))
    print(Fore.MAGENTA+"███████╗   ██║   █████╗  ██║  ███╗    █████╗    █████╗  ".center(150))
    print(Fore.MAGENTA+"╚════██║   ██║   ██╔══╝  ██║   ██║    ╚════╝    ██╔══╝  ".center(150))
    print(Fore.MAGENTA+"███████║   ██║   ███████╗╚██████╔╝              ███████╗".center(150))
    print(Fore.MAGENTA+"╚══════╝   ╚═╝   ╚══════╝ ╚═════╝               ╚══════╝".center(150))