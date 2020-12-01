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
        print('Your personal ID-code is: ' + id)
        # birth date extraction NB!!! STRINGS
        bd = id[0:2]    # "DD"
        bm = id[2:4]    # "MM"
        by = id[4:6]    # "YY"
        c = id[6]       # "C" century sign: ("-" 1900-1999),("+" 1800-1899),("A" 2000-2099)
        z = id[7:10]    # "ZZZ" Individual number
        q = id[10]      # "Q" Control char.checksum
        b_day = str(bd) + '.' + str(bm) + '.19' + str(by)
        b_day_formated = datetime.datetime.strptime(b_day, '%d.%m.%Y')              # birth date human_readable
        today = datetime.date.today()
        age = today.year - b_day_formated.year - (
                (today.month, today.day) < (b_day_formated.month, b_day_formated.day))

        # sex
        if int(z) % 2 == 0:
            sex = 'female'
        else:
            sex = 'man'

        # personal number status - permanent / temporary
        if int(z) >= 2 & int(z) <= 899:
            id_state = ' permanent'
        else:
            id_state = ' temporary'
        print('Personal code is: ' + id_state)

        # birth date check & output according to 'C'entury information
        if c == '+':
            print('Your birth date is: ', str(18) + by + '.' + bm + '.' + bd + ' and you are ' + str(age) + ' full years ' + sex + '.')

        elif c == '-':
            print('Your birth date is: ', str(19) + by + '.' + bm + '.' + bd + ' and you are ' + str(age) + ' full years ' + sex + '.')

        elif c == 'A':
            print('Your birth date is: ', str(20) + by + '.' + bm + '.' + bd + ' and you are ' + str(age) + ' full years ' + sex + '.')
        else:
            break
            print('Wrong century information.')

        # control character check - "DDMMYY.ZZZ"
        control_char = (int(id[0:10]) - int(id[6])) / 31













    except ValueError:
        print()


