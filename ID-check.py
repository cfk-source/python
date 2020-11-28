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
b_place = int(id_input[7:10])

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
if 0 <= b_place <= 10:
    print("Te olite sündinud Kuressaare Haiglas")
elif 11 <= b_place <= 19:
    print("Te olite sündinud Kuressaare Tartu Ülikooli Naistekliinikus, Tartumaa, Tartu")
elif 21 <= b_place <= 220:
    print("Te olite sündinud Ida-Tallinna Keskhaiglas või Pelgulinna sünnitusmajas või Hiiumaal või Keilas või Rapla haiglas või Loksa haiglas")
elif 221 <= b_place <= 270:
    print("Te olite sündinud Ida-Viru Keskhaiglas (Kohtla-Järve, endine Jõhvi)")
elif 271 <= b_place <= 370:
    print("Te olite sündinud Maarjamõisa Kliinikumis (Tartu) või Jõgeva Haiglas")
elif 371 <= b_place <= 420:
    print("Te olite sündinud Narva Haiglas")
elif 421 <= b_place <= 470:
    print("Te olite sündinud Pärnu Haiglas")
elif 471 <= b_place <= 490:
    print("Te olite sündinud Pelgulinna Sünnitusmajas (Tallinn) või Haapsalu haiglas")
elif 491 <= b_place <= 520:
    print("Te olite sündinud Järvamaa Haiglas (Paide)")
elif 521 <= b_place <= 570:
    print("Te olite sündinud Rakveres või Tapa haiglas")
elif 571 <= b_place <= 600:
    print("Te olite sündinud Valga Haiglas")
elif 601 <= b_place <= 650:
    print("Te olite sündinud Viljandi Haiglas")
elif 651 <= b_place <= 700:
    print("Te olite sündinud Lõuna-Eesti Haiglas (Võru) või Põlva Haiglas")



#Print results of code analysis

print('Sinu isikukood on: ', str(id_int))
print('Te olete sündinud: ' + by + by_id + '.' + bm_id + '.' + bd_id )
print('Sugu ' + sex)