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

# last digit control check

check_scale_1 = [1,2,3,4,5,6,7,8,9,1]

check_scale_2 = [3,4,5,6,7,8,9,1,2,3]

# x = id_input()                              # ID user input (string!)
# y = id_int[10]                              # last digit in ID
# while True (x[0] * 1) + (x[1] * 2) + (x[3] * 3) + (x[4] * 4) + (x[5] * 5) + (x[6] * 6) + (x[7] * 7) + (x[8] * 8) + (x[9] * 9) + (x[10] * 1) / 11 != int(id_int[11]) or
#                     (x[0] * 3) + (x[1] * 4) + (x[3] * 5) + (x[4] * 6) + (x[5] * 7) + (x[6] * 8) + (x[7] * 9) + (x[8] * 1) + (x[9] * 2) + (x[10] * 3) / 11 != int(id_int[11]):


sex_id = id_input[0]
birth_year = id_input[1:3]              # YY
birth_month = id_input[3:5]             # MM
birth_day = id_input[5:7]               # DD
birth_place = int(id_input[7:10])


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
if 0 <= birth_place <= 10:
    print("Te olite sündinud Kuressaare Haiglas")
elif 11 <= birth_place <= 19:
    print("Te olite sündinud Kuressaare Tartu Ülikooli Naistekliinikus, Tartumaa, Tartu")
elif 21 <= birth_place <= 220:
    print("Te olite sündinud Ida-Tallinna Keskhaiglas või Pelgulinna sünnitusmajas või Hiiumaal või Keilas või Rapla haiglas või Loksa haiglas")
elif 221 <= birth_place <= 270:
    print("Te olite sündinud Ida-Viru Keskhaiglas (Kohtla-Järve, endine Jõhvi)")
elif 271 <= birth_place <= 370:
    print("Te olite sündinud Maarjamõisa Kliinikumis (Tartu) või Jõgeva Haiglas")
elif 371 <= birth_place <= 420:
    print("Te olite sündinud Narva Haiglas")
elif 421 <= birth_place <= 470:
    print("Te olite sündinud Pärnu Haiglas")
elif 471 <= birth_place <= 490:
    print("Te olite sündinud Pelgulinna Sünnitusmajas (Tallinn) või Haapsalu haiglas")
elif 491 <= birth_place <= 520:
    print("Te olite sündinud Järvamaa Haiglas (Paide)")
elif 521 <= birth_place <= 570:
    print("Te olite sündinud Rakveres või Tapa haiglas")
elif 571 <= birth_place <= 600:
    print("Te olite sündinud Valga Haiglas")
elif 601 <= birth_place <= 650:
    print("Te olite sündinud Viljandi Haiglas")
elif 651 <= birth_place <= 700:
                print("Te olite sündinud Lõuna-Eesti Haiglas (Võru) või Põlva Haiglas")



#Print results of code analysis

print('Te olete sündinud: ' + by + birth_year + '.' + birth_month + '.' + birth_day)
print('Sugu ' + sex)