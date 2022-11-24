from os import system
from time import sleep


def bloody_valley():
	img = [['.' for x in range(125)] for y in range(21)]
	
	x1 = {5:[15,16,17,18,19,20,21,22,   27,28,                 37,38,39,      45,46,47,     52,53,54,55,56,57,58, 62,63,        68,69]}
	x2 = {6:[15,16,            21,      27,28,               36,       40,  44,      48,    52,53,            58,    63,64,  67,68]}
	x3 = {7:[15,16,17,18,19,20,         27,28,               36,       40,  44,      48,    52,53,            58,        65,66]}
	x4 = {8:[15,16,            21,      27,28,               36,       40,  44,      48,    52,53,            58,        65,66]}
	x5 = {9:[15,16,17,18,19,20,21,22,   27,28,29,30,31,32,33,  37,38,39,      45,46,47,     52,53,54,55,56,57,58,        65,66]}

	x6 =  {11:[61,62,               68,69,          74,              82,83,84,           90,91,92,           98,99,100,101,102,103,   107,108,               113,114]}
	x7 =  {12:[   62,63,         67,68,          73,74,75,           82,83,              90,91,              98,99,                       108,109,       112,113]}
	x8 =  {13:[      63,64,   66,67,          72,         76,        82,83,              90,91,              98,99,100,101,102,                  110,111]}
	x9 =  {14:[         64,65,66,          71,72,73,74,75,76,77,     82,83,              90,91,              98,99,                              110,111]}
	x10 = {15:[            65,          70,71,               77,78,  82,83,84,85,86,87,  90,91,92,93,94,95,  98,99,100,101,102,103,              110,111]}
	d = x1 | x2 | x3 | x4 | x5 | x6 | x7 | x8 | x9 | x10
	for y in d:
		for x in d[y]:
			if x in range(0, 125):
				img[y][x] = '█'
	for y in img:
		print(''.join(y))
		sleep(0.025)
	sleep(3)
	system('clear')

def house():
	img = [['.' for x in range(125)] for y in range(21)]

	x1 = {5:  [                                                   41,               47,48,49,         53,54,         58,59]}
	x2 = {6:  [                                                40,   42,         46,         50,      53,54,         58,59]}
	x3 = {7:  [                                             39,40,   42,43,      46,         50,      53,   55,   57,   59]}
	x4 = {8:  [                                             39,         43,      46,         50,      53,      56,      59]}
	x5 = {9:  [                                          38,39,40,41,42,43,44,      47,48,49,         53,               59]}
	
	x6 =  {11:[         27,               33,34,35,36,37,38,   40,41,42,43,      46,47,48,49,50,51,      54,55,   57,58,      61,62,63,64,   67,      70,71,      74,75,76,77,78,79,                  86]}
	x7 =  {12:[      26,   28,            33,34,                  41,42,         46,47,                  54,55,56,57,            62,63,      67,   69,70,71,      74,75,      78,                  85,86,87]}
	x8 =  {13:[   25,26,   28,29,         33,34,35,36,37,         41,42,         46,47,48,49,50,         54,55,56,               62,63,      67,   69,   71,      74,75,76,77,                  84,         88]}
	x9 =  {14:[   25,         29,         33,34,                  41,42,         46,47,                  54,55,56,57,            62,63,      67,68,69,   71,      74,75,      78,            83,84,85,86,87,88,89 ]}
	x10 = {15:[24,25,26,27,28,29,30,      33,34,35,36,37,38,      41,42,         46,47,48,49,50,51,      54,55,   57,58,         62,63,      67,68,      71,      74,75,76,77,78,79,      82,83,               89,90]}
	d = x1 | x2 | x3 | x4 | x5 | x6 | x7 | x8 | x9 | x10
	for y in d:
		for x in d[y]:
			if x in range(0, 125):
				img[y][x] = '█'
	for y in img:
		print(''.join(y))
		sleep(0.025)
	sleep(3)
	system('clear')
