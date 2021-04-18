import random
import cowsay
import colorama
from colorama import Fore
colorama.init(autoreset=True)


def about_page():

    about_banner = [cowsay.cheese, cowsay.daemon, cowsay.dragon, cowsay.kitty, cowsay.meow, cowsay.milk, cowsay.pig, cowsay.stegosaurus, cowsay.turkey, cowsay.turtle]
    # a = random.choice(about_banner)
    random.choice(about_banner)('''Hey!!!, what's up!!!,\n Heard you wanna know about us...''')

    print(Fore.RED+"About Tool:\n") 
    print(Fore.CYAN+"Many tools perform steganography, so what makes our tool different?\n")
    print(Fore.GREEN+"We will formulate our algorithms to encode and decode the message to be hidden, with applied custom encryption algorithms on the message for its encryption and decryption. Using different levels of security, users can select different encryption algorithms to be applied to the message to encrypt it before hiding it. We will be developing this project in python language in addition to some essential features from object-oriented programming.\n")

# about_page()