import numpy as np
import textwrap as tw

def MediumEncrpyt_Method(message, key):
    result = ""
    message_len = len(message)
    rotateBy = list()
    random_seed = set_random_seed(key)
    rotateBy = random_seed.randint(0, 9900, message_len)
    # print(rotateBy)
    mess_int = string_to_list(message)
    mess_int = np.array(mess_int)
    # print(mess_int[0], type(mess_int[0]))
    resultant_sum = mess_int + rotateBy
    # print(resultant_sum.shape)
    # print(resultant_sum[0])
    for i in resultant_sum:
        # print("{:04d}".format(i))
        result = result+"{:04d}".format(i)
    return result
        

def set_random_seed(key):
    vocab = dict()
    seed_tobe_set = ""
    corpus = 'abcdefghijklmnopqrstuvwxyz0123456789'
    for index, i in enumerate(corpus):
        vocab[i] = index
    for i in key.lower():
        seed_tobe_set = seed_tobe_set + str(vocab[i])
    random_seed = np.random.RandomState(int(seed_tobe_set))
    return random_seed


def string_to_list(string):
    char_list = list()
    vocab = dict()
    for char in string:
        char_list.append(char)
    temp = 'a b c d e f g h i j k l m n o p q r s t u v w x y z 0 1 2 3 4 5 6 7 8 9 A B C D E F G H I J K L M N O P Q R S T U V W X Y Z ! @ # $ % ^ & * ( ) < > ? + - _ /'
    temp = temp.split(" ")
    temp.extend([" ", ",", ".", '\n', "'"])
    for key,value in enumerate(temp):
        vocab[value] = key
    # print(char_list)
    char_to_int = list(map(lambda x:vocab[x], char_list))
    return char_to_int

# string_to_list("Gargeya Sharma")

with open("src/msg.txt", 'r') as file:
    message_string = file.read()

after = MediumEncrpyt_Method(message_string ,"gagi")


### DECRYPTION 

def MediumDecrypt_Method(en_message, key):
    en_list = tw.wrap(en_message, 4)
    # print(en_list)
    random_seed = set_random_seed(key)
    rotateBy = random_seed.randint(0, 9900, len(en_list))
    en_list = np.array(en_list, dtype=np.int)
    decrpyted_list = en_list - rotateBy
    vocab = dict()
    temp = 'a b c d e f g h i j k l m n o p q r s t u v w x y z 0 1 2 3 4 5 6 7 8 9 A B C D E F G H I J K L M N O P Q R S T U V W X Y Z ! @ # $ % ^ & * ( ) < > ? + - _ /'
    temp = temp.split(" ")
    temp.extend([" ", ",", ".", '\n', "'"])
    for key,value in enumerate(temp):
        vocab[key] = value
    int_to_char = list(map(lambda x:vocab[x], decrpyted_list))
    result = "".join(int_to_char)
    return result


print(MediumDecrypt_Method(after, "gagi"))
