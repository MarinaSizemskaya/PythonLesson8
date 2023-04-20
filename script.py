from data_create import name_data, surname_data, phone_data, address_data, new_inform_data

def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f"В каком формате вы хотите записать данные?\n\n"
                    f"1 вариант:\n\n"
                    f"{name}\n"
                    f"{surname}\n"
                    f"{phone}\n"
                    f"{address}\n"
                    f"2 вариант:\n\n"
                    f"{name};{surname};{phone};{address}\n\n"
                    f"Выберите номер варианта: "))

    while var != 1 and var !=2:
        print("Нет такого варианта")
        var = int(input("Введите номер варианта: "))

    if var == 1:
        with open('D:\Marina\Документы\гик брейнс\Python_Lesson8\data_first_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name}\n{surname}\n{phone}\n{address}\n\n')
    else:
        with open('D:\Marina\Документы\гик брейнс\Python_Lesson8\data_second_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name};{surname};{phone};{address}\n\n')
    
def print_data():
    print('Вывожу для Вас данные из 1 файла\n')
    with open('D:\Marina\Документы\гик брейнс\Python_Lesson8\data_first_variant.csv', 'r', encoding='utf-8') as file:
        data_first = list(file.readlines())
        print(*data_first, sep='')

    print('Вывожу для Вас данные из 2 файла\n')
    with open('D:\Marina\Документы\гик брейнс\Python_Lesson8\data_second_variant.csv', 'r', encoding='utf-8')as file:
        data_second = list(file.readlines())
        print(*data_second)
    return data_first, data_second
  

def put_data():
    print('Из какого файла Вы хотите изменить данные?')
    data_first, data_second = print_data()
    number_file = int(input('Введите номер файла: '))  

    while number_file != 1 and number_file != 2:
        print('Нет такого файла')
        number_file = int(input('Введите номер файла: '))
    

    if number_file == 1:
        print('Какую по счету запись вы хотите изменить? ')
        for i, row in enumerate(data_first):
            print(i+1,row)
        number_journal = int(input('Введите номер записи: '))
    
        
        print(f'Изменить данную запись\n{data_first[number_journal-1]}')

        new_inform = new_inform_data()
        data_first = data_first[:number_journal-1] + [f'{new_inform}\n'] + \
                    data_first[number_journal:] 
        with open('D:\Marina\Документы\гик брейнс\Python_Lesson8\data_first_variant.csv', 'w', encoding='utf-8') as file:
            file.write(''.join(data_first))
            print('Изменения успешно сохранены!')
    else:
        print("Какую именно запись по счету Вы хотите изменить?")
        for i, row in enumerate(data_second):
            print(i+1,row)
        number_journal = int(input('Введите номер записи: '))

        print(f'Изменить данную запись\n{data_second[number_journal-1]}')
        name = name_data()
        surname = surname_data()
        phone = phone_data()
        address = address_data()
        data_second = data_second[:number_journal-1] + [f'{name};{surname};{phone};{address}\n'] + \
                      data_second[number_journal:]
        with open('D:\Marina\Документы\гик брейнс\Python_Lesson8\data_second_variant.csv', 'w', encoding='utf-8') as file:
            file.write(''.join(data_second))
            print('Изменения успешно сохранены!')

def delete_data():
    print('Из какого файла Вы хотите удалить данные?')
    data_first, data_second = print_data()
    number_file = int(input('Введите номер файла: '))
    while new_func(number_file) and number_file != 2:
        print('Нет такого файла')
        number_file = int(input('Введите номер файла: '))
    if number_file == 1: 
        for i, row in enumerate(data_first):
            print(i+1,row)
        print("Какую именно запись по счету Вы хотите удалить?")
        number_journal = int(input('Введите номер записи: '))

        print(f'Удалить данную запись\n{data_first[number_journal-1]}')
        data_first = data_first[:number_journal-1] + data_first[number_journal:]
        with open('D:\Marina\Документы\гик брейнс\Python_Lesson8\data_first_variant.csv', 'w', encoding='utf-8') as file:
            file.write(''.join(data_first))
        print('Изменения успешно сохранены!')
    else:
        print("Какую именно запись по счету Вы хотите удалить?")
        for k, row in enumerate(data_second):
            print(k+1,row)
        number_journal = int(input('Введите номер записи: '))

        print(f'Удалить данную запись\n{data_second[number_journal - 1]}')
        data_second = data_second[:number_journal-1] + data_second[number_journal:]
        with open('D:\Marina\Документы\гик брейнс\Python_Lesson8\data_second_variant.csv', 'w', encoding='utf-8') as file:
            file.write(''.join(data_second))
        print('Изменения успешно сохранены!')

def new_func(number_file):
    return number_file != 1
    
