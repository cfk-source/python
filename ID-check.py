# personal code check
while True:
    try:
        id_input = input('Palun sisestage isikukood: ')
        id_int = int(id_input)
        if len(id_input) != 11:
            print('Isikukoodil peab olema 11 numbrid, palun proovige uuesti.')
        else:
            id_int = int(id_input)
            break
    except:
        print('Palun sisetage ainult nubrid.')

sex_id = id_input[0]
by_id = id_input[1:3]            # YY
bm_id = id_input[3:5]            # MM
bd_id = id_input[5:7]            # DD
birth_place_id = id_input[7:11]
birth_place_int = int(id_input)


#sex and year extraction

if sex_id == '1':
    sex = 'mees'
    by = '18'
elif sex_id == '2':
    sex = 'naine'
    by = '18'
elif sex_id == '3':
    sex = 'mees'
    by = '19'
elif sex_id == '4':
    sex = 'naine'
    by = '19'
elif sex_id == '5':
    sex = 'mees'
    by = '20'
elif sex_id == '6':
    sex = 'naine'
    by = '20'

# birth place check
if 1 >= birth_place_int <= 10:
    b_place = 'Kuressaare Haigla'
elif 11 >= birth_place_int <= 19:
    b_place = 'Tartu Ülikooli Naistekliinik, Tartumaa, Tartu'
elif 21 >= birth_place_int <= 220:
    b_place = 'Ida-Tallinna Keskhaigla, Pelgulinna sünnitusmaja, Hiiumaa, Keila, Rapla Haigla, Loksa Haigla'
elif 221 >= birth_place_int <= 270:
    b_place = 'Ida-Viru Keskhaigla (Kohtla-Järve, endine Jõhvi)'
elif 271 >= birth_place_int <= 370:
    b_place = 'Maarjamõisa Kliinikum (Tartu), Jõgeva Haigla'
elif 371 >= birth_place_int <= 420:
    b_place = 'Narva Haigla'
elif 421 >= birth_place_int <= 470:
    b_place = 'Pärnu Haigla'
elif 471 >= birth_place_int <= 490:
    b_place = 'Pelgulinna Sünnitusmaja (Tallinn), Haapsalu Haigla'
elif 491 >= birth_place_int <= 520:
    b_place = 'Järvamaa Haigla (Paide)'
elif 521 >= birth_place_int <= 570:
    b_place = 'Rakvere, Tapa Haigla'
elif 571 >= birth_place_int <= 600:
    b_place = 'Valga Haigla'
elif 601 >= birth_place_int <= 650:
    b_place = 'Viljandi Haigla'
elif 651 >= birth_place_int <= 700:
    b_place = 'Lõuna-Eesti Haigla (Võru), Põlva Haigla'



#Print results of code analysis

print('Sinu isikukood on: ' + str(id_int))
print('Te olete sündinud: ' + by + by_id + '.' + bm_id + '.' + bd_id + b_place)
print('Sugu ' + sex)