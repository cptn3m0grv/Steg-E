import random
import cowsay

# about_banner = [cowsay.cheese('Hello!!!, what`s up!!!, Heard you wanna know about us.'), cowsay.daemon('Hello!!!, what`s up!!!, Heard you wanna know about us.'), cowsay.dragon('Hello!!!, what`s up!!!, Heard you wanna know about us.'), cowsay.kitty('Hello!!!, what`s up!!!, Heard you wanna know about us.'), cowsay.meow('Hello!!!, what`s up!!!, Heard you wanna know about us.'), cowsay.milk('Hello!!!, what`s up!!!, Heard you wanna know about us.'), cowsay.pig('Hello!!!, what`s up!!!, Heard you wanna know about us.'), cowsay.stegosaurus('Hello!!!, what`s up!!!, Heard you wanna know about us.'), cowsay.turkey('Hello!!!, what`s up!!!, Heard you wanna know about us.'), cowsay.turtle('Hello!!!, what`s up!!!, Heard you wanna know about us.')]

about_banner = [cowsay.cheese, cowsay.daemon, cowsay.dragon, cowsay.kitty, cowsay.meow, cowsay.milk, cowsay.pig, cowsay.stegosaurus, cowsay.turkey, cowsay.turtle]

a = random.choice(about_banner)

print(a('Hello!!!, what`s up!!!, Heard you wanna know about us.')) 

def about_page():

    about_banner = [cowsay.cheese, cowsay.daemon, cowsay.dragon, cowsay.kitty, cowsay.meow, cowsay.milk, cowsay.pig, cowsay.stegosaurus, cowsay.turkey, cowsay.turtle]
    a = random.choice(about_banner)

    randon_color = [red, green, yellow, blue, magenta, cyan, white]
    b = ramdon.choice(random_color)
    b = b.upper()
    print(a( Fore.b + "Hey!!!, what's up!!!,\n Heard you wanna know about us..."))

    print('')

about_page()