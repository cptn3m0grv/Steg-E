import numpy as np
import textwrap as tw

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
