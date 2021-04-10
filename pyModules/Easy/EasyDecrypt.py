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
