import text
import sys
import getpass
from time import sleep
from os import system
nun = False
a_update = 0
CURSOR_UP_ONE = '\x1b[1A'


def choose_location():
    print('''Выберите действие:
[1] Перейти на главную площадь
[2] Перейти на детскую площадку
[3] Перейти на тёмный угол за каким-то клубом
[4] Перейти на старая площадь, которая уже заросла

Просмотреть инвентарь (Ctrl+X)
Выйти из игры (ESC)''')
    choice = input()
    print(CURSOR_UP_ONE)
    text.database(choice=choice, location=True)

def output(text):
    for i in text:
        if i != "*":
            sleep(0.033)
            sys.stdout.write(i)
            sys.stdout.flush()
        else:
            getpass.getpass(prompt='')
            print(CURSOR_UP_ONE, end="")

def square(name):
    if nun == False:
        for i in 'Тут нечего делать*':
                if i != "*":
                    sleep(0.033)
                    sys.stdout.write(i)
                    sys.stdout.flush()
                else:
                    getpass.getpass(prompt='')
        system('clear')
        choose_location()
def playground(name):
    if nun == False:
        for i in 'Тут нечего делать*':
                if i != "*":
                    sleep(0.033)
                    sys.stdout.write(i)
                    sys.stdout.flush()
                else:
                    getpass.getpass(prompt='')
        system('clear')
        choose_location()
def dark_corner(name):
    if nun == False:
        for i in 'Тут нечего делать*':
                if i != "*":
                    sleep(0.033)
                    sys.stdout.write(i)
                    sys.stdout.flush()
                else:
                    getpass.getpass(prompt='')
        system('clear')
        choose_location()
    
def old_square(name,partner):
    a = {}
    d = {
    'text':  f'''Вы встретили монашку*
{name}: Хэээй!*
Монашка: АААА– ЗАБИРАЙ ЧТО УГОДНО, НО МЕНЯ НЕ ТРОГАЙ*
Тут от монашки и след простыл*''',

    'choice_1': '''Выберите действие:
[1] Отправить своего помощника с ней поговорить
[2] Пойти самому''',

    'choice_2': '''Выберите действие:
[1] Пойти самому''',

    'result_1': '''Фрод: Короче. Я с ней всё обсудил. Ну ты её и напугал до чёртиков! Всё выдала! Ну слушай.
В деревню приплёлся ещё какой-то светловолосый парень, как она упомянула - певец на нашем концерте тут.
Ну веет от него таким же вайбом, как у тебя, чёртик*''',

    'choice_2_1': '''Выберите действие:
[1] Надавить на неё
[2] Спокойно всё обсудить''',

    'result_2_1_1': f'''{name}: Слушай, если ты сейчас же не выдашь мне информацию о чём либо, я тебя лично сдам в руки тому вору, чтобы из тебя сделали куклу!*
Монашка: "дрожит как кленовый лист и смотрит куда угодно, но никак не на детектива, а потом вовсе убежит от вас, не издав и звука"*''',

    'result_2_1_2': f'''{name}: Я не причиню тебе вреда и не сделаю плохо. Просто расскажи что ты знаешь. Это очень нам поможет в деле.*
Монашка: "всё-таки посмотрела на детектива"*
Ну после вас сюда приехал ещё один человек…
Он со светлыми волосами, с таким же готическим стилем и он вроде певец у нас на концерте…*''',
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
    system('clear')

