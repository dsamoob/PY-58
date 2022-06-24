import requests
from pprint import pprint
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
    heroes_url = "https://akabab.github.io/superhero-api/api/all.json"
    heroes_list = ['Hulk', 'Captain America', 'Thanos']
    print(heroes_checking(heroes_url, heroes_list))

    TOKEN = ''
    file_name = ''
    disk_file_path = ''
    new_directory_name = ''
    file_name_for_deleting = ''
    ya = YandexDisk(token=TOKEN)

    pprint(ya.get_files_list())
    ya.upload_file_to_disk(disk_file_path=disk_file_path, filename=file_name)
    ya.make_new_directory(new_directory_name=new_directory_name)
    ya.delete_file(file_name_for_deleting=file_name_for_deleting)


