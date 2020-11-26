id = input('Palun sisestage oma isiku kood: ')
error_message = 'Palun kontrollige isikukood ja proovige uuesti.'




if len(id) == 11:
    print('Sinu isikukood on: ',id)

else:
   print(id,'Vale isikukood pikkus!',error_message)

if int(id[1]) < 2:
    print('Isikukood viga.',error_message)