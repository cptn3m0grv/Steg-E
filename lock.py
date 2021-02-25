# import colorama
# from colorama import Fore, Back, Style

# colorama.init(autoreset=True)
# # foreground color
# print(Fore.RED + 'STEGNOGRAPHY'.center(100))
# #print('\033[39m') 
# #clear character if we dont want to use it we can set autoreset=True in line 4 as argument
# #background color
# print(Back.CYAN + 'Using Custom Encryption Techniques'.center(100)) 
# print(Style.BRIGHT + 'Help Page!!'.center(100)) #Style of string to be printed
# print(Fore.YELLOW + Back.CYAN + 'Concatination'.center(100)) #concatinating fore as well as background
# #Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, HITE, RESET.
# #Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, HITE, RESET.
# #Style: DIM, NORMAL, BRIGHT, RESET_ALL 

# def lock():  
#     print("")
#     print("              ******           ".center(100))
#     print("         ***         ***        ".center(100))
#     print("      ((*               *))     ".center(100))
#     print("    ((*###################*))   ".center(100))
#     print("   #|                       |#  ".center(100))
#     print("   #|                       |#  ".center(100))
#     print("   #|          (*)          |#  ".center(100))
#     print("   #|          | |          |#  ".center(100))
#     print("   #|          |_|          |#  ".center(100))
#     print("   #|_______________________|#  ".center(100))

# lock()

import argparse
import getpass
import os

parser = argparse.ArgumentParser(description='Steganography')

parser.add_argument('--src', help='Enter the location of source file (image, pdf, network packets)')
parser.add_argument('--msg', help='Enter the location of message to hide.')
parser.add_argument('--tgt', help='Enter the path to save output file.')

args = parser.parse_args()


os.system("COPY {} > {}".format(args.src, args.tgt))

with open(args.msg) as message:
    message = message.readline()
    if(len(message)>50):
        message = message[0:51]
    var = "\n$AAGG$"+message
    # print(var)

with open(args.tgt, "a") as target:
    target.write(var)


def putPass():

    pwd = getpass.getpass("Enter encryption key: ")
    cpwd = getpass.getpass("Confirm encrryption key: ")
    return pwd, cpwd
    
pwd, cpwd = putPass()
    
while(pwd!=cpwd):
    print("Incorrect Confirmation Key, Please enter again!")
    pwd, cpwd = putPass()



def lock():  
    print("\n")
    print("              ******           ".center(150))
    print("         ***         ***        ".center(150))
    print("      ((*               *))     ".center(150))
    print("    ((*###################*))   ".center(150))
    print("   #|                       |#  ".center(150))
    print("   #|                       |#  ".center(150))
    print("   #|          (*)          |#  ".center(150))
    print("   #|          | |          |#  ".center(150))
    print("   #|          |_|          |#  ".center(150))
    print("   #|_______________________|#  ".center(150))

lock()
print("Key entered: " + pwd)
