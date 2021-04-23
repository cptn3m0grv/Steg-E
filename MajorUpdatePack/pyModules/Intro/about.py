import random
import cowsay
import colorama
from colorama import Fore, Style
colorama.init(autoreset=True)


def about_page():

    about_banner = [cowsay.cheese, cowsay.daemon, cowsay.dragon, cowsay.kitty, cowsay.meow, cowsay.milk, cowsay.pig, cowsay.stegosaurus, cowsay.turtle, 'b']
    a = random.choice(about_banner)
    if(a == 'b'):
        man()
    else:
        a("Hey!!!, what's up!!!,\n Heard you wanna know about us...")

    print(Fore.RED+Style.BRIGHT+"About Tool:\n") 
    print(Fore.CYAN+Style.BRIGHT+"What is STEG-E?\n")
    print(Fore.GREEN+"STEG-E is a tool specifically designed to perform the task of stegnography (i.e., hiding any crucial information under a base file). It is developed using python with addition of some essential features from object-oriented programming.\n")
    print(Fore.CYAN+Style.BRIGHT+"Many tools perform steganography, so what makes our tool different?\n")
    print(Fore.GREEN+"We formulate our algorithms to encode and decode the message to be hidden, with applied custom encryption algorithms on the message for its encryption and decryption. Using different levels of security, users can select different degree of encryption algorithms to be applied to the message before hiding it. The process of hiding the message can be performed over images(.png, .jpg, .jpeg), .pdf and network packets.\n\n")
    print(Fore.BLUE+Style.BRIGHT+"About Us:\n")
    print(Fore.MAGENTA+"Ashish Chaubey\n")
    print(Fore.YELLOW+Style.BRIGHT+"\tLinkedIn: https://www.linkedin.com/in/hackpandit/")
    print(Fore.YELLOW+Style.BRIGHT+"\n\tGithub: https://github.com/ashchaubey")
    print(Fore.MAGENTA+"\nAsmit Kumar Sharma\n")
    print(Fore.YELLOW+Style.BRIGHT+"\tLinkedIn: https://www.linkedin.com/in/asmit-sharma-a499b91ba/")
    print(Fore.YELLOW+Style.BRIGHT+"\n\tGithub: https://github.com/Dracula62")
    print(Fore.MAGENTA+"\nGargeya Sharma\n")
    print(Fore.YELLOW+Style.BRIGHT+"\tLinkedIn: https://www.linkedin.com/in/gargeya-sharma-4159801a3/")
    print(Fore.YELLOW+Style.BRIGHT+"\n\tGithub: https://github.com/Stalwart-GS")
    print(Fore.MAGENTA+"\nGaurav Goyal\n")
    print(Fore.YELLOW+Style.BRIGHT+"\tLinkedIn: https://www.linkedin.com/in/gaurav-goyal-4a850a173")
    print(Fore.YELLOW+Style.BRIGHT+"\n\tGithub: https://github.com/cptn3m0grv")


def man():
    print("                        _####_                        ".center(150))
    print("                      *        *                      ".center(150))
    print("                     /  .====.  \                     ".center(150))
    print("                     \/  @  @  \/                     ".center(150))
    print("                     (  \____/  )                     ".center(150))
    print("  _________ooo_______ \________/ __________________   ".center(150))
    print(" /                                                 \  ".center(150))
    print("|                                                   | ".center(150))
    print("| Me: Hey!!!                                        | ".center(150))
    print("| STEG-E: Hey!!!                                    | ".center(150))
    print("| Me: What's Up???                                  | ".center(150))
    print("| STEG-E: Heard You Wanna Know About Us...          | ".center(150))
    print("|                                                   | ".center(150))
    print(" \________________________________ooo______________/  ".center(150))
    print("                       |  |  |                        ".center(150))
    print("                       |_ | _|                        ".center(150))
    print("                       |  |  |                        ".center(150))
    print("                       |__|__|                        ".center(150))
    print("                       /-'^'-\                        ".center(150))
    print("                      (__/ \__)                       ".center(150))
    print("\n")