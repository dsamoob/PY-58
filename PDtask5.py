
import time
import copy

documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]
directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': ['301']
}
menu = {'p': 'Поиск владельца по номеру документа',
        's': 'Определние местонахождения документа по номеру',
        'l': 'Показать все зарегестрированные документы',
        'a': 'Добавить новый документ',
        'd': 'Удаление документа',
        'm': 'Переместить докуменет на другую полку',
        'as': 'Добавление новой полки',
        'ex': 'Завершение работы программы'
}

positive_answers = ['да', 'ок', 'yes', 'ok', 'lf', 'нуы']
negative_answers = ['no', 'нет', 'ytn', 'тщ']


def menu_list(menu):
    print(f'{"-" * 15} Оглавление меню {"-" * 15}')
    for key, name in menu.items():
        print(f'{key}-{name}')
    print(f'{"-" * 15} {"-" * 15}')
    command = input('Введите команду из списка: ')
    if command in menu.keys():
        return command
    else:
        print('Неверная команда')
        return 'menu'


def name_by_doc(documents):
    doc_number = input('Введите номер документа: ')
    if doc_number in [x['number'] for x in documents]:
        for doc in documents:
            if doc_number == doc['number']:
                print(doc['name'])
                one_more_time = input('Найти что-либо еще? ').lower()
                if one_more_time in positive_answers:
                    name_by_doc(documents)
                    return 'menu'
                else:
                    return 'menu'
    else:
        print(f'Документа с номером {doc_number} нет в списке.')
        one_more_time = input('Попробовать еще раз? ').lower()
        if one_more_time in positive_answers:
            name_by_doc(documents)
            return 'menu'
        else:
            print('Возврат в меню')
            return 'menu'


def check_shelf(documents, directories):
    doc_number = input('Введите номер документа: ')
    if doc_number in [x['number'] for x in documents]:
        if any(doc_number in shelf for shelf in directories.values()):
            for value in directories:
                if doc_number in directories[value]:
                    print(f'Документ № {doc_number} находится на полке № {value}')
                    request = input('Проверить еще документ? ').lower()
                    if request in positive_answers:
                        check_shelf(documents, directories)
                        return 'menu'
                    else:
                        print('Возврат в меню')
                        time.sleep(0.1)
                        return 'menu'
        else:
            print(f'Документ № {doc_number} есть базе, но он не размещен на полке')
            request = input('Поместить документ на полку? ').lower()
            if request in positive_answers:
                shelf_number = input('Введите номер полки для хранения документа:')
                if shelf_number in directories:
                    directories[shelf_number].append(doc_number)
                    print(f'Документ № {doc_number} размещен на полке {shelf_number}')
                    request = input('Проверить еще документ? ').lower()
                    if request in positive_answers:
                        check_shelf(documents, directories)
                        return 'menu'
                    else:
                        print('Возврат в меню')
                        time.sleep(0.1)
                        return 'menu'
                else:
                    print('Данной полки нет в списке полок, она будет добавленная автоматически')
                    directories[shelf_number] = [doc_number]
                    print(f'Документ № {doc_number} размещен на полке {shelf_number}')
                    request = input('Проверить еще документ? ').lower()
                    if request in positive_answers:
                        check_shelf(documents, directories)
                        return 'menu'
                    else:
                        print('Возврат в меню')
                        time.sleep(0.1)
                        return 'menu'
    else:
        for shelf_number in directories:
            if doc_number in directories[shelf_number]:
                print(f'Документ № {doc_number} отсутствует в базе, но он находится на полке № {shelf_number}\n'
                      f'его необходимо добавить в базу, предварительно он будет стерт из полки')
                directories_copy = copy.copy(directories)
                directories[shelf_number].remove(doc_number)
                print(f'Документ № {doc_number} удален с полки {shelf_number}')
                add_document(documents, directories)


def add_document(documents, directories):
    doc_type = input('Введите тип документа: ')
    doc_number = input('Введите номер документа: ')
    doc_owner = input('Введите имя владельца документа: ')
    if doc_number not in [x['number'] for x in documents]:
        if not any(doc_number in shelf for shelf in directories.values()):
            documents.append({'type': doc_type, 'number': doc_number, 'name': doc_owner })
            shelf_number = input('Введите номер полки для хранения документа:')
            if shelf_number in directories:
                directories[shelf_number].append(doc_number)
                print(f'{doc_type}№ {doc_number} добавлен в базу и размещен на полке {shelf_number}')
                request = input('Добавить еще документ? ').lower()
                if request in positive_answers:
                    add_document(documents, directories)
                    return 'menu'
                else:
                    print('Возврат в меню')
                    time.sleep(0.1)
                    return 'menu'
            else:
                directories[shelf_number] = [doc_number]
                print(f'{doc_type}№ {doc_number} добавлен в базу и размещен на полке {shelf_number}')
                request = input('Добавить еще документ? ').lower()
                if request in positive_answers:
                    add_document(documents, directories)
                    return 'menu'
                else:
                    print('Возврат в меню')
                    time.sleep(0.1)
                    return 'menu'
    else:
        if not any(doc_number in shelf for shelf in directories.values()):
            print(f'Документ под номером {doc_number} уже зарегистрирован, но не размещен на полке')
            request = input('Разместить его на полке? ').lower()
            if request in positive_answers:
                shelf_number = input('Введите номер полки для хранения документа:')
                if shelf_number in directories:
                    directories[shelf_number].append(doc_number)
                    print(f'{doc_type}№ {doc_number} добавлен в базу и размещен на полке {shelf_number}')
                    request = input('Добавить еще документ? ').lower()
                    if request in positive_answers:
                        add_document(documents, directories)
                        return 'menu'
                    else:
                        print('Возврат в меню')
                        time.sleep(0.1)
                        return 'menu'
                else:
                    directories[shelf_number] = [doc_number]
                    print(f'Полки №{shelf_number} нет в базе, она будет добавлена автоматически')
                    print(f'{doc_type}№ {doc_number} добавлен в базу и размещен на полке {shelf_number}')
                    request = input('Добавить еще документ? ').lower()
                    if request in positive_answers:
                        add_document(documents, directories)
                        return 'menu'
                    else:
                        print('Возврат в меню')
                        time.sleep(0.1)
                        return 'menu'
            else:
                print('Возврат в меню')
                time.sleep(0.1)
                return 'menu'
        else:
            for value in directories:
                if doc_number in directories[value]:
                    time.sleep(0.1)
                    print(f'Документ № {doc_number} уже есть в базе находится на полке № {value}')
                    time.sleep(0.1)
                    return 'menu'


