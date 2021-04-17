import random
import cowsay
import colorama
from colorama import Fore,Style
colorama.init(autoreset=True)

def about_page():

    about_banner = [cowsay.cheese, cowsay.daemon, cowsay.dragon, cowsay.kitty, cowsay.meow, cowsay.milk, cowsay.pig, cowsay.stegosaurus, cowsay.turkey, cowsay.turtle]
    a = random.choice(about_banner)

    randon_color = [red, green, yellow, blue, magenta, cyan, white]
    b = ramdon.choice(random_color)
    b = b.upper()
    print(a( Fore.b + "Hey!!!, what's up!!!,\n Heard you wanna know about us..."))

    print('')

about_page()