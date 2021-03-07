### THis File is meant to take a input string, than reverse the string and apply rotation of alphabets with the factor of 7
## EASY ENCRPYTION 1: 
def rotateHere(temp):
    n = len(temp)
    d = 6%n
    resultL = temp[0:d]
    resultL = resultL[::-1]
    resultR = temp[d:n]
    resultR = resultR[::-1]

    result = resultL + resultR
    result = result[::-1]
    return result

def easyMethod_Rotate(message):
    temp = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ,.'
    rotated = rotateHere(temp)
    temp = 'a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'
    temp = temp.split(" ")
    temp.extend([" ", ",", "."])
    msg = message
    msg = msg[::-1] ## Reversing the message string
    rotified = ""
    for ch in msg:
        rotified = rotified + rotated[temp.index(ch)]
    return rotified.encode("utf-8")

print(easyMethod_Rotate("This is the BEST METHOD"))