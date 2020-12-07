#!/usr/bin/python3
def decode_cesar(shifter, e_string):
    englisn_letters = [
        'a',
        'b',
        'c',
        'd',
        'e',
        'f',
        'g',
        'h',
        'i',
        'j',
        'k',
        'l',
        'm',
        'n',
        'o',
        'p',
        'q',
        'r',
        's',
        't',
        'u',
        'v',
        'w',
        'x',
        'y',
        'z'
    ]

    d_string = ''

    for letter in e_string:
        letter_pos = englisn_letters.index(letter)
        letter_d_pos = letter_pos + shifter 

        if (letter_d_pos > 26):
            letter_d_pos = (letter_d_pos - 26)        
        
        d_string += englisn_letters[letter_d_pos]

    return d_string

for i in range(-25, 28):
    print('Shift: ' + str(i) +' -> '+ decode_cesar(i, 'dspttjohuifsvcjdpoabrkttds'))
