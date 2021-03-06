documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
    {"type": "insurance", "number": "333", "name": "Аристарх Павлов"}
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
        'menu': 'Вызов меню',
        'ex': 'Завершение работы программы'
        }
positive_answers = ['да', 'ок', 'yes', 'ok', 'lf', 'нуы']


def menu_list(menu):
    print(f'{"-" * 15} Оглавление меню {"-" * 15}')
    for key, name in menu.items():
        print(f'{key}-{name}')
    print(f'{"-" * 15} {"-" * 15}')
    command = input('Введите команду из списка: ')
    while command not in menu:
        print('Неверная команда')
        command = input('Введите команду')
    return command


def name_by_doc(documents):
    doc_number = input('Введите номер документа: ')
    if doc_number in [x['number'] for x in documents]:
        for doc in documents:
            if doc_number == doc['number']:
                print(doc['name'])
    else:
        print(f'Документа с номером {doc_number} нет в списке.')
    if input('Попробовать еще раз? ').lower() in positive_answers:
        name_by_doc(documents)


def check_shelf(documents, directories):
    doc_number = input('Введите номер документа: ')
    if doc_number in [x['number'] for x in documents]:
        if any(doc_number in shelf for shelf in directories.values()):
            for value in directories:
                if doc_number in directories[value]:
                    print(f'Документ № {doc_number} находится на полке № {value}')
        else:
            print(f'Документ № {doc_number} есть базе, но он не размещен на полке')
            request = input('Поместить документ на полку? ').lower()
            if request in positive_answers:
                shelf_number = input('Введите номер полки для хранения документа:')
                if shelf_number in directories:
                    directories[shelf_number].append(doc_number)
                    print(f'Документ № {doc_number} размещен на полке {shelf_number}')
                else:
                    new_shelf = shelf_number
                    if input('Данной полки нет в списке полок, добавить? ') in positive_answers():
                        directories[new_shelf] = []
                        directories[new_shelf].append(doc_number)
                        print(f'Документ № {doc_number} размещен на полке {shelf_number}')
    else:
        if any(doc_number in shelf for shelf in directories.values()):
            for shelf_number in directories:
                if doc_number in directories[shelf_number]:
                    new_shelf = shelf_number
            print(f'Документ № {doc_number} отсутствует в базе, но он находится на полке № {shelf_number}\n'
                      f'его необходимо добавить в базу, предварительно он будет стерт из полки')
            directories[new_shelf].remove(doc_number)
            print(f'Документ № {doc_number} удален с полки {shelf_number}')
            add_document(documents, directories)

    if input('Проверить еще документ? ').lower() in positive_answers:
        check_shelf(documents, directories)


def add_document(documents, directories):
    doc_type = input('Введите тип документа: ')
    doc_number = input('Введите номер документа: ')
    doc_owner = input('Введите имя владельца документа: ')
    if doc_number not in [x['number'] for x in documents]:
        if not any(doc_number in shelf for shelf in directories.values()):
            shelf_number = input('Введите номер полки для хранения документа:')
            if shelf_number in directories:
                directories[shelf_number].append(doc_number)
                documents.append({'type': doc_type, 'number': doc_number, 'name': doc_owner})
                print(f'Документ № {doc_number} добавлен в базу и размещен на полке {shelf_number}')
            else:
                if input('Указанной Вами полки нет в базе, добавить эту полку? ') in positive_answers:
                    directories[shelf_number] = [doc_number]
                    documents.append({'type': doc_type, 'number': doc_number, 'name': doc_owner})
                    print(f'{doc_type}№ {doc_number} добавлен в базу и размещен на полке {shelf_number}')
        else:
            for shelf_number in directories:
                if doc_number in directories[shelf_number]:
                    finded_derictory = shelf_number
            print(f'Документ № {doc_number} уже находится на полке {finded_derictory}')
            if input('Оставить его там? ') in positive_answers:
                documents.append({'type': doc_type, 'number': doc_number, 'name': doc_owner})
                print(f'Документ № {doc_number} добавлен в базу и размещен на полке {shelf_number}')
            shelf_number = input('Введите номер полки для перемещения документа:')
            if shelf_number not in directories:
                if input(f'Полки № {shelf_number} нет в картотеке, добавить? ') in positive_answers:
                    documents.append({'type': doc_type, 'number': doc_number, 'name': doc_owner})
                    directories[finded_derictory].remove(doc_number)
                    directories[shelf_number] = [doc_number]
                    print(f'Документ № {doc_number} перемещен на полку {shelf_number}')
    else:
        if not any(doc_number in shelf for shelf in directories.values()):
            if input('Разместить его на полке? ').lower() in positive_answers:
                shelf_number = input('Введите номер полки для хранения документа:')
                if shelf_number in directories:
                    directories[shelf_number].append(doc_number)
                    print(f'{doc_type}№ {doc_number} добавлен в базу и размещен на полке {shelf_number}')
                else:
                    if input(f'Полки №{shelf_number} нет в базе, добавить?') in positive_answers:
                        directories[shelf_number] = [doc_number]
                        print(f'{doc_type}№ {doc_number} добавлен в базу и размещен на полке {shelf_number}')
        else:
            for value in directories:
                if doc_number in directories[value]:
                    print(f'Документ № {doc_number} уже есть в базе находится на полке № {value}')


