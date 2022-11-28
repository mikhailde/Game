import sys
import getpass
import locations
from time import sleep
from os import system
CURSOR_UP_ONE = '\x1b[1A'
ERASE_LINE = '\x1b[2K'
inventory = {}
localname = ''
partner = False


def output(text):
    for i in text:
        if i != "*":
            sleep(0.033)
            sys.stdout.write(i)
            sys.stdout.flush()
        else:
            getpass.getpass(prompt='')
            print(CURSOR_UP_ONE, end="")

def inv():
    global inventory, localname, partner
    print('Ваш инвентарь: ')
    for k, v in inventory.items(): print(f'-- {k}: {v}\n')
    getpass.getpass(prompt='')
    for i in range(len(inventory)): print(CURSOR_UP_ONE, ERASE_LINE)
    locations.choose_location(localname, partner)


def database(key='', name = '', choice=0, inven = {}):
    global localname, inventory, partner
    if name != '': localname = name
    a = {
        '1': 'result-1',
        '2': 'result-2'
    }
    text = {
        'start_': '''В богом забытой деревушке, несущая название “bloody valley” завёлся необычный житель.*
Его волосы цвета угля, его готический стиль, да и эта бледная кожа! Брр!*
Однако не только внешний вид этого “чертилы” пугал жителей деревни.*
Спустя какое-то время из деревни начали пропадать молодые люди.*
Ох какая же прелесть что новый житель деревни (тот самый “чертила”) оказался детективом.*
Кто бы мог подумать что именно он будет искать того самого вора, который каждую ночь спокойно крадет людей из деревни.*
В которой итак мало людей!*''',
    'name_': 'Введите свое имя: ',
    'house': f'''Вы обнаруживате старого знакомого*
{localname}: Итааак! Я нашёл себе работу в этой глуши!*
Фрод: И тебе привет, {localname}! Что ты там нашел?*
{localname}: Я нынешний детектив этой глуши!*
''',
    'choice-1': '''Выберите действие:
[1] Только не мешайся мне под ногами, хорошо???
[2] И ты мой помощник в этом деле!
''',
    'result-1': f'''{CURSOR_UP_ONE}Фрод: Да как так то...*
''',
    'result-2': f'''{CURSOR_UP_ONE}Фрод: Да как так то...*
''',
    'note': '''Фрод: У меня есть записка, которая может тебе помочь в расследовании и лупа, держи*
Получено: записка, лупа*'''
    }
    if inv: inventory |= inven
    flag = False
    if '_' in key: flag = True
    if flag: system('clear')
    if choice == 0: output(text[key])
    else:
        if choice == '1': partner = False
        if choice == '2': partner = True
        if choice == '\x18': inv()
        if choice == '\x1b': exit()
        else: output(text[a[choice]])
