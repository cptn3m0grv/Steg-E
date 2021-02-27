import click
import getpass
import os
import sys

# description = "\tTo hide a message in a file:\n\t\tpython code.py encrypt --src SOURCE_FILE --msg MESSAGE_FILE --tgt PATH_WHERE_RESULT_IS_SAVED\n\tTo retrieve the hidden message from file:\n\t\tpython code.py decrypt --tgt TARGET_FILE_LOCATION\n"

@click.command()
@click.option('--encrypt', is_flag=True, default=False)
@click.option('--decrypt', is_flag=True, default=False)
@click.option('--src', default=".",help='Enter the location of source file')
@click.option('--msg', default=".",help="Enter the message to hide")
@click.option('--tgt', default=".",help="Location to save the result")


def check(encrypt, src, msg, tgt, decrypt):
    """\tTo hide a message in a file:\n\n\t\tpython code.py encrypt --src SOURCE_FILE --msg MESSAGE_FILE --tgt PATH_OF_FILE_SAVED\n\n\tTo retrieve the hidden message from file:\n\n\t\tpython code.py decrypt --tgt TARGET_FILE_LOCATION\n"""

    ssss = ' '
    flag = ' '
    if(encrypt and  not decrypt):
        print(str(sys.platform))
        ll = tgt
        flag = 'encrypt'
    elif(decrypt and not encrypt):
        print("decrypt working")
        flag = 'decrypt'
    else:
        print("Rerun the program using right arguments")

    if(flag=='encrypt'):
        chlo(src, msg, tgt)
    elif(flag=='decrypt'):
        olhc(tgt)


def chlo(src, msg, tgt):
    pkmkbl = []

    with open(src, 'rb') as pkmkb:
        pkmkbl = pkmkb.readlines()

    with open(msg, 'rb') as ll:
        pkmkbl.extend(ll.readlines())

    with open(tgt, 'wb') as lll:
        for s in pkmkbl:
            lll.write(s)

    # print(pkmkbl)

def olhc(tgt):
    with open(tgt, 'rb') as lll:
        print(lll.readlines()[-1])

check()