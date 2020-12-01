# personal code check
while True:
    try:
        id_input = input('Palun sisestage isikukood: ')

        # char check
        id_int = int(id_input)

        # len check
        if len(id_input) != 11:
            print('Isikukoodil peab olema 11 numbrid, palun proovige uuesti.')

        # Control number check
        else:
            check_scale_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
            check_scale_2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
            check_sum_1 = 0
            check_sum_2 = check_sum_1

            # scale check
            for x in range(0, 10):
                check_sum_1 = check_sum_1 + int(id_input[x]) * check_scale_1[x]
                check_sum_2 = check_sum_2 + int(id_input[x]) * check_scale_2[x]

            #
            control_number_1 = check_sum_1 % 11
            control_number_2 = check_sum_2 % 11

            #
            if (10 > control_number_1 == int(id_input[10])) or (
                    int(id_input[10]) == control_number_2 or
                    control_number_2 == 10 & int(id_input[10]) == 0):
                break
            else:
                print('Isikukoodi viga, palun proovige uuesti.')
    except ValueError:
        print('Isikukoodil peab olema ainult numbrid, palun proovige uuesti.')

sex_id = id_input[0]
birth_year = id_input[1:3]  # YY
birth_month = id_input[3:5]  # MM
birth_day = id_input[5:7]  # DD
birth_place = int(id_input[7:10])

# sex and year check
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
    print("Te olite sündinud Ida-Tallinna Keskhaiglas või Pelgulinna "
          "sünnitusmajas või Hiiumaal või Keilas või Rapla haiglas või Loksa haiglas")
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

# Results of last two checks

print('Te olete sündinud: ' + by + birth_year + '.' + birth_month + '.' + birth_day)
print('Sugu ' + sex)
