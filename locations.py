import text
import sys
import getpass
import titles
from time import sleep
from os import system
CURSOR_UP_ONE = '\x1b[1A'
partner = False
nun = False
localname = ''


def choose_location(name='',part = ''):
    global localname, partner
    if part != '': partner = part
    if name != '': localname = name
    a = {
        '1': square,
        '2': playground,
        '3': dark_corner,
        '4': old_square,
    }
    system('clear')
    print('''Выберите действие:
[1] Перейти на главную площадь
[2] Перейти на детскую площадку
[3] Перейти на тёмный угол за каким-то клубом
[4] Перейти на старая площадь, которая уже заросла

Просмотреть инвентарь (Ctrl+X)
Выйти из игры (ESC)''')
    choice = input()
    print(CURSOR_UP_ONE)
    if choice == '\x18': text.inv()
    elif choice == '\x1b': exit()
    else: a[choice]()


def output(text):
    for i in text:
        if i != "*":
            sleep(0.033)
            sys.stdout.write(i)
            sys.stdout.flush()
        else:
            getpass.getpass(prompt='')
            print(CURSOR_UP_ONE, end="")

def square():
    titles.square()
    system('clear')
    if nun == False:
        output('Тут нечего делать*')
        system('clear')
        choose_location()

def playground():
    titles.playground()
    system('clear')
    if nun == False:
        output('Тут нечего делать*')
        system('clear')
        choose_location()

def dark_corner():
    titles.dark_corner()
    system('clear')
    if nun == False:
        output('Тут нечего делать*')
        system('clear')
        choose_location()
    
def old_square():
    global localname, partner
    titles.old_square()
    system('clear')
    a = {}
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

    'result_1': '''Фрод: Короче. Я с ней всё обсудил. Ну ты её и напугал до чёртиков! Всё выдала! Ну слушай.
В деревню приплёлся ещё какой-то светловолосый парень, как она упомянула - певец на нашем концерте тут.
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
    'success': 'Вы получили необходимую информацию',
    'failure': 'Вы не смогли получить необходимую информацию'
}
    output(d['text'])
    if partner: output(d['choice_1'])
    else: output(d['choice_2'])
    choice = input()
    if partner and choice == '1':
        output(d['result_1'])
        output(d['success'])
        nun = True
        choose_location()
    elif partner and choice == '2' or choice == '1':
        output(d['choice_2_1'])
        choice = input()
        if choice == '1':
            output(d['result_2_1_1'])
            output(d['failure'])
            choose_location()
        if choice == '2':
            output(d['result_2_1_2'])
            output(d['success'])
            nun = True
            choose_location()

