def acquaintance(first_list, second_list):
    if len(first_list) == len(second_list):
        for i, j in list(zip(sorted(first_list), sorted(second_list))):
            print(f'{i} и {j}')
    else:
        print(f'Списки разного размера - не получится спарить')
    print(f'\n')

def ingredients_calculation(persons):
    cook_book = [['салат', [
        ['картофель', 100, 'гр.'],
        ['морковь', 50, 'гр.'],
        ['огурцы', 50, 'гр.'],
        ['горошек', 30, 'гр.'],
        ['майонез', 70, 'мл.'], ]],
                 ['пицца',
                  [
                      ['сыр', 50, 'гр.'],
                      ['томаты', 50, 'гр.'],
                      ['тесто', 100, 'гр.'],
                      ['бекон', 30, 'гр.'],
                      ['колбаса', 30, 'гр.'],
                      ['грибы', 20, 'гр.'],
                  ],
                  ],
                 ['фруктовый десерт',
                  [
                      ['хурма', 60, 'гр.'],
                      ['киви', 60, 'гр.'],
                      ['творог', 60, 'гр.'],
                      ['сахар', 10, 'гр.'],
                      ['мед', 50, 'мл.'],
                  ]
                  ]
                 ]

    for i, j in cook_book:
        print('\n', i.capitalize(), sep='')
        for name, volume, gr in j:
            print(f'{name} {volume * persons} {gr}')


if __name__ == '__main__':
    first_list = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
    second_list = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
    acquaintance(first_list, second_list)
    ingredients_calculation(int(input('Введите количество персон: ')))
