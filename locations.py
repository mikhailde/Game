import text
import sys
import getpass
import titles
import game_map
from time import sleep
from os import system
from sys import platform
if platform == 'linux': clr = 'clear'
if platform == 'win32': clr = 'cls'
CURSOR_UP_ONE = '\x1b[1A'
ERASE_LINE = '\x1b[2K'
partner = False
nun = False
keys = False
localname = ''
inventory = {}
location = '0'


def output(text):
    for i in text:
        if i != "*":
            sleep(0.033)
            sys.stdout.write(i)
            sys.stdout.flush()
        else:
            getpass.getpass(prompt='')
            print(CURSOR_UP_ONE, end="")

def error():
    output('Неверный ввод, попробуйте еще раз*')
    print(ERASE_LINE, CURSOR_UP_ONE, ERASE_LINE, end='')

def choose_location(name='',part = '',inv = {}):
    global localname, partner, inventory, location
    if part != '': partner = part
    if name != '': localname = name
    if inv: inventory |= inv
    a = {
        '1': square,
        '2': playground,
        '3': dark_corner,
        '4': old_square,
    }
    system(clr)
    print('''Выберите действие:
[1] Перейти на главную площадь
[2] Перейти на детскую площадку
[3] Перейти на тёмный угол за каким-то клубом
[4] Перейти на старая площадь, которая уже заросла

Просмотреть инвентарь (Ctrl+X)
Выйти из игры (ESC)''')
    choice = input()
    while choice not in ['1','2','3','4','\x18','\x1b']:
        error()
        choice = input()
    print(CURSOR_UP_ONE)
    if choice == '\x18': text.inv(inventory)
    elif choice == '\x1b': exit()
    else:
        game_map.char(location)
        for i in range(2): game_map.char(choice)
        location = choice
        a[choice]()
    system(clr)
    
def square():
    titles.square()
    system(clr)
    if nun == False and keys == False:
        output('Тут нечего делать*')
        system(clr)
        choose_location()

def playground():
    titles.playground()
    system(clr)
    d = {}
    if nun == False and keys == False:
        output('Тут нечего делать*')
        system(clr)
        choose_location()
    #else:
    #    output(d['text'])

def dark_corner():
    global localname, partner, nun, keys, inventory
    titles.dark_corner()
    system(clr)
    d = {
        'text': f'''В далеке виднеется магазин*
{localname}: "совершенно случайно заметил в круглой тьме яркий огонёк, тлеющей сигареты"*
{localname}: Ага! Ещё один свидетель!*
Продавщица: Чертила, я не буду так просто тебе давать показания. Ты вылез из ниоткуда и уже стал детективом.*
''',
    'choice_1': '''Выберите действие:
[1] Отправить своего помощника с ней поговорить
[2] Пойти самому
''',

    'choice_2': '''Выберите действие:
[1] Пойти самому
''',
    'result_1': '''Фрот: Ты мне конечно друг, но твоё исследование дорого стоит - целая пачка сигарет!*
Грабёж! Но всё-таки! Я нашёл кое-что стоящее!!!*
''',
    'choice_2_1': '''Выберите действие:
[1] Предложить что-то взамен на информацию
''',
    'result_2_1':f'''{localname}: Ну… Могу свою лупу дать взамен на вашу информацию!*
Конечно бесполезный обмен, ибо я даже не знаю что у вас, но в какой-то мере он логичный!* 
"Детектив улыбнулся во все 32 зуба, дабы показать свои добрые намерения (плохо выходит)"* 
Продавщица: " скептически уже осмотрела лупу, а потом детектива " Ладно, ты не глупый.*
Держи ключи, они остались от квартиры того светловолосого парня*
''',
    'success': '''Вы получили ключи с брелком*
''',
    'success_2': '''Вы получили ключи с брелком но потеряли лупу*
'''
    }
    if nun == False:
        output('Тут нечего делать*')
        system(clr)
        choose_location()

    else:
        output(d['text'])
        if partner: output(d['choice_1'])
        else: output(d['choice_2'])
        choice = input()
        while choice not in ['1','2']:
            error()
            choice = input()
        print(CURSOR_UP_ONE, end="")
        if partner and choice == '1':
            output(d['result_1'])
            output(d['success'])
            inventory |= {'Ключи с брелком': 'На брелке надпись "гримёрка"'}
            keys = True
            choose_location()
        elif partner and choice == '2' or choice == '1':
            output(d['choice_2_1'])
            choice = input()
            while choice != '1':
                error()
                choice = input()
            print(CURSOR_UP_ONE, end="")
            if choice == '1':
                output(d['result_2_1'])
                output(d['success_2'])
                del inventory['Лупа']
                inventory |= {'Ключи с брелком': 'На брелке надпись "гримёрка"'}
                keys = True
                choose_location()
    
def old_square():
    global localname, partner, nun
    titles.old_square()
    system(clr)
    d = {
    'text':  f'''Вы встретили монашку*
{localname}: Хэээй!*
Монашка: АААА– ЗАБИРАЙ ЧТО УГОДНО, НО МЕНЯ НЕ ТРОГАЙ*
Тут от монашки и след простыл*
''',

    'choice_1': '''Выберите действие:
[1] Отправить своего помощника с ней поговорить
[2] Пойти самому
''',

    'choice_2': '''Выберите действие:
[1] Пойти самому
''',

    'result_1': '''Фрод: Короче. Я с ней всё обсудил. Ну ты её и напугал до чёртиков! Всё выдала! Ну слушай.*
В деревню приплёлся ещё какой-то светловолосый парень, как она упомянула - певец на нашем концерте тут.*
Ну веет от него таким же вайбом, как у тебя, чёртик*
''',

    'choice_2_1': '''Выберите действие:
[1] Надавить на неё
[2] Спокойно всё обсудить
''',

    'result_2_1_1': f'''{localname}: Слушай, если ты сейчас же не выдашь мне информацию о чём либо, я тебя лично сдам в руки тому вору, чтобы из тебя сделали куклу!*
Монашка: "дрожит как кленовый лист и смотрит куда угодно, но никак не на детектива, а потом вовсе убежит от вас, не издав и звука"*
''',

    'result_2_1_2': f'''{localname}: Я не причиню тебе вреда и не сделаю плохо. Просто расскажи что ты знаешь. Это очень нам поможет в деле.*
Монашка: "всё-таки посмотрела на детектива"*
Ну после вас сюда приехал ещё один человек…*
Он со светлыми волосами, с таким же готическим стилем и он вроде певец у нас на концерте…*
''',
    'success': 'Вы получили необходимую информацию*',
    'failure': 'Вы не смогли получить необходимую информацию*'
}
    output(d['text'])
    if partner: output(d['choice_1'])
    else: output(d['choice_2'])
    choice = input()
    while choice not in ['1','2']:
        error()
        choice = input()
    print(CURSOR_UP_ONE, end="")
    if partner and choice == '1':
        output(d['result_1'])
        output(d['success'])
        nun = True
        choose_location()
    elif partner and choice == '2' or choice == '1':
        output(d['choice_2_1'])
        choice = input()
        while choice not in ['1','2']:
            error()
            choice = input()
        print(CURSOR_UP_ONE, end="")
        if choice == '1':
            output(d['result_2_1_1'])
            output(d['failure'])
            choose_location()
        if choice == '2':
            output(d['result_2_1_2'])
            output(d['success'])
            nun = True
            choose_location()
