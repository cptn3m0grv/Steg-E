import numpy as np

def MediumEncrpyt_Method(message, key):
    message_len = len(message)
    rotateBy = list()
    random_seed = set_random_seed(key)
    for i in range(message_len):
        rotateBy.append(random_seed.rand())
    rotateBy = np.array(rotateBy)
    print(rotateBy)
        


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

MediumEncrpyt_Method("Gargeya","gagi")