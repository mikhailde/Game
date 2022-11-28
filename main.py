import game_map
import titles
import text
import locations
from os import system
CURSOR_UP_ONE = '\x1b[1A'


titles.bloody_valley()
text.database('start')
game_map.char(-1)
for i in range(2): game_map.char(0)
titles.house()
text.database('name_')
name = input()
system('clear')
text.database('house', name)
text.database('choice-1')
choice = input()
if choice == '1': partner = False
if choice == '2': partner = True
text.database(choice=choice)
text.database('note', inven={'Записка': '''Wo früher das Kloster stand, aber nur eine Nonne blieb
         Там где монастырь раньше стоял, но осталась только монашка''', 'Лупа': 'Просто лупа'})
locations.choose_location(name,partner)
