import argparse
import getpass
import os
import sys
import time
import itertools
import threading
import math
import random
import re
from pyModules.Easy.EasyEncrypt import easyMethod_Rotate
from pyModules.Easy.EasyDecrypt import easyMethod_Decrypt
from pyModules.Medium.MediumEncrypt import MediumEncrpyt_Method
from pyModules.Medium.MediumDecrypt import MediumDecrypt_Method
from pyModules.Hard.HardEncrypt import hard_encrypt
from pyModules.Hard.HardDecrypt import hard_decrypt
from pyModules.Intro.introScreen import key_graphics
from pyModules.Intro.introScreen import lock
from pyModules.Intro.introScreen import banner
from pyModules.Network.NetEncrypt import Net_Encrypt
from pyModules.Network.NetDecrypt import Net_Decrypt
from pyModules.Intro.about import about_page
import colorama
from colorama import Fore, Style
colorama.init(autoreset=True)

parser = argparse.ArgumentParser(description="description")

parser.add_argument('choice', help="encrpyt/decrypt/about/packetEncrypt/packetDecrypt")
parser.add_argument('--carrier', help='Enter the location of source file (.jpg, .jpeg, .png, .pdf)')
parser.add_argument('--data', help='Enter the location of message to hide.')
parser.add_argument('--result', help='Enter the path to save output file.')

args = parser.parse_args()

################################################ CLASSES #########################################################✔

class StegE:
    
    def __init__(self):
        self.src = args.carrier
        self.msg = args.data
        self.tgt = args.result
        self.level_of_encryption = 1

    def putPass(self):
        pwd = getpass.getpass("Enter encryption key: ")
        cpwd = getpass.getpass("Confirm encryption key: ")
        return pwd, cpwd

    def first_page(self):
        banner()        
        lock(150)

        try:
            self.pwd, self.cpwd = self.putPass()
        except:
            print("^C")
            print(Fore.RED+"Terminating program!!!")
            exit()
            
        while(self.pwd!=self.cpwd or len(self.pwd) == 0 or len(self.pwd) == 0):
            print("\n"+Fore.RED+"Incorrect Confirmation Key, Please enter again!!!")
            try:
                self.pwd, self.cpwd = self.putPass()
            except:
                print("^C")
                print(Fore.RED+"Terminating program!!!")
                exit()

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
        
        if(self.level_of_encryption == "1" or self.level_of_encryption == "2" or self.level_of_encryption == "3"):
            message_to_hide = self.encrypted_message.encode('utf-8')
                    
        try:
            with open(self.src, "rb") as sugar:
                image_orig = sugar.read()
                image_orig = image_orig + message_to_hide
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

    def calculations(self):
        if(int(self.level_of_encryption)==1):
            try:
                with open(self.msg, "r") as mm:
                    mesg = mm.read()
            except:
                print(Fore.RED+"Unable to read message file!!!")
                exit()

            if(len(mesg)<10):
                msg_len = "0000"+str(len(mesg))
            elif(len(mesg)<100):
                msg_len = "000"+str(len(mesg))
            elif(len(mesg)<1000):
                msg_len = "00"+str(len(mesg))
            elif(len(mesg)<10000):
                msg_len = "0"+str(len(mesg))
            else:
                print("Message length is exceeding the limit of 9999 characters, it will automatically sliced to first 999 characters.")
                ch = input("Would you like to continue? [Y/N]: ")
                if(ch=='N' or ch=='n'):
                    print(Fore.RED+"Program Terminated Successfully. You can try again..".center(100))
                    exit()
                mesg = mesg[0:10000]
                msg_len = "09999"
            
            salt = "$3%`/"
            rem = self.level_of_encryption+"@" 
            final_msg = ""
            final_msg = easyMethod_Rotate(mesg, self.pwd)   
            return salt+rem+final_msg+salt  

        elif(int(self.level_of_encryption)==2):
            try:
                with open(self.msg, "r") as coco:
                    cocoa = coco.read()
            except:
                print(Fore.RED+"Unable to read message file!!!")
                exit()
            ecr_msg = MediumEncrpyt_Method(cocoa, self.pwd)
            salt = "$3%`/"
            rem = self.level_of_encryption+"@"
            return salt+rem+ecr_msg+salt

        elif(int(self.level_of_encryption)==3):
            try:
                with open(self.msg, "r") as coca:
                    cola = coca.read()
            except:
                print(Fore.RED+"Unable to read message file!!!")
                exit()
            ecr_msg = hard_encrypt(cola, self.pwd)
            salt = "$3%`/"
            rem = self.level_of_encryption+"@"
            return salt+rem+ecr_msg+salt

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

    def keyInput(self):
        tempTulsi = getpass.getpass("Enter the password to Decrypt: ")
        confirmedTempTulsi = getpass.getpass("Confirm the password to decrypt: ")

        while(tempTulsi!=confirmedTempTulsi):
            print("Your keys don't match buddy, enter them again!!!!")
            tempTulsi = getpass.getpass("Enter the password to decrypt: ")
            confirmedTempTulsi = getpass.getpass("Confirm the password to decrypt: ")

        return tempTulsi

    def calculations(self):
        try:
            with open(self.tgt, "rb") as file:
                encrypted_source_msg = file.read()
        except:
            print(Fore.RED+"Unable to read target file!!!")
            print(Fore.RED+"Program will now terminate!!!")
            exit()

        try:
            encrypted_source_msg_temp = re.findall(r"\$3%`\/[123]@.*\$3%`\/".encode('utf-8'), encrypted_source_msg)
            # encrypted_source_msg_level_3 = re.findall(r"\$3\|\\\|!\)\|\\\|U!\)3\$@3@.*\$3\|\\\|!\)\|\\\|U!\)3\$".encode('utf-8'), encrypted_source_msg)

            # if(len(encrypted_source_msg_level_3)>0):
            #     level_of_encryption = int(encrypted_source_msg_level_3[0].decode('utf-8')[16])
            # else:
            level_of_encryption = int(encrypted_source_msg_temp[0].decode('utf-8')[5])
        except:
            print(Fore.RED+Style.BRIGHT+"The file has no encrypted message hidden.")
            exit()

        if(level_of_encryption == 1):
            msg_to_decrypt = encrypted_source_msg_temp[0].decode('utf-8')[7:-5]
            tulsi = self.keyInput()
            return easyMethod_Decrypt(msg_to_decrypt, tulsi)

        elif(level_of_encryption == 2):
            msg_to_decrypt = encrypted_source_msg_temp[0].decode('utf-8')[7:-5]
            tulsi = self.keyInput()
            try:
                return MediumDecrypt_Method(msg_to_decrypt, tulsi)
            except:
                return "Incorrect Key"

        elif(level_of_encryption == 3):
            msg_to_decrypt = encrypted_source_msg_temp[0].decode('utf-8')[7:-5]
            tulsi = self.keyInput()
            try:
                return hard_decrypt(msg_to_decrypt, tulsi)
            except:
                return "Incorrect Key"

