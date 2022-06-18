import os
from pprint import pprint


def strings_counting(file: str) -> int:
    with open(file, 'r') as f:
        return sum(1 for _ in f)


def catalog_reader(file_name: str) -> dict:
    with open(file_name) as file:
        dict = {}
        for line in file:
            dish_name = line.strip()
            dict[dish_name] = []
            for j in range(int(file.readline())):
                consist = file.readline().split(' | ')
                dict[dish_name].append({'ingredient_name': consist[0],
                                        'quantity': int(consist[1]),
                                        'measure': consist[2].strip()})
            file.readline()
    return dict


def shop_list_by_dishes(dishes: list, person_count: int, cook_book: dict) -> dict:
    result = {}
    for dish in dishes:
        if dish in cook_book:
            for consist in cook_book[dish]:
                if consist['ingredient_name'] in result:
                    result[consist['ingredient_name']]['quantity'] += consist['quantity'] * person_count
                else:
                    result[consist['ingredient_name']] = {'measure': consist['measure'],
                                                          'quantity': (consist['quantity'] * person_count)}
        else:
            print(f'Блюда "{dish}" нет в книге рецептов')
            pass
    return result


def rewriting(file_for_writing: str, base_path, location):
    files = [[strings_counting(os.path.join(base_path, location, i)), os.path.join(base_path, location, i), i]
             for i in list(os.listdir(base_path + '/' + location))]
    for file_from_list in sorted(files):
        w_to = open(file_for_writing, 'a')
        w_to.write(f'{file_from_list[2]}\n')
        w_to.write(f'{file_from_list[0]}\n')
        with open(file_from_list[1], 'r') as file:
            counting = 1
            for line in file:
                w_to.write(f'строка № {counting} в файле {file_from_list[2]} : {line}')
                counting += 1
        w_to.write(f'\n')
        w_to.close()


if __name__ == '__main__':
    file_with_recipes = '/Users/egorbelov/GitHub/PY-58/dif_files/Recipe.txt'
    dishes = ['Омлет', 'Фахитос', 'Селедь под шубой', 'Запеченный картофель']
    pprint(catalog_reader(file_with_recipes))  # 1st task result
    pprint(shop_list_by_dishes(dishes, 2, catalog_reader(file_with_recipes)))  # 2nd task result
    file_for_writing = '/Users/egorbelov/GitHub/PY-58/dif_files/result.txt'
    base_path = os.getcwd()
    location = 'txts_for_PDtask7'
    rewriting(file_for_writing, base_path, location)  # 3rd task result
