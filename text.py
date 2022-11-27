import sys
import getpass
import game_map
import titles
import locations
from os import system
from time import sleep
CURSOR_UP_ONE = '\x1b[1A'
ERASE_LINE = '\x1b[2K'
inventory = {}
lastkey = 'start'
prelastkey = 'start'
localname = ''
a_update = 0
prechoice = 0




def inv(location = False):
    global inventory, lastkey, prelastkey, localname
    print('Ваш инвентарь: ')
    for k, v in inventory.items():
        print(f'-- {k}: {v}\n')
    getpass.getpass(prompt='')
    system('clear')
    if location: locations.choose_location()
    else:
        database(lastkey,f=False)
        choice = input()
        print(CURSOR_UP_ONE, end="")
        database(choice=choice)
    


def database(key='', name='', choice=0, f=True, inven = {}, location=False):
    global lastkey, prelastkey, localname, inventory, a_update
    if name != '':
        localname = name
    if inven:
        inventory |= inven
    a = {}
    if a_update == 0:
        #a[0] = 'name'
        a[1] = 'house_1'
        a[2] = 'house_2'
        if choice == '1': partner = False
        if choice == '2': partner = True
    if a_update == 1:
        a[1] = locations.square(localname)
        a[2] = locations.playground(localname)
        a[3] = locations.dark_corner(localname)
        a[4] = locations.old_square(localname,partner)
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
        'house_2': '''Фрод: Да как так то...*''',
        'note_': '''Фрод: У меня есть записка, которая может тебе помочь в расследовании и лупа, держи*
Получено: записка, лупа*\n'''
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
        if location:
            if choice == '\x18':
                print('true')
                inv(location=True)
                return 0
            if choice == '\x1b':
                exit()
            if prechoice != 0:
                game_map.char(int(prechoice))
            else: game_map.char(0)
            for i in range(2): game_map.char(int(choice))
            titles.choose_title(choice)
            a[int(choice)]()
        else:
            if choice == '\x18':
                inv()
                return 0
            if choice == '\x1b':
                exit() 
            for i in d[a[int(choice)]]:
                if i != "*":
                    sleep(0.033)
                    sys.stdout.write(i)
                    sys.stdout.flush()
                else:
                    getpass.getpass(prompt='')
            a_update += 1
