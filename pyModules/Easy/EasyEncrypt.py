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

    temp = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()<>?+-_/ ,.'
    rotated = rotateHere(temp, rotTimes)
    temp = 'a b c d e f g h i j k l m n o p q r s t u v w x y z 0 1 2 3 4 5 6 7 8 9 A B C D E F G H I J K L M N O P Q R S T U V W X Y Z ! @ # $ % ^ & * ( ) < > ? + - _ /'
    temp = temp.split(" ")
    temp.extend([" ", ",", "."])
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
