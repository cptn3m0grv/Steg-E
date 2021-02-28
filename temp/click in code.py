import click
import getpass
# import os
import sys
import time

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
        obj = Banner();
        obj.first_page()

def hide():

    # def lock(width):  
    #     print("\n")
    #     print("              ******           ".center(width))
    #     time.sleep(0.07)
    #     print("         ***         ***        ".center(width))
    #     time.sleep(0.07)
    #     print("      ((*               *))     ".center(width))
    #     time.sleep(0.07)
    #     print("    ((*###################*))   ".center(width))
    #     time.sleep(0.07)
    #     print("   #|                       |#  ".center(width))
    #     time.sleep(0.07)
    #     print("   #|                       |#  ".center(width))
    #     time.sleep(0.07)
    #     print("   #|          (*)          |#  ".center(width))
    #     time.sleep(0.07)
    #     print("   #|          | |          |#  ".center(width))
    #     time.sleep(0.07)
    #     print("   #|          |_|          |#  ".center(width))
    #     time.sleep(0.07)
    #     print("   #|_______________________|#  ".center(width))


    # def putPass():
    #     pwd = getpass.getpass("Enter encryption key: ")
    #     # print("\033[32m")
    #     cpwd = getpass.getpass("Confirm encryption key: ")
    #     # print("\033[39m", end="")
    #     return pwd, cpwd


    # def first_page():        
    #     lock(100)
    #     pwd, cpwd = putPass()
            
    #     while(pwd!=cpwd):
    #         print("\033[31m")
    #         print("\nIncorrect Confirmation Key, Please enter again!!!")
    #         print("\033[39m")
    #         pwd, cpwd = putPass()

    #     # print("Key entered: ", end="")
    #     print("\n '*' Symbolizes the strength of encryption, DEFAULT LEVEL: * ")
    #     level_of_encryption = input("\tEnter the level of encryption \n\t1: *\n\t2: **\n\t3: ***\n\t==> ")
    #     try:
    #         if(not (int(level_of_encryption)>=1 and int(level_of_encryption)<=3)):
    #             print("Level of encryption used will be default.")
    #     except:
            # print("Level of encryption used will be default.")

        # print(level_of_encryption)
    pass


class Banner:

    def __init__(self):
        pass

    def lock(self, width):  
        print("\n")
        print("              ******           ".center(width))
        time.sleep(0.07)
        print("         ***         ***        ".center(width))
        time.sleep(0.07)
        print("      ((*               *))     ".center(width))
        time.sleep(0.07)
        print("    ((*###################*))   ".center(width))
        time.sleep(0.07)
        print("   #|                       |#  ".center(width))
        time.sleep(0.07)
        print("   #|                       |#  ".center(width))
        time.sleep(0.07)
        print("   #|          (*)          |#  ".center(width))
        time.sleep(0.07)
        print("   #|          | |          |#  ".center(width))
        time.sleep(0.07)
        print("   #|          |_|          |#  ".center(width))
        time.sleep(0.07)
        print("   #|_______________________|#  ".center(width))


    def putPass(self):
        pwd = getpass.getpass("Enter encryption key: ")
        # print("\033[32m")
        cpwd = getpass.getpass("Confirm encryption key: ")
        # print("\033[39m", end="")
        return pwd, cpwd


    def first_page(self):        
        self.lock(100)
        pwd, cpwd = self.putPass()
            
        while(pwd!=cpwd):
            print("\033[31m")
            print("\nIncorrect Confirmation Key, Please enter again!!!")
            print("\033[39m")
            pwd, cpwd = self.putPass()

        # print("Key entered: ", end="")
        print("\n '*' Symbolizes the strength of encryption, DEFAULT LEVEL: * ")
        level_of_encryption = input("\tEnter the level of encryption \n\t1: *\n\t2: **\n\t3: ***\n\t==> ")
        try:
            if(not (int(level_of_encryption)>=1 and int(level_of_encryption)<=3)):
                print("Level of encryption used will be default.")
        except:
            print("Level of encryption used will be default.")



if __name__ == '__main__':
    check()

