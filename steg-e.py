import argparse
import getpass
import os
import sys
import time
from pyModules.Easy.EasyEncrypt import easyMethod_Rotate
from pyModules.Easy.EasyDecrypt import easyMethod_Decrypt
from pyModules.Medium.MediumEncrypt import MediumEncrpyt_Method
from pyModules.Medium.MediumDecrypt import MediumDecrypt_Method
from pyModules.Intro.introScreen import key_graphics
from pyModules.Intro.introScreen import lock
from pyModules.Intro.introScreen import banner
import re
import colorama
from colorama import Fore, Style
colorama.init(autoreset=True)

parser = argparse.ArgumentParser(description="description")

parser.add_argument('choice', help="Enter encrypt or decrypt here!!!")
parser.add_argument('--src', help='Enter the location of source file (image, pdf, network packets)')
parser.add_argument('--msg', help='Enter the location of message to hide.')
parser.add_argument('--tgt', help='Enter the path to save output file.')

args = parser.parse_args()

################################################ CLASSES #########################################################

class StegE:
    
    def __init__(self):
        self.src = args.src
        self.msg = args.msg
        self.tgt = args.tgt
        self.level_of_encryption = 1

    def putPass(self):
        pwd = getpass.getpass("Enter encryption key: ")
        cpwd = getpass.getpass("Confirm encryption key: ")
        return pwd, cpwd

    def first_page(self):
        banner()        
        lock(150)
        self.pwd, self.cpwd = self.putPass()
            
        while(self.pwd!=self.cpwd):
            print("\n"+Fore.RED+"Incorrect Confirmation Key, Please enter again!!!")
            self.pwd, self.cpwd = self.putPass()

        print("\n '*' Symbolizes the strength of encryption, DEFAULT LEVEL: * ")
        print(Fore.CYAN+"\tEnter the level of encryption \n\t1: *\n\t2: **\n\t3: ***\n\t==> ", end=" ")
        self.level_of_encryption = input()
        try:
            if(not (int(self.level_of_encryption)>=1 and int(self.level_of_encryption)<=3)):
                print(Fore.GREEN+"Level of encryption used will be default.")
                self.level_of_encryption = "1"
        except:
            print(Fore.GREEN+"Level of encryption used will be default.")
            self.level_of_encryption = "1"

    def calculations(self):
        pass

class Encryption(StegE):
    
    def __init__(self):
        self.level_of_encryption = 1
        super().__init__()
        if(self.src != None and self.msg != None):
            self.first_page()
            self.encrypt_here()
        else:
            print(Style.BRIGHT+Fore.RED+"Wrong Arguments!!!")
            exit()

    def encrypt_here(self):
        print("Level of encryption chosen: "+self.level_of_encryption)
        self.encrypted_message = self.calculations()
        message_to_hide = self.encrypted_message.encode('utf-8')

        try:
            with open(self.src, "rb") as sugar:
                image_orig = sugar.read()
                image_orig = image_orig+message_to_hide
        except:
            print(Fore.RED+"Source file not found!!!")
            print(Fore.RED+"Program will now terminate!!!")
            exit()

        try:
            with open(self.tgt, "wb") as coffee:
                coffee.write(image_orig)
        except:
            print(Fore.RED+"Target File Not Created!!!")
            exit()
        
        print(Fore.GREEN+"Target saved to: ", self.tgt)
        print("\n")
        print(Fore.GREEN+"**** Success ****".center(150))
        # the encrypted text will then be hidden into the src file and save it in tgt location

    def calculations(self):

        if(int(self.level_of_encryption)==1):
            try:
                with open(self.msg, "r") as mm:
                    mesg = mm.read()
            except:
                print(Fore.RED+"Unable to read message file!!!")
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
                    print(Fore.RED+"Program Terminated Successfully. You can try again..".center(100))
                    exit()
                mesg = mesg[0:1000]
                msg_len = "0999"
            
            salt = "{"+msg_len+self.level_of_encryption+"}" 
            final_msg = ""
            final_msg = easyMethod_Rotate(mesg, self.pwd)
            
            return salt+final_msg+salt  

        elif(int(self.level_of_encryption)==2):
            try:
                with open(self.msg, "r") as coco:
                    cocoa = coco.read()
            except:
                print(Fore.RED+"Unable to read message file!!!")
                exit()

            ecr_msg = MediumEncrpyt_Method(cocoa, self.pwd)

            salt = "{"+str(len(ecr_msg))+self.level_of_encryption+"}"
        
            return salt+ecr_msg+salt

        elif(int(self.level_of_encryption)==3):
            pass


class Decryption(StegE):
    def __init__(self):
        super().__init__()
        if(self.src != None or self.msg != None):
            print(Fore.RED+"Wrong Arguments!!!!!")
            exit()
        else:
            banner()
            print()
            print()
            key_graphics(150)
            self.decrypt_here()

    def decrypt_here(self):
        message_to_display = self.calculations()
        print("Do you also want to save the decrypted message to a separate file (y/n): ", end=" ")
        ch = input()
        ch = ch.lower()
        if(ch=='y'):
            output_file = input("Enter the output location: ")
            try:
                with open(output_file, "w") as ginger:
                    ginger.write(message_to_display)
            except:
                print(Fore.RED+"Cannot save output to file.")
        elif(not(ch=='n')):
            print("Not a valid choice, message will only be displayed on terminal.")

        print("\nMessage here:\n"+Fore.CYAN+message_to_display)

    def calculations(self):

        try:
            with open(self.tgt, "rb") as file:
                encrypted_source_msg = file.read()
        except:
            print(Fore.RED+"Unable to read target file!!!")
            print(Fore.RED+"Program will now terminate!!!")
            exit()


        encrypted_source_msg_temp = encrypted_source_msg
        encrypted_source_msg_temp = re.findall(r"\{[0-9]{2,}\}.*\{[0-9]{2,}\}$".encode('utf-8'), encrypted_source_msg)
        level_of_encryption = int(encrypted_source_msg_temp[0].decode('utf-8')[-2])

        if(level_of_encryption == 1):
            
            encrypted_source_msg = re.findall(r"\{[0-9]{1,5}\}.*\{[0-9]{1,5}\}$".encode('utf-8'), encrypted_source_msg)
            length_of_message = int(encrypted_source_msg[0].decode('utf-8')[1:5])
            level_of_encryption = int(encrypted_source_msg[0].decode('utf-8')[5])

            tulsi = input("Enter the password to Decrypt: ")
            
            return easyMethod_Decrypt(encrypted_source_msg[0][7:7+length_of_message].decode('utf-8'), tulsi)

        elif(level_of_encryption == 2):

            encrypted_source_msg = re.findall(r"2\}.*\{".encode('utf-8'), encrypted_source_msg)
            encrypted_source_msg = encrypted_source_msg[-1].decode('utf-8')[2:-1]

            tulsi = input("Enter the password to Decrypt: ")
            
            try:
                return MediumDecrypt_Method(encrypted_source_msg, tulsi)
            except:
                return "Incorrect Key"

        elif(level_of_encryption == 3):
            pass

if __name__ == '__main__':
    if(args.choice=='encrypt'):
        obj = Encryption()
    elif(args.choice=='decrypt'):
        obj = Decryption()
    else:
        print(Fore.RED+"Wrong Arguments!!!")
        exit()