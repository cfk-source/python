# personal code check program



# variables
error_message = 'Palun kontrollige isikukood ja proovige uuesti.'



# user input
id = input('Palun sisestage oma isiku kood: ')



# personal code numeric check




# birth date extraction
yy = (id[1:3])   # year
mm = (id[3:5])   # month
dd = (id[5:7])   # day



# personal code length check
if len(id) == 11:
    print('Sinu isikukood on: ',id)
else:
   print(id,'Vale isikukood pikkus!',error_message)



# century check
if int(id[0]) == 1 or int(id[0]) == 2:
    print('Sinu sünniaeg on: 18' + yy + '.' + mm + '.' + dd)
if int(id[0]) == 3 or int(id[0]) == 4:
    print('Sinu sünniaeg on: 19' + yy + '.' + mm + '.' + dd)
if int(id[0]) == 5 or int(id[0]) == 6:
    print('Sinu sünniaeg on: 20' + yy + '.' + mm + '.' + dd)
if int(id[0]) == 7 or int(id[0]) == 8:
    print('Sa ei olnud veel sündinud!',error_message)



# sex check
if int(id[0]) == 1 or int(id[0]) == 3 or int(id[0]) == 5 or int(id[0]) == 7:
    print('Sugu: mees')
if int(id[0]) == 2 or int(id[0]) == 4 or int(id[0]) == 6 or int(id[0]) == 8:
    print('Sugu: naine')