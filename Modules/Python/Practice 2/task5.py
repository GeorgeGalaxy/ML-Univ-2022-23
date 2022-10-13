data_base = {}

while input('Ввести сотрудника (0/1): ') != '0':

    fio = input('ФИО: ')

    error = True

    while error:
        try:
            age = int(input('Возраст: '))
            error = False
        except:
            print('Только цифры !')

    status = input('Должность: ')

    error = True

    while error:
        try:
            place_number = int(input('Номер рабочего места: '))
            error = False
        except:
            print('Только цифры !')

    access = ''

    while access not in ['да', 'нет']:

        access = input('наличие доступа к тайне (ТОЛЬКО: да/нет): ')

    data_base[fio] = {'возраст': age,
                      'должность': status,
                      'номер рабочего места': place_number,
                      'наличие доступа к тайне (да/нет)': access}

print(data_base)
