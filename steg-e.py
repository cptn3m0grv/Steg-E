import argparse
import getpass
import os
import sys
import time
from modules.EasyEncrypt import easyMethod_Rotate
from modules.EasyDecrypt import easyMethod_Decrypt
from modules.introScreen import key_graphics
from modules.introScreen import lock
from modules.introScreen import banner
import re


parser = argparse.ArgumentParser(description="description")

parser.add_argument('choice', help="Enter encrypt or decrypt here!!!")
parser.add_argument('--src', help='Enter the location of source file (image, pdf, network packets)')
parser.add_argument('--msg', help='Enter the location of message to hide.')
parser.add_argument('--tgt', help='Enter the path to save output file.')

args = parser.parse_args()

################################################ CLASSES #########################################################

class CoolClass:
    
    def __init__(self):
        self.src = args.src
        self.msg = args.msg
        self.tgt = args.tgt
        self.level_of_encryption = 1

    def putPass(self):
        pwd = getpass.getpass("Enter encryption key: ")
        cpwd = getpass.getpass("Confirm encrryption key: ")
        return pwd, cpwd

    def first_page(self):
        banner()        
        lock(150)
        self.pwd, self.cpwd = self.putPass()
            
        while(self.pwd!=self.cpwd):
            print("\nIncorrect Confirmation Key, Please enter again!!!")
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
        self.level_of_encryption = 1
        super().__init__()
        if(self.src != None and self.msg != None):
            self.first_page()
            self.encrypt_here()
        else:
            print("Kuch to daal do")

    def encrypt_here(self):
        print("Mesage entered: "+self.msg)
        print("Level of encryption chosen: "+self.level_of_encryption)
        self.encrypted_message = self.calculations()
        # user's key will be added in a salt to match the key
        # we may use some hashing method to hash the key and add it in the file
        message_to_hide = self.encrypted_message.encode('utf-8')

        try:
            with open(self.src, "rb") as sugar:
                image_orig = sugar.read()
                image_orig = image_orig+"\n".encode('utf-8')+message_to_hide
        except:
            print("Source file not found!!!")
            print("Program will now terminate!!!")
            exit()

        try:
            with open(self.tgt, "wb") as coffee:
                coffee.write(image_orig)
        except:
            print("Target File Not Created!!!")
            exit()
        
        print("Message saved to: ", self.tgt)
        print("\n")
        print("Success!!!".center(150))
        # the encrypted text will then be hidden into the src file and save it in tgt location

    def calculations(self):
        try:
            with open(self.msg, "r") as mm:
                mesg = mm.read()
        except:
            print("Unable to read message file!!!")
            exit()

        if(len(mesg)<10):
            msg_len = "000"+str(len(mesg))
        elif(len(mesg)<100):
            msg_len = "00"+str(len(mesg))
        elif(len(mesg)<1000):
            msg_len = "0"+str(len(mesg))
        else:
            print("Message length is exceeding the limit of 999 characters, it will automatically sliced to first 999 characters.")
            ch = input("Would you like to continue? [Y/N]: ")
            if(ch=='N' or ch=='n'):
                print("Program Terminated Successfully. You can try again..".center(100))
                exit()
            mesg = mesg[0:1000]
            msg_len = "0999"
        
        salt = "{"+msg_len+self.level_of_encryption+"}" 
        final_msg = ""
        if(int(self.level_of_encryption)==1):
            final_msg = easyMethod_Rotate(mesg)

        return salt+final_msg+salt

class Decryption(CoolClass):
    def __init__(self):
        super().__init__()
        if(self.src != None or self.msg != None):
            print("Wrong Arguments!!!!!")
            exit()
        else:
            banner()
            print()
            print()
            key_graphics(150)
            self.decrypt_here()

    def decrypt_here(self):
        message_to_display = self.calculations()
        print("Message here:\n\n"+message_to_display)

    def calculations(self):
        try:
            with open(self.tgt, "rb") as file:
                encrypted_source_msg = file.read()
        except:
            print("Unable to read target file!!!")
            print("Program will now terminate!!!")
            exit()


        encrypted_source_msg = re.findall(r"\{[0-9]{1,5}\}.*\{[0-9]{1,5}\}$".encode('utf-8'), encrypted_source_msg)
        length_of_message = int(encrypted_source_msg[0].decode('utf-8')[1:5])
        level_of_encryption = int(encrypted_source_msg[0].decode('utf-8')[5])

        if(level_of_encryption == 1):
            return easyMethod_Decrypt(encrypted_source_msg[0][7:7+length_of_message].decode('utf-8'))

        # return easyMethod_Decrypt(encrypted_source_msg)


if __name__ == '__main__':
    if(args.choice=='encrypt'):
        obj = Encryption()
    elif(args.choice=='decrypt'):
        obj = Decryption()
    else:
        print("Wrong Arguments!!!")
        exit()