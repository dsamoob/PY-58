far_east_city = ['Благовещенск', 'Белогорск', 'Свободный', 'Завитинск', 'Зея', ' Райчихинск', 'Сковородино', 'Тында',
                 'Шимановск', 'Улан-Удэ', 'Бабушкин', 'Гусиноозёрск', 'Закаменск', 'Кяхта', 'Северобайкальск',
                 'Биробиджан', 'Облучье', 'Чита', 'Краснокаменск', 'Балей', 'Борзя', 'Могоча', 'Нерчинск',
                 'Петровск-Забайкальский', 'Сретенск', 'Хилок', 'Шилка', 'Петропавловск-Камчатский', 'Вилючинск',
                 'Елизово', 'Магадан', 'Сусуман', 'Владивосток', 'Уссурийск', 'Артём', 'Находка', 'Арсеньев',
                 'Большой Камень', 'Дальнегорск', 'Дальнереченск ', 'Лесозаводск', 'Партизанск', 'Спасск-Дальний',
                 'Фокино', 'Якутск', 'Нерюнгри', 'Алдан', 'Верхоянск', 'Вилюйск', 'Ленск', 'Мирный', 'Нюрба',
                 'Олёкминск', 'Покровск', 'Среднеколымск', 'Томмот', 'Удачный', 'Южно-Сахалинск',
                 'Александровск-Сахалинский', 'Анива', 'Долинск', 'Курильск', 'Макаров', 'Невельск', 'Оха',
                 'Поронайск', 'Северо-Курильск', 'Томари', 'Углегорск', 'Холмск', 'Шахтёрск', 'Корсаков',
                 'Хабаровск', 'Комсомольск-на-Амуре', 'Амурск', 'Бикин', 'Вяземский', 'Николаевск-на-Амуре',
                 'Советская Гавань', 'Анадырь', 'Билибино', 'Певек']

far_east_region = ['Амурская область', 'Республика бурятия', 'Еврейская автономная область', 'Забайкальский край',
                   'Камчатский край', 'Магаданская область', 'Приморский край', 'Республика Саха (Якутия)',
                   'Сахалинская область', 'Хабаровский Край', 'Чукотский автономный округ']


def region_searching(city, region, far_east_region, far_east_city):
    if city in far_east_city:
        return True
    elif region in far_east_region:
        return True
    else:
        return False


def answer_correction(input):
    input = input[0].upper() + input[1:].lower()
    return input


def str_to_int(input):
    calendar = {'Январь': 1, 'Февраль': 2, 'Март': 3, 'Апрель': 4, 'Май': 5, 'Июнь': 6, 'Июль': 7, 'Август': 8,
                'Сентябрь': 9, 'Октябрь': 10, 'Ноябрь': 11, 'Декабрь': 12}
    if input.isalpha():
        input = answer_correction(input)
        if input in calendar:
            return calendar[input]
    elif input.isdigit():
        return int(input)

def zodiac(day, month):
    if month == 1:
        if 0 < day <= 20:
            print('Козерог)')
        elif 21 <= day <= 31:
            print("Водолей")
    elif month == 2:
        if 0 < day <= 19:
            print('Водолей)')
        elif 20 <= day <= 29:
            print("Рыбы")
    elif month == 3:
        if 0 < day <= 20:
            print('Рыбы)')
        elif 21 <= day <= 31:
            print("Овен")
    elif month == 4:
        if 0 < day <= 20:
            print('Овен')
        elif 21 <= day <= 31:
            print("Телец")
    elif month == 5:
        if 0 < day <= 20:
            print('Телец')
        elif 21 <= day <= 31:
            print("Близнецы")
    elif month == 6:
        if 0 < day <= 21:
            print('Близнецы')
        elif 22 <= day <= 31:
            print("Рак")
    elif month == 7:
        if 0 < day <= 22:
            print('Рак')
        elif 23 <= day <= 31:
            print("Лев")
    elif month == 8:
        if 0 < day <= 23:
            print('Лев')
        elif 24 <= day <= 31:
            print("Дева")
    elif month == 9:
        if 0 < day <= 23:
            print('Дева')
        elif 24 <= day <= 31:
            print("Весы")
    elif month == 10:
        if 0 < day <= 23:
            print('Весы')
        elif 24 <= day <= 31:
            print("Скорпион")
    elif month == 11:
        if 0 < day <= 22:
            print('Скорпион')
        elif 23 <= day <= 31:
            print("Стрелец")
    elif month == 12:
        if 0 < day <= 21:
            print('Стрелец')
        elif 21 <= day <= 31:
            print("Козерог")
    else:
        print('Значит либо месяц либо число введены коряво')


if __name__ == '__main__':

    bank_rate = 17.5
    print(f'--Анкета для ипотечного кредитования--\n'
          f'--Ставка ЦБ РФ на момент заполнения заявки составляет {bank_rate} %--\n')
    region = answer_correction(input('Введите регион вашего проживания: '))
    city = answer_correction(input('Введите город вашего проживания: '))
    city_confirmation = input('Город проживания совпадает с регистрацией? (да/нет): ')

    childs = answer_correction(input('У вас есть дети? (да/нет) '))
    if childs == 'Да':
        children_quantity = int(input('Сколько к вас детей? (цифрой): '))
        if children_quantity > 3:
            bank_rate -= 1
    else:
        children_quantity = 0
    bank_user = answer_correction(input('Являетесь ли вы клиентом банка? (да/нет) '))
    if bank_user == 'Да':
        salary_project = answer_correction(input('Зарплатный проект в данном банке? (да/нет) '))
        if salary_project == 'Да':
            bank_rate -= 0.5
    insurance = answer_correction(input('Страхование кредита будет оформленно в данном банке? (да/нет) '))
    if insurance == 'Да':
        bank_rate -= 1.5
    if region_searching(city, region, far_east_region, far_east_city):
        bank_rate = 2
        print(f'Так как город вашего проживания относитеся к дальнему востоку процентная ставка по ипотеке составит '
              f'{bank_rate} %')
    else:
        print(f'Согласно информации из вашей анкеты процентная ставка по кредиту составит {bank_rate} %')

    print(f'-----Задача 2-----')
    month = str_to_int(input('Введите месяц рождения:  '))
    day = str_to_int(input('Введите число рождения:  '))
    zodiac(day, month)


