import click
import getpass
import os
import sys

# description = "\tTo hide a message in a file:\n\t\tpython code.py encrypt --src SOURCE_FILE --msg MESSAGE_FILE --tgt PATH_WHERE_RESULT_IS_SAVED\n\tTo retrieve the hidden message from file:\n\t\tpython code.py decrypt --tgt TARGET_FILE_LOCATION\n"

@click.command()
@click.option('--encrypt', is_flag=True, default=False)
@click.option('--decrypt', is_flag=True, default=False)
@click.option('--src', help='Enter the location of source file')
@click.option('--msg', help="Enter the message to hide")
@click.option('--tgt', default=".",help="Location to save the result")

def check(encrypt, src, msg, tgt, decrypt):
    """\tTo hide a message in a file:\n\n\t\tpython code.py encrypt --src SOURCE_FILE --msg MESSAGE_FILE --tgt PATH_OF_FILE_SAVED\n\n\tTo retrieve the hidden message from file:\n\n\t\tpython code.py decrypt --tgt TARGET_FILE_LOCATION\n"""

    flag = False
    if(encrypt and  not decrypt):
        print(str(sys.platform))
        print("src: ", type(src))
        print("msg: ", type(msg))
        print("tgt: ", type(tgt))
        flag = True
    elif(decrypt and not encrypt):
        print("decrypt working")
        flag = True
    else:
        print("Rerun the program using right arguments")

    if(flag):
        chlo()

def lock():  
    print("\n")
    print("              ******           ".center(100))
    print("         ***         ***        ".center(100))
    print("      ((*               *))     ".center(100))
    print("    ((*###################*))   ".center(100))
    print("   #|                       |#  ".center(100))
    print("   #|                       |#  ".center(100))
    print("   #|          (*)          |#  ".center(100))
    print("   #|          | |          |#  ".center(100))
    print("   #|          |_|          |#  ".center(100))
    print("   #|_______________________|#  ".center(100))


def putPass():
    pwd = getpass.getpass("Enter encryption key: ")
    print("\033[32m")
    cpwd = getpass.getpass("Confirm encryption key: ")
    print("\033[39m", end="")
    return pwd, cpwd


def chlo():        
    lock()
    pwd, cpwd = putPass()
        
    while(pwd!=cpwd):
        print("\033[31m")
        print("\nIncorrect Confirmation Key, Please enter again!!!")
        print("\033[39m")
        pwd, cpwd = putPass()

    print("Key entered: ", end="")
    print(pwd)


check()