geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]

ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт',

]
stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}
inc = ['2018-01-01', 'yandex', 'cpc', 100, '2018-02-02', 'google', 'cpc', 100]


def locations(geo_logs):
    del_list = []
    for i in geo_logs:
        for key, value in i.items():
            if 'Россия' not in value:
                del_list.append(geo_logs.index(i))
    for i in del_list[::-1]:
        del geo_logs[i]
    return geo_logs

a = 'bbbb'
def exceptions(ids):
    x = []
    [[x.append(k) for k in a] for a in ids.values()]
    return list(set(x))


def percentage_of_words(queries):
    results = []
    for i in queries:
        results.append(len(i.split()))
    for i in list(set(results)):
        print(f'Поисковых запросов из {i} слов {float(results.count(i) / (len(results) / 100))}%')


def best_sales(stats):
    for i, k in stats.items():
        if k == max(stats.values()):
            return i
    else:
        return 'Нету лучших'


def list_to_dict(args):
    start = args[len(args)-1]
    c = {}
    for i in reversed(range(len(args)-1)):
        c[args[i]] = start
        start = c.copy()
        c.clear()
    return start


def task_number(task):
    print(f'{"-" * 15}Задача № {task}{"-" * 15}')


if __name__ == '__main__':
    task_number(1)
    print(locations(geo_logs))
    task_number(2)
    print(exceptions(ids))
    task_number(3)
    percentage_of_words(queries)
    task_number(4)
    print(best_sales(stats))
    task_number(5)
    print(list_to_dict(inc))