class StegPack:
    def __init__(self):
        self.src = args.carrier
        self.msg = args.data
        self.tgt = args.result

    def calculations(self):
        '''The child classes will be defining this method'''
        pass


class PackEncrypt(StegPack):
    def __init__(self):
        super().__init__()
        if(self.src != None):
            print("You don't need to enter the carrier here, please refer help page!!!")
            exit()

        self.encr()

    def encr(self):
        tulsi = getpass.getpass("Enter the key: ")
        confirmedTulsi = getpass.getpass("Confirm the key: ")

        while(tulsi!=confirmedTulsi):
            print("Your keys don't match buddy, enter them again!!!!")
            tulsi = getpass.getpass("Enter the key: ")
            confirmedTulsi = getpass.getpass("Confirm the key: ")

        self.calculations(tulsi)

    def calculations(self, tulsi):
        try:
            with open(self.msg, "r") as coco:
                cocoa = coco.read()
        except:
            print(Fore.RED+"Unable to read message file!!!")
            exit()

        encr_cocoa = easyMethod_Rotate(cocoa, tulsi)
        flag = False
        def animate():
            for symbol in itertools.cycle([Fore.CYAN+"⢿", Fore.CYAN+"⣻", Fore.CYAN+"⣽", Fore.CYAN+"⣾", Fore.CYAN+"⣷", Fore.CYAN+"⣯", Fore.CYAN+"⣟", Fore.CYAN+"⡿"]):
                if flag:
                    break
                sys.stdout.write(Fore.CYAN+'\rEncrypting..... ' + symbol + '     ')
                sys.stdout.flush()
                time.sleep(0.2)
            sys.stdout.write(Fore.GREEN+'\rEncrypted!!!     ')

        t = threading.Thread(target=animate)
        t.start()
        Net_Encrypt(encr_cocoa, tulsi, self.tgt)
        flag = True

               

class PackDecrypt(StegPack):
    def __init__(self):
        super().__init__()
        if(self.src != None or self.msg != None):
            print("You only need to mention the network file here, refer to the help page.")
            exit()
        
        self.decr()
    
    def decr(self):
        tulsi = getpass.getpass("Enter the key: ")
        confirmedTulsi = getpass.getpass("Confirm the key: ")

        while(tulsi!=confirmedTulsi):
            print("Your keys don't match buddy, enter them again!!!!")
            tulsi = getpass.getpass("Enter the key: ")
            confirmedTulsi = getpass.getpass("Confirm the key: ")

        encr_msg = self.calculations(tulsi)
        decr_msg = easyMethod_Decrypt(encr_msg, tulsi)
        print("\nYour message here:\n")
        print(decr_msg)

    def calculations(self, tulsi):        
        ecr_msf_from_packet = Net_Decrypt(tulsi, self.tgt)
        if(ecr_msf_from_packet == "Enter the right key!!!!"):
            print("\nEnter the right key!!!")
            exit()

        return ecr_msf_from_packet

if __name__ == '__main__':
    if(args.choice=='about'):
        about_page() 
        #pass
    elif(args.choice=='encrypt'):
        obj = Encryption()
    elif(args.choice=='decrypt'):
        obj = Decryption()
    elif(args.choice=='packetEncrypt'):
        obj = PackEncrypt()
    elif(args.choice=='packetDecrypt'):
        obj = PackDecrypt()
    else:
        print(Fore.RED+"Wrong Arguments!!!")
        exit()