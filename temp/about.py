import random
import cowsay
import colorama
from colorama import Fore
colorama.init(autoreset=True)


def about_page():

    about_banner = [cowsay.cheese, cowsay.daemon, cowsay.dragon, cowsay.kitty, cowsay.meow, cowsay.milk, cowsay.pig, cowsay.stegosaurus, cowsay.turkey, cowsay.turtle]
    a = random.choice(about_banner)

    random_color = [Fore.RED,Fore.GREEN,Fore.YELLOW,Fore.BLUE,Fore.MAGENTA,Fore.CYAN,Fore.WHITE]
    b = random.choice(random_color)
    # b = b.upper()
    c = '''Hey!!!, what's up!!!,\n Heard you wanna know about us...'''
    print(a(b.c))
    print('')

about_page()