# Finish personal identificational number validation

import datetime

while True:
    try:
        id = input('Please enter your personal code: ')   # DDMMYYCZZZQ - 131052-308T

        # birth date numeric check
        if not (id[0:6].isnumeric()):
            print('The first 6 should be only numbers, please try again.')
            break

        # length check
        len(id) == 11

        # birth date extraction NB!!! STRINGS
        bd = id[0:2]    # "DD"
        bm = id[2:4]    # "MM"
        by = id[4:6]    # "YY"
        c = id[6]       # "C" century sign: ("-" 1900-1999),("+" 1800-1899),("A" 2000-2099)
        z = id[7:10]    # "ZZZ" Individual number
        q = id[10]      # "Q" Control char.checksum

        # birth date check & output according to 'C'entury information
        if c == '+':
            print('Your birth date is: ', str(18) + by + '.' + bm + '.' + bd + '')

        elif c == '-':
            print('Your birth date is: ', str(19) + by + '.' + bm + '.' + bd)

        elif c == 'A':
            print('Your birth date is: ', str(20) + by + '.' + bm + '.' + bd)
        else:
            print('Wrong century information.')
            break










    except ValueError:
        print()


