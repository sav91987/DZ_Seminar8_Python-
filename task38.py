import os

def get_contact_list(contact):
    
    for line in contact:
        my_list = line.split(';')
    
    for i in range(len(my_list)):
        my_list[i] = tuple(my_list[i].split(','))
    my_list.pop()
    print(my_list)
    return my_list
    

def add_contact(contact_list, contact):
    fio = input('Введите ФИО нового контакта: ')
    phone_number = input('Введите номер телефона контакта: ')

    contact_list.append((fio, phone_number))
    contact.seek(0, os.SEEK_END)
    contact.write(f'{fio},{phone_number};')

    return contact_list

def search_contact(contact_list):
    search_data = input('Введите информация для поиска: ').lower()
    search_list = []
    index_list = []
    for elem in contact_list:
        if (elem[0].lower().find(search_data) != -1) or (elem[1].find(search_data) != -1):
            search_list.append(elem)
            index_list.append(contact_list.index(elem))
    if len(index_list) == 1: return search_list, index_list[0]
    elif len(index_list) == 0: return '-', 0
    else: return search_list, 0
    

def print_contact_list(contact_list):
    for elem in contact_list:
        print(f'ФИО: {elem[0].strip()}\nТелефон: {elem[1].strip()}\n\n')

def change_contact(contact_list, search_contact_list, index_for_change):
    
    if len(search_contact_list) > 1: print('Необходимо сузить условия поиска, найдено боллее одного контакта')
    else:
        input_value = int(input('Если Вы хотите изменить ФИО - наберите 1, если хотите изменить номер телефона - наберите 2: '))
        if input_value == 1: 
            new_fio = input('Введите новое значение для ФИО: ')
            for elem in search_contact_list:
                changed_contact = (new_fio, elem[1])
            contact_list.pop(index_for_change)
            contact_list.insert(index_for_change, changed_contact)
            return contact_list
        elif input_value == 2:
            new_phone_number = input('Введите новое значение для телефона: ')
            for elem in search_contact_list:
                changed_contact = (elem[0], new_phone_number)
            contact_list.pop(index_for_change)
            contact_list.insert(index_for_change, changed_contact)
            return contact_list
            
        else: print('Некорректные данные!')

def upadate_contact_list(contact_list, contact):
    for elem in contact_list:
        contact.write(f'{elem[0]},{elem[1]};')


def del_contact(contact_list, index_for_change):
    contact_list.pop(index_for_change)
    return contact_list




value = int(input('Введите требуемое действие со справочником:\n\t1 - Показать все контакты \n\t2 - Добавить контакт\n\t3 - Найти контакт\n\t4 - Изменить контакт\n\t5 - Удалить контакт\n\t6 - Выход\n'))

while value != 6:
    if value == 1:
        contact = open('file.txt', 'r+', encoding='utf-8')
        print_contact_list(get_contact_list(contact))
        contact.close()

    elif value == 2:
        contact = open('file.txt', 'r+', encoding='utf-8')
        print_contact_list(add_contact(get_contact_list(contact), contact))
        contact.close()

    elif value == 3:
        contact = open('file.txt', 'r+', encoding='utf-8')
        search_list, index_for_change = search_contact(get_contact_list(contact))
        if index_for_change !=0: print_contact_list(search_list)
        else: print('\nНичего не найдено')
        contact.close()
            
    elif value == 4:
        contact = open('file.txt', 'r+', encoding='utf-8')
        changed_contact_list = get_contact_list(contact)
        search_list, index_for_change = search_contact(changed_contact_list)
        if search_list =='-': print('Ничего не найдено')
        else: 
            change_contact(changed_contact_list, search_list, index_for_change)
        contact.close()
        contact = open('file.txt', 'w', encoding='utf-8')
        upadate_contact_list(changed_contact_list, contact)
        contact.close()
    elif value == 5:
        contact = open('file.txt', 'r+', encoding='utf-8')
        changed_contact_list = get_contact_list(contact)
        search_list, index_for_change = search_contact(changed_contact_list)
        del_contact(changed_contact_list, index_for_change)
        contact.close()
        contact = open('file.txt', 'w', encoding='utf-8')
        upadate_contact_list(changed_contact_list, contact)
        contact.close()
    elif value == 6:
        print('До свиданья!')
    else: print('Введено неверное значение')
    value = int(input('Введите требуемое действие со справочником:\n\t1 - Показать все контакты \n\t2 - Добавить контакт\n\t3 - Найти контакт\n\t4 - Изменить контакт\n\t5 - Удалить контакт\n\t6 - Выход\n'))