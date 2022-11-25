import text
import sys
import getpass
from time import sleep
from os import system
nun = False


def square():
    if nun == False:
        for i in 'Тут нечего делать*':
                if i != "*":
                    sleep(0.033)
                    sys.stdout.write(i)
                    sys.stdout.flush()
                else:
                    getpass.getpass(prompt='')
        system('clear')
        text.choose_location()
def playground():
    if nun == False:
        for i in 'Тут нечего делать*':
                if i != "*":
                    sleep(0.033)
                    sys.stdout.write(i)
                    sys.stdout.flush()
                else:
                    getpass.getpass(prompt='')
        system('clear')
        text.choose_location()
def dark_corner():
    if nun == False:
        for i in 'Тут нечего делать*':
                if i != "*":
                    sleep(0.033)
                    sys.stdout.write(i)
                    sys.stdout.flush()
                else:
                    getpass.getpass(prompt='')
        system('clear')
        text.choose_location()
def old_square():
    print('Вы встретили монашку')