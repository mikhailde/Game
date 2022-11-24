import game_map
import titles
import text
from os import system
CURSOR_UP_ONE = '\x1b[1A'


titles.choose_title('bloody')

text.database('start')

game_map.char(-1)
for i in range(2):
    game_map.char(0)

titles.choose_title('house')

text.database('name')
name = input()
system('clear')

text.database('house', name)
text.database('choice_1')
choice = input()
print(CURSOR_UP_ONE, end="")
text.database(choice=choice)

text.database('note_', inven={'Записка': '''Wo früher das Kloster stand, aber nur eine Nonne blieb
         Там где монастырь раньше стоял, но осталась только монашка''', 'Лупа': 'Просто лупа'})

text.choose_location()




while True:
    location = input('[1]\n[2]\n[3]\n[4]\n[5]\n[6]\n[0] - выход\nВведите локацию: ')
    if location == '0':
        break
    for i in range(2):
        game_map.char(int(location))
