import game_map
import titles
import text
import locations
import getpass
import sys
from time import sleep
from os import system
from sys import platform
if platform == 'linux': clr = 'clear'
if platform == 'win32': clr = 'cls'
CURSOR_UP_ONE = '\x1b[1A'
ERASE_LINE = '\x1b[2K'


def error():
    for i in 'Неверный ввод, попробуйте еще раз*':
        if i != "*":
            sleep(0.033)
            sys.stdout.write(i)
            sys.stdout.flush()
        else:
            getpass.getpass(prompt='')
            print((CURSOR_UP_ONE+ERASE_LINE) * 2, end='')

titles.bloody_valley()
text.database('start_')
game_map.char('-1')
for i in range(2): game_map.char('0')
titles.house()
text.database('name_')
name = input()
while name == '':
    error()
    text.output('Введите свое имя: ')
    name = input()
system(clr)
text.database('house', name)
text.database('choice-1')
choice = input()
while choice not in ['1','2']:
    error()
    choice = input()
if choice == '1': partner = False
if choice == '2': partner = True
text.database(choice=choice)
text.database('note', inven={'Записка': '''Wo früher Konzerte stattfanden, diese Ära aber vorbei ist
         Там где раньше проводились концерты, но та эра прошла''', 'Лупа': 'Просто лупа'})
inventory = {'Записка': '''Wo früher Konzerte stattfanden, diese Ära aber vorbei ist
         Там где раньше проводились концерты, но та эра прошла''', 'Лупа': 'Просто лупа'}
locations.choose_location(name,partner,inventory)
