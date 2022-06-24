import requests
from pprint import pprint
import json
from YandexDisk import YandexDisk


def heroes_checking(url, heroes_list:list):
    response = requests.get(url).json()
    best_hero = ''
    best_brain = 0
    for name in heroes_list:
        for item in response:
            if name == item['name'] and best_brain < item['powerstats']['intelligence']:
                best_hero = item['name']
                best_brain = item['powerstats']['intelligence']
    return f'{best_hero} is the best becoz his "int" = {best_brain}'


if __name__ == '__main__':
    TOKEN =
    heroes_url = "https://akabab.github.io/superhero-api/api/all.json"
    heroes_list = ['Hulk', 'Captain America', 'Thanos']
    print(heroes_checking(heroes_url, heroes_list))

    ya = YandexDisk(token=TOKEN)
    ya.upload_file_to_disk(disk_file_path="/123/text.xls",
                           filename="/Users/egorbelov/GitHub/PY-58/dif_files/Recipe.txt")
    headers = {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {TOKEN}'
        }
    ya.make_new_directory('ubunthu')
    pprint(ya.get_files_list())
    ya.delete_file('Recipe3.txt')


