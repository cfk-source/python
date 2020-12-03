a = float(input('side: a '))
b = float(input('side: b '))
c = float(input('side: c '))

if int(a) == int(b) or int(a) == int(c) or int(c) == int(b):
    print('Triangle is hip equal')
else:
    print('Triangle is not hip equal')