import numpy as np
import textwrap as tw

ourDict = {
    "a": "ஓ",
    "b": "ఇ",
    "c": "ग",
    "d": "傷",
    "e": "捥",
    "f": "䆇",
    "g": "᧮",
    "h": "θ",
    "i": "Я",
    "j": "∑",
    "k": "ב",
    "l": "ꌓ",
    "m": "ꋌ",
    "n": "Ў",
    "o": "Ҫ",
    "p": "Ĭ",
    "q": "؊",
    "r": "ǿ",
    "s": "ڭ",
    "t": "ࢯ",
    "u": "ݟ",
    "v": "ᴓ",
    "w": "₷",
    "x": "שּ",
    "y": "ﭧ",
    "z": "ﭲ",
    "A": "ﾛ",
    "B": "ﾙ",
    "C": "ﾖ",
    "D": "ﾔ",
    "E": "ﾒ",
    "F": "ﾐ",
    "G": "ﾎ",
    "H": "ﾋ",
    "I": "ﾈ",
    "J": "ﾇ",
    "K": "ﾂ",
    "L": "ﾀ",
    "M": "ｽ",
    "N": "ｻ",
    "O": "舘",
    "P": "頻",
    "Q": "辶",
    "R": "3",
    "S": "艹",
    "T": "者",
    "U": "爫",
    "V": "漢",
    "W": "兀",
    "X": "立",
    "Y": "淋",
    "Z": "藺",
    "1": "B",
    "2": "理",
    "3": "李",
    "4": "m",
    "5": "隆",
    "6": "栗",
    "7": "律",
    "8": "戮",
    "9": "T",
    "0": "颪",
    "!": "坭",
    "@": "≠",
    "#": "◊",
    "$": "Ω",
    "%": "‡",
    "^": "Õ",
    "&": "÷",
    "*": "ê",
    "(": "Ã",
    ")": "Å",
    "-": "®",
    "_": "¤",
    "=": "§",
    "+": "©",
    "[": "¯",
    "]": "Ë",
    "{": "¢",
    "}": "ß",  
    "/": "Š",
    "|": "∞",
    ";": "Œ",
    ":": "Ü",
    ",": "Ž",
    ".": "Ð",
    "<": "¨",
    ">": "™",
    "?": "￦",
    "~": "｠",
    " ": "Θ",
    "`": "`",
    "'": "A",
    '"': "0"
}

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

def reverseRotateHere(temp, rotTimes):
    n = len(temp)
    rotTimes = (n-rotTimes)%n
    resultL = temp[0:rotTimes]
    resultL = resultL[::-1]
    resultR = temp[rotTimes:n]
    resultR = resultR[::-1] 

    result = resultL + resultR
    result = result[::-1]
    return result

def easyMethod_Decrypt(message, tulsi):

    rotTimes = 0
    idx = 1

    for chAt in tulsi:
        rotTimes = rotTimes + (ord(chAt)*idx)
        idx += 1

    temp = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()-_=+[]'
    temp = temp + "{"
    temp = temp + '}/|;:,.<>?~ '
    temp = temp + "'"
    temp = temp + '"'

    rotated = reverseRotateHere(temp, rotTimes)

    temp = 'a b c d e f g h i j k l m n o p q r s t u v w x y z 0 1 2 3 4 5 6 7 8 9 A B C D E F G H I J K L M N O P Q R S T U V W X Y Z ! @ # $ % ^ & * ( ) - _ = + [ ] { } / | ; : , . < > ? ~'
    temp = temp.split(" ")
    temp.extend([" ", "'", '"'])

    msg = message
    msg = msg[::-1] ## Reversing the message string
    rotified = ""
    for ch in msg:
        if(ch in temp):
            rotified = rotified + rotated[temp.index(ch)]
        elif(ch=="`"):
            rotified = rotified + "\n"
        else:
            rotified = rotified + ch


    return rotified

def MediumDecrypt_Method(en_message, key):
    en_list = tw.wrap(en_message, 4)
    # print(en_list)
    random_seed = set_random_seed(key)
    rotateBy = random_seed.randint(0, 9900, len(en_list))
    en_list = np.array(en_list, dtype=np.int)
    decrpyted_list = en_list - rotateBy
    vocab = dict()
    temp = 'a b c d e f g h i j k l m n o p q r s t u v w x y z 0 1 2 3 4 5 6 7 8 9 A B C D E F G H I J K L M N O P Q R S T U V W X Y Z ! @ # $ % ^ & * ( ) - _ = + [ ] { } / | ; : , . < > ? ~'
    temp = temp.split(" ")
    temp.extend([" ", "`", "'", '"', "\n"])
    for key,value in enumerate(temp):
        vocab[key] = value
    int_to_char = list(map(lambda x:vocab[x], decrpyted_list))
    result = "".join(int_to_char)
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

def hard_decrypt(message, key1):

    customDecryptDict = dict()

    for key, value in ourDict.items():
        customDecryptDict[value] = key

    cl = list(customDecryptDict.keys())

    actual_message = ""

    for ch in message:
        if(ch in cl):
            actual_message = actual_message + customDecryptDict[ch]
        else:
            actual_message = actual_message + ch

    message = actual_message

    part1, part2 = message.split("Z")
    
    key_part1, key_part2 = splitMessage(key1)

    decrypted_part1 = easyMethod_Decrypt(part1, key_part1)
    decrypted_part2 = MediumDecrypt_Method(part2, key_part2)

    decrypted_part1 = decrypted_part1.replace("`", "\n")
    decrypted_part2 = decrypted_part2.replace("`", "\n")

    return (decrypted_part1 + decrypted_part2)
