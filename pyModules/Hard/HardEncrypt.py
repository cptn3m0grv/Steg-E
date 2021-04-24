import numpy as np
import datetime
from EasyEncrypt import *
from MediumEncrypt import *

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


def rotateTimeStamp(eachChar, eachRotateTime):
    temp = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()-_=+[]'
    temp = temp + "{"
    temp = temp + '}/|;:,.<>?~ '
    temp = temp + "'"
    temp = temp + '"'

    if(eachChar == '`'):
        return '`'

    idx_to_rotate = -1

    for i in range(0, len(temp)):
        if(temp[i]==eachChar):
            idx_to_rotate = i
            break

    if(idx_to_rotate + eachRotateTime >= len(temp)):
        rotatedChar = temp[idx_to_rotate + eachRotateTime - len(temp)]
        return rotatedChar

    return temp[idx_to_rotate + eachRotateTime]

def applyTimeStamp(textToEncryptTrim, timeStampStr):
    encrL = ""
    for i in range(0, len(textToEncryptTrim)):
        encrL = encrL + rotateTimeStamp(textToEncryptTrim[i], int(timeStampStr[i]))
    
    return encrL

def timeRotate(textToEncrypt):
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    date = datetime.datetime.now().day
    hour = datetime.datetime.now().hour
    minute = datetime.datetime.now().minute
    seconds = datetime.datetime.now().second

    timeStamp = str(year)+str(month)+str(date)+str(hour)+str(minute)+str(seconds)

    final = ""
    j = 0
    for i in range(0, len(textToEncrypt)//len(timeStamp)):
        final = final + applyTimeStamp(textToEncrypt[j:j+len(timeStamp)], timeStamp)
        j = j + len(timeStamp)

    rem = len(textToEncrypt)%len(timeStamp)
    if(rem>0):
        rem_str = textToEncrypt[-1*(rem):]
        trimmed_timeStamp = timeStamp[0:rem]
        final = final + applyTimeStamp(rem_str, trimmed_timeStamp)

    return final, timeStamp

def hard_encrypt(message, key):
    message_noNextLine = ""

    for ch in message:
        if ch=='\n':
            message_noNextLine = message_noNextLine + '`'
        else:
            message_noNextLine = message_noNextLine + ch

    msg_part1, msg_part2 = splitMessage(message_noNextLine)
    key_part1, key_part2 = splitMessage(key)

    encrpyted_part1 = easyMethod_Rotate(msg_part1, key_part1)
    encrpyted_part2 = MediumEncrpyt_Method(msg_part2, key_part2)

    len_easy = len(encrpyted_part1)
    len_med = len(encrpyted_part2)
    concatParts = encrpyted_part1 + encrpyted_part2
    
    time_encr, currTime = timeRotate(concatParts)
    encrpyted_part1 = time_encr[0:len_easy]
    encrpyted_part2 = time_encr[len_easy:]

    encrpyted_message = ""

    for ch in encrpyted_part1:
        if isValid(ch):
            encrpyted_message = encrpyted_message + ourDict[ch]
        else:
            encrpyted_message = encrpyted_message + ch

    encrpyted_message = encrpyted_message + "Z"

    for ch in encrpyted_part2:
        if(isValid(ch)):
            encrpyted_message = encrpyted_message + ourDict[ch]
        else:
            encrpyted_message = encrpyted_message + ch

    encrpyted_message = encrpyted_message + "Z"

    for ch in currTime:
        if(isValid(ch)):
            encrpyted_message = encrpyted_message + ourDict[ch]
        else:
            encrpyted_message = encrpyted_message + ch

    return encrpyted_message