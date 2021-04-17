import random
import cowsay

# about_banner = [cowsay.cheese('Hello!!!, what`s up!!!, Heard you wanna know about us.'), cowsay.daemon('Hello!!!, what`s up!!!, Heard you wanna know about us.'), cowsay.dragon('Hello!!!, what`s up!!!, Heard you wanna know about us.'), cowsay.kitty('Hello!!!, what`s up!!!, Heard you wanna know about us.'), cowsay.meow('Hello!!!, what`s up!!!, Heard you wanna know about us.'), cowsay.milk('Hello!!!, what`s up!!!, Heard you wanna know about us.'), cowsay.pig('Hello!!!, what`s up!!!, Heard you wanna know about us.'), cowsay.stegosaurus('Hello!!!, what`s up!!!, Heard you wanna know about us.'), cowsay.turkey('Hello!!!, what`s up!!!, Heard you wanna know about us.'), cowsay.turtle('Hello!!!, what`s up!!!, Heard you wanna know about us.')]

about_banner = [cowsay.cheese, cowsay.daemon, cowsay.dragon, cowsay.kitty, cowsay.meow, cowsay.milk, cowsay.pig, cowsay.stegosaurus, cowsay.turkey, cowsay.turtle]

a = random.choice(about_banner)

print(a('Hello!!!, what`s up!!!, Heard you wanna know about us.')) 

def about_page():
    
    about_random = random.choice(range(0, 10))

    if (about_random == 0):
        cowsay.cheese('Hello!!!, what`s up!!!, Heard you wanna know about us.')
    elif(about_random == 1):
        cowsay.daemon('Hello!!!, what`s up!!!, Heard you wanna know about us.')
    elif(about_random == 2):
        cowsay.dragon('Hello!!!, what`s up!!!, Heard you wanna know about us.')
    elif(about_random == 3):
        cowsay.kitty('Hello!!!, what`s up!!!, Heard you wanna know about us.')
    elif(about_random == 4):
        cowsay.meow('Hello!!!, what`s up!!!, Heard you wanna know about us.')
    elif(about_random == 5):
        cowsay.milk('Hello!!!, what`s up!!!, Heard you wanna know about us.')
    elif(about_random == 6):
        cowsay.pig('Hello!!!, what`s up!!!, Heard you wanna know about us.')
    elif(about_random == 7):
        cowsay.stegosaurus('Hello!!!, what`s up!!!, Heard you wanna know about us.')
    elif(about_random == 8):
        cowsay.turkey('Hello!!!, what`s up!!!, Heard you wanna know about us.')
    else:
        cowsay.turtle('Hello!!!, what`s up!!!, Heard you wanna know about us.')


    print('')