square = int(input('Введите длинну стороны квадрата: '))
print(f'\nВывод:\nПериметр: {square * 4}\nПлощадь: {square * square}')
print()
rect_length = int(input('Введите длинну прямоугольника: '))
rect_width = int(input('Введите ширину прямоугольника: '))
print(f'\nВывод:\nПериметр: {(rect_length * 2) + (rect_width * 2)}\nПлощадь: {rect_length * rect_width}')
sep_line = input('Введите любой символ: ')
print(f'\n{sep_line * (square * 4 + rect_length * rect_width)}\n')
salary = float(input('Введите заработную плату в месяц: '))
flat_percentage = float(input('Введите, какой процент(%) уходит на ипотеку: '))
life_percentage = float(input('Введите, какой процент(%) уходит на жизнь: '))
print(f'\nВывод:\n'
      f'На ипотеку было потрачено: {int((salary * 12 / 100) * flat_percentage)}\n'
      f'Было накоплено: {int(salary * 12 - ((salary * 12 / 100) * (flat_percentage + life_percentage)))}')

#how to control