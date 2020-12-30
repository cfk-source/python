import re
# hash color's
# #ABCDEF   FF5733  F73C14

    # ^#(([0-9a-fA-F]{2}){3}|([0-9a-fA-F]){3})$


# numbers not followed by +

    # \d+\+$

# time

    # ^([0-1][0-9]|[2][0-3]):([0-5][0-9])$

# full names and addresses

    with open('people.txt', 'r', encoding='utf8') as file:
        data = file.read()

        names = re.compile(r'^[A-Z]+\s[A-z]+$')
        address = re.compile(r'^\d+\s[St.,]\s[A-z]+\s[A-Z]+\s[0-9]+$')
    print(names, address)

#

    def chars_check():
        string = ''
        while string == re.compile(r'\w+'):
            return True:
        else:
        print('String not consists of chars')


# isikukood
    
# ^{3}|{4}|{6}[4-9][0-9][0-2][1-9][1-31]\d+[1-9][0-9][0-9]$