def list_all_docs(documents):
    for i in documents:
        print(f'{i["type"]} "{i["number"]}" "{i["name"]}"')
    time.sleep(0.1)
    return 'menu'


def delete_document(documents, directions):
    doc_number = input('Введите номер документа для удаления ')
    if doc_number in [x['number'] for x in documents]:
        if any(doc_number in shelf for shelf in directories.values()):
            for doc in documents:
                if doc_number == doc['number']:
                    documents.remove(documents[documents.index(doc)])
            for shelf_number in directories:
                if doc_number in directories[shelf_number]:
                    directories_copy = copy.copy(directories)
                    directories[shelf_number].remove(doc_number)
                    print(f'Документ № {doc_number} удален с полки {shelf_number} и из базы')
                    one_more_time = input('Еще удалить? ').lower()
                    if one_more_time in positive_answers:
                        delete_document(documents, directories)
                        return 'menu'
                    else:
                        print('Возврат в меню')
                        time.sleep(0.1)
                        return 'menu'

    else:
        print(f'Документа {doc_number} нет в базе')
        one_more_time = input('Попробовать еще раз? ').lower()
        if one_more_time in positive_answers:
            delete_document(documents, directories)
            return 'menu'
        else:
            print('Возврат в меню')
            time.sleep(0.1)
            return 'menu'


def moving_document(directions):
    doc_number = input('Введите номер документа для перемещения:')
    if any(doc_number in shelf for shelf in directories.values()):
        new_shelf_number = input('Введите новую полку:')
        if new_shelf_number not in directories:
            directories_copy = copy.copy(directories)
            for shelf, doc in directories_copy.items():
                if doc_number in doc:
                    directories[new_shelf_number] = [doc_number]
                    directories[shelf].remove(doc_number)
                    print(f'Документ № {doc_number} перемещен.')
                    if input('Переместить другой документ?') in positive_answers:
                        moving_document(directions)
                        return 'menu'
                    else:
                        print('Возврат в меню')
                        time.sleep(0.1)
                        return 'menu'

        else:
            for shelf, doc in directories.items():
                if doc_number in doc:
                    directories[shelf].remove(doc_number)
                    directories[new_shelf_number].append(doc_number)
                    print(f'Документ № {doc_number} перемещен.')
                    if input('Переместить другой документ?') in positive_answers:
                        moving_document(directions)
                        return 'menu'
                    else:
                        print('Возврат в меню')
                        time.sleep(0.1)
                        return 'menu'

    else:
        print(f'Документа с номером {doc_number} нет на полках')
        request = input('Добавить данный дкоумент? ')
        if request in positive_answers:
            add_document(documents, directions)
            return 'menu'
        else:
            if input('Попробовать еще раз?') in positive_answers:
                moving_document(directions)
                return 'menu'
            else:
                print('Возврат в меню')
                time.sleep(0.1)
                return 'menu'


def add_shelf(directories):
    new_shelf = input('Какую полку добавить? ')
    if new_shelf in directories:
        print(f'Полка № {new_shelf} уже есть')
        request = input('Добавить другую полку?').lower()
        if request in positive_answers:
            add_shelf(directories)
            return 'menu'
        else:
            print('Возврат в меню')
            time.sleep(0.1)
            return 'menu'
    else:
        directories[new_shelf] = []
        print(f'Полка № {new_shelf} добавлена')
        request = input('Добавить другую полку?').lower()
        if request in positive_answers:
            add_shelf(directories)
            return 'menu'
        else:
            print('Возврат в меню')
            time.sleep(0.1)
            return 'menu'




# вопрос new_list = list(chain.from_iterable(list(map(lambda x: x, directories.values())))) from_iterable

result = 'menu'

while result != 'ex':
    if result == 'menu':
        result = menu_list(menu)
    elif result == 'p':
        result = name_by_doc(documents)
    elif result == 's':
        result = check_shelf(documents, directories)
    elif result == 'l':
        result = list_all_docs(documents)
    elif result == 'a':
        result = add_document(documents, directories)
    elif result == 'd':
        result = delete_document(documents, directories)
    elif result == 'm':
        result = moving_document(directories)
    elif result == 'as':
        result = add_shelf(directories)
else:
    print('bye bye')





