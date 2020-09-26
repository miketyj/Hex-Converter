import re

def hasNumbers(inputString):
     return bool(re.search(r'\d', inputString))

def hasString(inputString):
    chars = set('0123456789')
    if any((c in chars) for c in inputString):
        return False
    else:
        return True

def convert_to_fourbytes(char_output):
    result = ''
    fourbytes_string = ''
    counter = 0
    char_output = char_output[::-1]
    return_value = ''
    for char in char_output:
            fourbytes_string = fourbytes_string + char[2:5]
    for i in range(0,len(fourbytes_string),2):
        counter += 1
        return_value = return_value + '\\x' + fourbytes_string[i:i+2]
        if counter == 4 and i != len(fourbytes_string)-2:
            return_value = return_value + ', '
            counter = 0
    return return_value

def convert_to_fourbytes_int(int_output):
    int_output = int_output[2:]
    if (len(int_output) % 2 != 0):
        int_output =  '0' + int_output
    fourbytes_string = ''
    for i in range(len(int_output)-2,-1,-2):
        fourbytes_string = fourbytes_string + "\\x" + int_output[i:i+2]
    return fourbytes_string

def program():
    error = False
    print('-' * 80)
    print("This is a program that converts integer/string into hexdecimal value.\n Author: @likemikesg\n Kindly Report Any Bug to yjteng.2018@smu.edu.sg")
    print('-' * 80)
    convertion_type = int(input('Select 1 or 2: \n1.Converting Int \n2.Converting Char\n' + '-' * 80 + '\nInput: '))

    if (convertion_type < 1 or convertion_type > 2):
        error = True
        print("Error: Invalid conversion type")

    if (error == False):
        val = input("Enter value for conversion(e.g. 123459876 or abcdefg): ")
    if (convertion_type == 2 and hasNumbers(val)):
        error = True
        print("Error: Invalid value: Please enter characters only")

    if (convertion_type == 1 and hasString(val)):
        error = True
        print("Error: Invalid value: Please enter numbers only")

    if (convertion_type == 1 and val != '' and error == False) :
        int_output = str(hex(int(val)))
        print( '-' * 80)
        print('Hexadecimal value for ' + val + ": ")
        print( '-' * 80)
        print( '-' * 80)
        print("Hexadecimal Value for " + val + ': ' + str(int_output[2:]))
        print("Reversed and Separated into 4 bytes: " + (convert_to_fourbytes_int(int_output)))
        print( '-' * 80)
        k=input("Press r to restart: ")
        if (k == 'r'):
            program()
    elif(convertion_type == 2 and val != '' and error == False) :
        char_output = []
        for each in val: {
            char_output.append(hex(ord(each)))
        }
        print( '-' * 80)
        print('Hexadecimal value for ' + val + ": ")
        print( '-' * 80)
        print( '-' * 80)
        print("Hexadecimal values for " + val + ': ' + str(char_output))
        print("Reversed and Separated into 4 bytes: " + str(convert_to_fourbytes(char_output)))
        print( '-' * 80)
        k=input("Press r to restart: ")
        if (k == 'r'):
            program()
    else:
        print( '-' * 80)
        print("!!! Program will now restart. !!!")
        print( '-' * 80)
        if (error == True):
            program()

program()
print( '-' * 80)
k=input("Press r to restart: ")

if (k == 'r'):
    program()