customDict = {
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
}

msg = input("Kuch enter to krdo: ")
new_msg = ""

for ch in msg:
    if ord(ch)>=97 and ord(ch)<=122:
        new_msg = new_msg + customDict[ch]
    else:
        new_msg = new_msg + ch

print(new_msg)

# for lll in l:
#     print(len(lll.encode('utf-16')), end=" ")

customDecryptDict = dict()

for key, value in customDict.items():
    customDecryptDict[value] = key

cl = list(customDecryptDict.keys())

msg = ""
for ch in new_msg:
    if ch in cl:
        msg = msg + customDecryptDict[ch]
    else:
        msg = msg + ch

print(msg)

print(new_msg.encode('utf-16'))
love = new_msg.encode('utf-16')
print(love.decode('utf-16'))

salt = "$3|\|!)|\|U!)3$"