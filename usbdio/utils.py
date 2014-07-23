"""
General purpose utility functions 
for USB DIO 32
"""

def replace_a_letter (old_string, letter_position, new_letter):
    """
    replace_a_letter takes the following arguements:
    old_string- the string in which you wish to change a letter
    letter_position- the zero-based position to the letter you wish to change
    new_letter - waht you wish to change to letter to
    replace_a_letter returns the modified string
    """
    new_letter_2 = str(new_letter) # make sure the new letter is a string
    old_string_2 = str(old_string) #make sure it is a string
    string_list = list(old_string_2) #turn string into a list
    string_list[letter_position] = new_letter_2 #replace the letter at the desired position in the list
    new_string = ''.join(string_list) # turn the list into a string
    return new_string

def bi_to_dec (bi):
    """
    takes in a binary number and returns a decimal number
    """
    bi_str = str(bi)
    dec = int( bi_str, 2)
    return dec

def dec_to_bi (dec):
    """
    takes in a decimal number and returns a binary number
    """
    if int(dec) == 0:
        bi = int(0)
        return bi
    bi_old = bin(dec)
    bi_new = bi_old[2:]
    bi = int(bi_new)
    return bi

def letter_value (letter):
    alphabet = {
        "a": 1
        "b": 2
        "c": 3
        "d": 4
        "e": 5
        "f": 6
        "g": 7
        "h": 8
        "i": 9
        "j": 10
        "k": 11
        "l": 12
        "m": 13
        "n": 14
        "o": 15
        "p": 16
        "q": 17
        "r": 18
        "s": 19
        "t": 20
        "u": 21
        "v": 22
        "w": 23
        "x": 24
        "y": 25
        "z": 26
        "1": 1
        "2": 2
        "3": 3
        "4": 4
        "5": 5
        "6": 6
        "7": 7
        "8": 8
        "9": 9
        "0": 0
    }
    old_letter = str(letter)
    new_letter = old_letter.lower()
    value = alphabet[new_letter]
    return value

    









