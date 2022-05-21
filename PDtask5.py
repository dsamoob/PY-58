documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}
# p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
# s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
# l – list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
# a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип,
# имя владельца и номер полки, на котором он будет храниться
# d – delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок.
# m – move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую.
# as – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень.

positive_answers = ['да', '']

def check_doc_number(documents):
    doc_number = input('Введите номер документа: ')
    owner_name = None
    if doc_number in list(map(lambda x: x['numbers'], documents)):
    # for i in documents:
    #     if doc_number in i.values():
        owner_name = i['name']

    if owner_name != None:
        print(owner_name)
        one_more_time = input('Будете еще искать? yes/no ')
        if one_more_time == 'yes':
            check_doc_number(documents)
        else:
            return 'navigation'
    elif owner_name == None:
        print(f'Документа с номером {doc_number} нет в списке.')
        one_more_time = input('Попробовать еще раз? yes/no ').lower()
        if one_more_time == 'yes':
            check_doc_number(documents)
        else:
            return 'navigation'



check_doc_number(documents)
