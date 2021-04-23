import numpy as np

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