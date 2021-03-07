import argparse
import getpass
import os
import sys
import time
# from temp.pdf_check import ll

# description = "\tTo hide a message in a file:\n\t\tpython code.py encrypt --src SOURCE_FILE --msg MESSAGE_FILE --tgt PATH_WHERE_RESULT_IS_SAVED\n\tTo retrieve the hidden message from file:\n\t\tpython code.py decrypt --tgt TARGET_FILE_LOCATION\n"

parser = argparse.ArgumentParser(description="description")

parser.add_argument('choice', help="Enter encrypt or decrypt here!!!")
parser.add_argument('--src', help='Enter the location of source file (image, pdf, network packets)')
parser.add_argument('--msg', help='Enter the location of message to hide.')
parser.add_argument('--tgt', help='Enter the path to save output file.')

args = parser.parse_args()

################################################ CLASSES #########################################################

class CoolClass:
    
    def __init__(self):
        # print("Super init")
        self.src = args.src
        self.msg = args.msg
        self.tgt = args.tgt
        self.level_of_encryption = 1

    def putPass(self):

        pwd = getpass.getpass("Enter encryption key: ")
        cpwd = getpass.getpass("Confirm encrryption key: ")
        return pwd, cpwd

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


    # def putPass(self):
    #     pwd = getpass.getpass("Enter encryption key: ")
    #     # print("\033[32m")
    #     cpwd = getpass.getpass("Confirm encryption key: ")
    #     # print("\033[39m", end="")
    #     return pwd, cpwd

    def banner(self):
        print("------------------------------------------------------------------------------------------".center(100))
        print("--------------------------------------STEGNOGRAPHY----------------------------------------".center(100))
        print("------------------------------------------WITH--------------------------------------------".center(100))
        print("--------------------------------CUSTOM ENCYPTION METHOD-----------------------------------".center(100))
        print("------------------------------------------------------------------------------------------".center(100))


        print("""
         ____  _______  ____   _____           ____   _____    ___      _       ___              
        |         |    |      |        |\   | |    | |        |   |    / \     |   | |    |  \   / 
        |____     |    |____  |   __   | \  | |    | |   __   |___|   /___\    |___| |____|   \ /  
             |    |    |      |  |  |  |  \ | |    | |  |  |  |\     /     \   |     |    |    |   
         ____|    |    |____  |__|  |  |   \| |____| |__|  |  | \   /       \  |     |    |    |   

        """)
        

    def first_page(self):
        self.banner()        
        self.lock(100)
        self.pwd, self.cpwd = self.putPass()
            
        while(self.pwd!=self.cpwd):
            # print("\033[31m")
            print("\nIncorrect Confirmation Key, Please enter again!!!")
            # print("\033[39m")
            self.pwd, self.cpwd = self.putPass()

        print("\n '*' Symbolizes the strength of encryption, DEFAULT LEVEL: * ")
        self.level_of_encryption = input("\tEnter the level of encryption \n\t1: *\n\t2: **\n\t3: ***\n\t==> ")
        try:
            if(not (int(self.level_of_encryption)>=1 and int(self.level_of_encryption)<=3)):
                print("Level of encryption used will be default.")
                self.level_of_encryption = "1"
        except:
            print("Level of encryption used will be default.")
            self.level_of_encryption = "1"

    def calculations(self):
        pass

class Encryption(CoolClass):
    
    def __init__(self):
        # print("Encryption Called")
        self.level_of_encryption = 1
        super().__init__()
        if(self.src != None and self.msg != None):
            self.first_page()
            self.encrypt_here()
            # self.calculations()
        else:
            print("Kuch to daal do")

    def encrypt_here(self):
        # print("Encryption will be done here")
        print("Mesage entered: "+self.msg)
        print("Level of encryption chosen: "+self.level_of_encryption)
        self.encrypted_message = self.calculations(self.msg, self.level_of_encryption, self.pwd)

        print("Encrypted text: "+self.encrypted_message)
        # the encrypted text will then be hidden into the src file and save it in tgt location

    def calculations(self, msg, level_of_encryption, pwd):
        with open(self.msg, "r") as mm:
            mesg = mm.read()

        if(len(mesg)<10):
            msg_len = "000"+str(len(mesg))
        elif(len(mesg)<100):
            msg_len = "00"+str(len(mesg))
        elif(len(mesg)<1000):
            msg_len = "0"+str(len(mesg))
        else:
            print("Message length is exceeding the limit of 999 characters, it will automatically sliced to first 999 characters.")
            #we will also have to ask, if the user still wants to continue or re-enter the message
            ch = input("Would you like to continue? [Y/N]: ")
            if(ch=='N' or ch=='n'):
                print("Program Terminated Successfully. You can try again..".center(100))
                exit()
            mesg = mesg[0:1000]
            msg_len = "0999"
        
        salt = "{"+msg_len+self.level_of_encryption+"}" 
        return salt+mesg+salt

class Decryption(CoolClass):
    def __init__(self):
        print("Decryption called")
        super().__init__()
        print(self.src, self.msg)
        if(self.src != None and self.msg != None):
            print("Jyada shaane mt bno")
        else:
            self.tgt = args.tgt
            self.lock(150)
            self.decrypt_here()
            self.calculations()

    def decrypt_here(self):
        print("Decryption here")
        print(self.tgt)
        # print(self.level_of_encryption)

    def calculations(self):
        print("Reverse Calculations here")

if __name__ == '__main__':
    if(args.choice=='encrypt'):
        obj = Encryption()
    elif(args.choice=='decrypt'):
        obj = Decryption()


    # ll()