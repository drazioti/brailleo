import getch

"""

prints out braille characters's correspondant ASCII code equivalents

102 : f  --> 1
100 : d  --> 2
115 : s  --> 3
106 : j  --> 4
107 : k  --> 5
108 : l  --> 6

"""

aDict = dict(zip('αβγδεζη', ['00000','00001','00010','00011','00100','11000','11001']))

def text_enc(text):
	key = ord(getch.getch())
	text = text[::-1]
	length = len(text)
	coded_text = ''
	for i in range(length):
		coded_text = aDict[text[i]]+ coded_text
	return coded_text.lower()

print("every keypress will return it's correspondant ASCII code\npress esc to exit")
while True:
    key = ord(getch.getch())
    print(key,getch.getch())
    if key == 27:
        break

