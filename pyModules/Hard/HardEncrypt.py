import numpy as np
from customDict import ourDict

def isValid(aChar):
    if ord(aChar)>=97 and ord(aChar)<=122:
        return True
    
    if ord(aChar)>=65 and ord(aChar)<=90:
        return True

    if ord(aChar)>=48 and ord(aChar)<=57:
        return True

    validList = [ord('!'), ord('@'), ord('#'), ord('$'), ord('%'), ord('^'), ord('&'), ord('*'), ord('('), ord(')'), ord('-'), ord('_'), ord('='), ord('+'), ord('['), ord(']'), ord('{'), ord('}'), ord('/'), ord('|'), ord(';'), ord(':'), ord(','), ord('.'), ord('<'), ord('>'), ord('?'), ord('~'), ord(' '), ord('`'), ord('"'), ord("'")]

    if(ord(aChar) in validList):
        return True

    return False

def splitMessage(message):
    msg_len = len(message)

    if msg_len%2==0:
        part1 = message[0:(msg_len//2)]
        part2 = message[(msg_len//2):]
    else:
        part1 = message[0:(msg_len//2)+1]
        part2 = message[(msg_len//2)+1:]

    return part1, part2

def rotateHere(temp, rotTimes):
    n = len(temp)
    rotTimes = rotTimes%n
    resultL = temp[0:rotTimes]
    resultL = resultL[::-1]
    resultR = temp[rotTimes:n]
    resultR = resultR[::-1]

    result = resultL + resultR
    result = result[::-1]
    return result

def easyMethod_Rotate(message, pwd):

    rotTimes = 0
    idx = 1

    for chAt in pwd:
        rotTimes = rotTimes + (ord(chAt)*idx)
        idx += 1

    temp = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()-_=+[]'
    temp = temp + "{"
    temp = temp + '}/|;:,.<>?~ '
    temp = temp + "'"
    temp = temp + '"'

    rotated = rotateHere(temp, rotTimes)

    temp = 'a b c d e f g h i j k l m n o p q r s t u v w x y z 0 1 2 3 4 5 6 7 8 9 A B C D E F G H I J K L M N O P Q R S T U V W X Y Z ! @ # $ % ^ & * ( ) - _ = + [ ] { } / | ; : , . < > ? ~'
    temp = temp.split(" ")
    temp.extend([" ", "'", '"'])

    msg = message[::-1]
    rotified = ""
    for ch in msg:
        if(ch in temp):
            rotified = rotified + rotated[temp.index(ch)]
        elif(ch=='\n'):
            rotified = rotified + "`"
        else:
            rotified = rotified + ch


    return rotified

def MediumEncrpyt_Method(message, key):
    result = ""
    message_len = len(message)
    rotateBy = list()
    random_seed = set_random_seed(key)
    rotateBy = random_seed.randint(0, 9900, message_len)
    mess_int = string_to_list(message)
    mess_int = np.array(mess_int)
    resultant_sum = mess_int + rotateBy
    for i in resultant_sum:
        result = result+"{:04d}".format(i)
    return result
        
def set_random_seed(key):
    vocab = dict()
    seed_tobe_set = ""
    corpus = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()-_=+[]'
    corpus = corpus + "{"
    corpus = corpus + '}/|;:,.<>?~ `'
    corpus = corpus + "'"
    corpus = corpus + '"'
    for index, i in enumerate(corpus):
        vocab[i] = index
    for i in key.lower():
        seed_tobe_set = seed_tobe_set + str(vocab[i])
    random_seed = np.random.RandomState(int(seed_tobe_set)%((2**32)-2))
    return random_seed

def string_to_list(string):
    char_list = list()
    vocab = dict()
    for char in string:
        char_list.append(char)
    temp = 'a b c d e f g h i j k l m n o p q r s t u v w x y z 0 1 2 3 4 5 6 7 8 9 A B C D E F G H I J K L M N O P Q R S T U V W X Y Z ! @ # $ % ^ & * ( ) - _ = + [ ] { } / | ; : , . < > ? ~'
    temp = temp.split(" ")
    temp.extend([" ", "`", "'", '"', "\n"])
    for key,value in enumerate(temp):
        vocab[value] = key
    char_to_int = list(map(lambda x:vocab[x], char_list))
    return char_to_int

def hard_encrypt(message, key):
    message_noNextLine = ""

    for ch in message:
        if ch=='\n':
            message_noNextLine = message_noNextLine + '`'
        else:
            message_noNextLine = message_noNextLine + ch

    msg_part1, msg_part2 = splitMessage(message_noNextLine)
    key_part1, key_part2 = splitMessage(key)

    print(key_part1)
    print(key_part2)

    encrpyted_part1 = easyMethod_Rotate(msg_part1, key_part1)
    encrpyted_part2 = MediumEncrpyt_Method(msg_part2, key_part2)

    print(msg_part1)
    print(encrpyted_part1)
    print(msg_part2)
    print(encrpyted_part2)

    encrpyted_message = ""

    for ch in encrpyted_part1:
        if isValid(ch):
            encrpyted_message = encrpyted_message + ourDict[ch]
        else:
            encrpyted_message = encrpyted_message + ch

    # encrpyted_message = encrpyted_message + " break "

    for ch in encrpyted_part2:
        if(isValid(ch)):
            encrpyted_message = encrpyted_message + ourDict[ch]
        else:
            encrpyted_message = encrpyted_message + ch

    return encrpyted_message

print(hard_encrypt("My\n'name' is GauRav \"Goyal\",\nI am 20 years old!","teraBaap"))