def list_all_docs(documents):
    for doc in documents:
        print(f'{doc["type"]} "{doc["number"]}" "{doc["name"]}"', )


def delete_document(documents, directories):
    doc_number = input('Введите номер документа для удаления ')
    if doc_number in [x['number'] for x in documents]:
        if any(doc_number in shelf for shelf in directories.values()):
            for doc in documents:
                if doc_number == doc['number']:
                    documents.remove(documents[documents.index(doc)])
            for shelf_number in directories:
                if doc_number in directories[shelf_number]:
                    directories[shelf_number].remove(doc_number)
                    print(f'Документ № {doc_number} удален с полки {shelf_number} и из базы')
        for doc in documents:
            if doc_number == doc['number']:
                documents.remove(documents[documents.index(doc)])
                print(f'Документ № {doc_number} удален')
    else:
        print(f'Документа {doc_number} нет в базе')
    if input('Еще раз? ').lower() in positive_answers:
        delete_document(documents, directories)


def moving_document(directions):
    doc_number = input('Введите номер документа для перемещения:')
    if any(doc_number in shelf for shelf in directories.values()):
        new_shelf_number = input('Введите новую полку:')
        if new_shelf_number in directories:
            for shelf, doc in directories.items():
                if doc_number in doc:
                    old_shelf = shelf
            directories[old_shelf].remove(doc_number)
            directories[new_shelf_number] = [doc_number]
            print(f'Документ № {doc_number} перемещен.')
        else:
            if input('Указанной вами полки нет в базе, добавить полку? '):
                for shelf, doc in directories.items():
                    if doc_number in doc:
                        old_shelf = shelf
                directories[new_shelf_number] = [doc_number]
                directories[old_shelf].remove(doc_number)
                print(f'Документ № {doc_number} перемещен.')
    else:
        print(f'Документа с номером {doc_number} нет на полках')
        if input('Добавить данный дкоумент? ') in positive_answers:
            add_document(documents, directions,doc_number)
    if input('Переместить другой документ?') in positive_answers:
        moving_document(directions)


def add_shelf(directories):
    new_shelf = input('Какую полку добавить? ')
    if new_shelf in directories:
        print(f'Полка № {new_shelf} уже есть')
    else:
        directories[new_shelf] = []
        print(f'Полка № {new_shelf} добавлена')
    if input('Добавить другую полку?').lower() in positive_answers:
        add_shelf(directories)


result = menu_list(menu)
while result != 'ex':
    if result == 'p':
        name_by_doc(documents)
        result = input('Введите команду ')
    elif result == 's':
        check_shelf(documents, directories)
        result = input('Введите команду ')
    elif result == 'l':
        list_all_docs(documents)
        result = input('Введите команду ')
    elif result == 'a':
        add_document(documents, directories)
        result = input('Введите команду ')
    elif result == 'd':
        delete_document(documents, directories)
        result = input('Введите команду ')
    elif result == 'm':
        moving_document(directories)
        result = input('Введите команду ')
    elif result == 'as':
        add_shelf(directories)
        result = input('Введите команду ')
    elif result == 'menu':
        result = menu_list(menu)
    else:
        print('Неверная команда')
        result = input('Введите команду ')
else:
    print('bye bye')
