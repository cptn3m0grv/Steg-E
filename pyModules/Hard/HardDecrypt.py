import numpy as np
import textwrap as tw

from EasyDecrypt import *
from MediumDecrypt import *

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


def reverseRotateTimeStamp(eachChar, eachRotateTime):
    temp = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()-_=+[]'
    temp = temp + "{"
    temp = temp + '}/|;:,.<>?~ '
    temp = temp + "'"
    temp = temp + '"'

    if eachChar == '`':
        return '`'

    idx_to_rotate = 12321321321321

    for i in range(0, len(temp)):
        if(temp[i]==eachChar):
            idx_to_rotate = i
            break

    return temp[idx_to_rotate - eachRotateTime]

def applyTimeStamp(somethingToDecryptTrim, timestampTrim):
    encrL = ""
    for i in range(0, len(somethingToDecryptTrim)):
        encrL = encrL + reverseRotateTimeStamp(somethingToDecryptTrim[i], int(timestampTrim[i]))
    
    return encrL

def reverseTimeStamp(somethingToDecrypt, timestamp):
    final = ""
    j = 0
    for i in range(0, len(somethingToDecrypt)//len(timestamp)):
        final = final + applyTimeStamp(somethingToDecrypt[j:j+len(timestamp)], timestamp)
        j = j + len(timestamp)

    rem = len(somethingToDecrypt)%len(timestamp)
    if(rem>0):
        rem_str = somethingToDecrypt[-1*(rem):]
        trimmed_timeStamp = timestamp[0:rem]
        final = final + applyTimeStamp(rem_str, trimmed_timeStamp)

    return final

def hard_decrypt(message, key1):

    customDecryptDict = dict()

    for key, value in ourDict.items():
        customDecryptDict[value] = key

    cl = list(customDecryptDict.keys())

    part1, part2, timeStamp = message.split("Z")
    easy_len = len(part1)
    med_len = len(part2)

    key_part1, key_part2 = splitMessage(key1)

    actual_message = ""

    for ch in part1:
        if(ch in cl):
            actual_message = actual_message + customDecryptDict[ch]
        else:
            actual_message = actual_message + ch

    for ch in part2:
        if(ch in cl):
            actual_message = actual_message + customDecryptDict[ch]
        else:
            actual_message = actual_message + ch

    timestamp = ""

    for ch in timeStamp:
        if(ch in cl):
            timestamp = timestamp + customDecryptDict[ch]
        else:
            timestamp = timestamp + ch
    
    toDecrypt = reverseTimeStamp(actual_message, timestamp)

    decrypted_part1 = easyMethod_Decrypt(toDecrypt[0:easy_len], key_part1)
    decrypted_part2 = MediumDecrypt_Method(toDecrypt[easy_len:], key_part2)

    decrypted_part1 = decrypted_part1.replace("`", "\n")
    decrypted_part2 = decrypted_part2.replace("`", "\n")

    return (decrypted_part1 + decrypted_part2)