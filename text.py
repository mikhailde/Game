import sys
import getpass
from os import system
from time import sleep
CURSOR_UP_ONE = '\x1b[1A'
ERASE_LINE = '\x1b[2K'
inventory = ['123', '321']
lastkey = 'start'
prelastkey = 'start'
localname = ''


def inv():
    global inventory, lastkey, prelastkey, localname
    print('Ваш инвентарь: ')
    for i in inventory:
        print(i)
    getpass.getpass(prompt='')
    system('clear')
    database(prelastkey, name=localname, f=False)
    database(lastkey, f=False)
    choice = input()
    print(CURSOR_UP_ONE)
    database(choice=choice)


def database(key='', name='', choice=0, f=True):
    global lastkey, prelastkey, localname
    if name != '':
        localname = name
    a = {0: 'name', 1: 'house_1', 2: 'house_2'}
    d = {
        'start': '''В богом забытой деревушке, несущая название “bloody valley” завёлся необычный житель.*
Его волосы цвета угля, его готический стиль, да и эта бледная кожа! Брр!*
Однако не только внешний вид этого “чертилы” пугал жителей деревни.*
Спустя какое-то время из деревни начали пропадать молодые люди.*
Ох какая же прелесть что новый житель деревни (тот самый “чертила”) оказался детективом.*
Кто бы мог подумать что именно он будет искать того самого вора, который каждую ночь спокойно крадет людей из деревни.*
В которой итак мало людей!*
''',
        'name': 'Введите свое имя: ',
        'house': f'''Вы обнаруживате старого знакомого*
{name}: Итааак! Я нашёл себе работу в этой глуши!*
Фрод: И тебе привет, {name}! Что ты там нашел?*
{name}: Я нынешний детектив этой глуши!*
''',
        'choice_1': '''Выберите действие:
[1] Только не мешайся мне под ногами, хорошо???
[2] И ты мой помощник в этом деле!
''',
        'house_1': '''Фрод: Да как так то...*''',
        'house_2': '''Фрод: Да как так то...*'''
    }
    flag = True
    for i in ['name', '_']:
        if i in key or key == '':
            flag = False
    if flag:
        system('clear')
    if choice == 0:
        for i in d[key]:
            if i != "*":
                sleep(0.033)
                sys.stdout.write(i)
                sys.stdout.flush()
            else:
                getpass.getpass(prompt='')
                print(CURSOR_UP_ONE, end="")
        if f:
            prelastkey = lastkey
            lastkey = key
    else:
        if choice == '\x18':
            inv()
        else:
            for i in d[a[int(choice)]]:
                if i != "*":
                    sleep(0.033)
                    sys.stdout.write(i)
                    sys.stdout.flush()
                else:
                    getpass.getpass(prompt='')
                    print(CURSOR_UP_ONE, end="")
