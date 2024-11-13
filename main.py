

code = {'A':'▄ ▄▄▄',
        'B':'▄▄▄ ▄ ▄ ▄',
	    'C':'▄▄▄ ▄ ▄▄▄ ▄',
	    'D':'▄▄▄ ▄ ▄',
	    'E':'▄',
	    'F':'▄ ▄ ▄▄▄ ▄',
	    'G':'▄▄▄ ▄▄▄ ▄',
	    'H':'▄ ▄ ▄ ▄',
	    'I':'▄ ▄',
	    'J':'▄ ▄▄▄ ▄▄▄ ▄▄▄',
	    'K':'▄▄▄ ▄ ▄▄▄',
	    'L':'▄ ▄▄▄ ▄ ▄',
	    'M':'▄▄▄ ▄▄▄',
	    'N':'▄▄▄ ▄',
	    'O':'▄▄▄ ▄▄▄ ▄▄▄',
	    'P':'▄ ▄▄▄ ▄▄▄ ▄',
	    'Q':'▄▄▄ ▄▄▄ ▄ ▄▄▄',
	    'R':'▄ ▄▄▄ ▄',
	    'S':'▄ ▄ ▄',
	    'T':'▄▄▄',
	    'U':'▄ ▄ ▄▄▄',
	    'V':'▄ ▄ ▄ ▄▄▄',
	    'W':'▄ ▄▄▄ ▄▄▄',
	    'X':'▄▄▄ ▄ ▄ ▄▄▄',
	    'Y':'▄▄▄ ▄ ▄▄▄ ▄▄▄',
	    'Z':'▄▄▄ ▄▄▄ ▄ ▄',
	    '0':'▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄',
	    '1':'▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄',
	    '2':'▄ ▄ ▄▄▄ ▄▄▄ ▄▄▄',
	    '3':'▄ ▄ ▄ ▄▄▄ ▄▄▄',
	    '4':'▄ ▄ ▄ ▄ ▄▄▄',
	    '5':'▄ ▄ ▄ ▄ ▄',
	    '6':'▄▄▄ ▄ ▄ ▄ ▄',
	    '7':'▄▄▄ ▄▄▄ ▄ ▄ ▄',
	    '8':'▄▄▄ ▄▄▄ ▄▄▄ ▄ ▄',
	    '9':'▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄',
        ".":'▄ ▄▄▄ ▄ ▄▄▄ ▄ ▄▄▄',
        ",":'▄▄▄ ▄▄▄ ▄ ▄ ▄▄▄ ▄▄▄',
        "?":'▄ ▄ ▄▄▄ ▄▄▄ ▄ ▄',
        "'":'▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄',
        " ":'    '} #word space is 7 - we will add 3 more below so just add 4 here

to_convert = input("Enter a phrase to encode:")
converted = ""
for char in to_convert:
    converted += code[char.upper()] + '   ' #3 spaces to denote a letter space
print("In Morse code:")
print(converted)