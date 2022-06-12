class Student:
    st_list = []  # список студентов по всему классу
    st_grades = {}  # словарь из студентов, с сортировкой по языку и с указанием отметок

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished = {}
        self.act_courses = {}
        if self.name + ' ' + self.surname not in Student.st_list:  # в перспективе, при большом обьеме - есть риск повторения имени
            Student.st_list.append([name + ' ' + surname])
        else:
            print('такое имя уже есть')

    def __str__(self):  #
        middle = self.middle_grade_stud()  # использует метод от self
        courses = [i for i in self.act_courses]
        finished = self.finished
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {middle}\n' \
               f'Курсы в процессе обучения: {", ".join([str(x) for x in [*courses]])}\nЗавершенные курсы:  ' \
               f'{", ".join([str(x) for x in [*finished]])}'  # есть еще вариант распаковки списка в ф - str(finished)[1:-2]

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Плохой кандидат для сравнения')
            return
        if self.middle_grade_stud() > other.middle_grade_lect():
            return f'{self.name} круче чем {other.name}'
        else:
            return f'{self.name} не круче чем {other.name}'

    def middle_grade_stud(self):  # Данный метод сделан для селфа и используется в str
        middle = (sum([sum(i) for i in list(self.act_courses.values())]) + sum(
            [sum(i) for i in list(self.finished.values())])) / \
                 (len([len(i) for i in list(self.act_courses.values())]) + len(
                     [len(i) for i in list(self.finished.values())]))
        return middle

    def middle_grade(course):   # Данная функция сделанна без селва, чтобы ее можно было вызывать на весь класс не через селф
        if course in Student.st_grades:
            marks_quantity = 0
            marks_sum = 0
            for mark in range(1, len(Student.st_grades[course]), 2):  # Перебор согласно словарю. т.к. после имени идет список
                marks_quantity += len(Student.st_grades[course][mark])
                marks_sum += sum(Student.st_grades[course][mark])
            if marks_quantity != 0:
                print(f'Средний бал среди всех студентов по курсу {course} {marks_sum / marks_quantity}')
            else:
                print('Нет оценок')
        else:
            print('Ошибка')

    def add_course(self, course):  # Добавление курса к студенту, планировал сделать проверку на пробелы и расстановки
        course = course.capitalize()  # Далее 3 if для
        if course not in self.act_courses:
            self.act_courses[course] = []
        if course not in Student.st_grades:
            Student.st_grades[course] = [self.name + ' ' + self.surname, []]  # Добавляет имя и список для оценлк
        if self.name + ' ' + self.surname not in Student.st_grades[course]:
            Student.st_grades[course].append(self.name + ' ' + self.surname)
            Student.st_grades[course].append([])

    def finish_course(self, course):  # закончить курс
        if course in self.act_courses:
            self.finished[course] = self.act_courses[course].copy()  # добавил копию т.к. побоялся ошибки (не проверял)
            del self.act_courses[course]
        else:
            print('Ошибка')

    def mark_to_lecturer(self, lecturer, course, mark):  # регистрирует оценку и в лекторе и селфе лектора и в самом классе
        course = course.capitalize()
        if course in self.act_courses:
            if course in lecturer.courses and course in lecturer.grades:
                lecturer.grades[course].append(mark)
                Lecturer.lect_courses[course][list(Lecturer.lect_courses[course]).index(lecturer.name + ' ' + lecturer.surname) + 1].append(mark)
            else:
                print(f'Преподаватель не относится к курсу {course}')
        else:
            print(f'У студента не такого курса')


class Mentor:
    men_list = []   # Список поименно

    def __init__(self, name, surname, course):
        self.name = name
        self.surname = surname
        self.course = course.capitalize()
        if name + ' ' + surname not in Mentor.men_list:
            Mentor.men_list.append(name + ' ' + surname)


class Lecturer(Mentor):
    lect_courses = {}
    lect_list = []

    def __init__(self, name, surname, course):
        super().__init__(name, surname, course)
        self.grades = {}
        self.courses = [self.course]  # не делал капиталайз т.к. в родителе делается
        self.grades[self.course] = []
        if self.name + ' ' + self.surname not in Lecturer.lect_list:
            Lecturer.lect_list.append(self.name + ' ' + self.surname)
        if self.course not in Lecturer.lect_courses:
            Lecturer.lect_courses[self.course] = [self.name + ' ' + self.surname, []]
        if self.name + ' ' + self.surname not in Lecturer.lect_courses[self.course]:
            Lecturer.lect_courses[self.course].append(self.name + ' ' + self.surname)
            Lecturer.lect_courses[self.course].append([])

    def __str__(self):
        middle = self.middle_grade_lect()  # по аналогии с методом в Student
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {middle}'

    def middle_grade_lect(self):  # Исправил вычисление средней.
        middle = sum([sum(i) for i in self.grades.values()])
        m2 = []
        [[m2.append(i) for i in b] for b in self.grades.values()]
        return middle / len(m2)

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Плохой кандидат для сравнения')
            return
        if self.middle_grade_lect() > other.middle_grade_stud():
            return f'{self.name} круче чем {other.name}'
        else:
            return f'{other.name} круче чем {self.name}'

    def add_course(self, course):
        course = course.capitalize()
        if course not in self.courses:
            self.courses.append(course)
        if course not in Lecturer.lect_courses:
            Lecturer.lect_courses[course] = [self.name + ' ' + self.surname, []]
        if self.name + ' ' + self.surname not in Lecturer.lect_courses[course]:
            Lecturer.lect_courses[course].append(self.name + ' ' + self.surname)
            Lecturer.lect_courses[course].append([])
        if course not in self.grades:
            self.grades[course] = []

    def middle_grade(course):
        if course in Lecturer.lect_courses:
            marks_quantity = 0
            marks_sum = 0
            for mark in range(1, len(Lecturer.lect_courses[course]), 2):
                marks_quantity += len(Lecturer.lect_courses[course][mark])

                marks_sum += sum(Lecturer.lect_courses[course][mark])
            if marks_quantity != 0:
                print(f'Средний бал среди всех лекторов по курсу {course}: {marks_sum / marks_quantity}')
            else:
                print('Нет оценок')
        else:
            print('Ошибка')


class Reviewer(Mentor):
    rev_courses = {}
    rev_list = []

    def __init__(self, name, surname, course):
        super().__init__(name, surname, course)
        self.grades = {}
        self.courses = [self.course]
        if self.name + ' ' + self.surname not in Reviewer.rev_list:
            Reviewer.rev_list.append(self.name + ' ' + self.surname)
        if self.course not in Reviewer.rev_courses:
            Reviewer.rev_courses[self.course] = [self.name + ' ' + self.surname, []]
        if self.name + ' ' + self.surname not in Reviewer.rev_courses[self.course]:
            Reviewer.rev_courses[self.course].append(self.name + ' ' + self.surname)
            Reviewer.rev_courses[self.course].append([])

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

    def add_course(self, course):
        if course not in self.courses:
            self.courses.append(course)
        if course not in Reviewer.rev_courses:
            Reviewer.rev_courses[course] = [self.name + ' ' + self.surname, []]
        if self.name + ' ' + self.surname not in Reviewer.rev_courses[course]:
            Reviewer.rev_courses[course].append(self.name + ' ' + self.surname)
            Reviewer.rev_courses[course].append([])

    def mark_to_student(self, student, course, grade):
        course = course.capitalize()
        if isinstance(student, Student) and course in self.courses and course in student.act_courses:
            if course in student.act_courses and course in Student.st_grades:
                student.act_courses[course].append(grade)
                Student.st_grades[course][list(Student.st_grades[course]).index(student.name + ' ' + \
                    student.surname) + 1].append(grade)
                Reviewer.rev_courses[course][list(Reviewer.rev_courses[course]).index(self.name + ' ' + self.surname) + 1].append(grade)
            else:
                print('Несоответствие курсов1')
        else:
            print('Несоответствие курсов2')


if __name__ == '__main__':
    # students registration
    st1, st2, st3, st4 = Student('Ruoy', 'Eman'), Student('Bobby', 'Dilan'), Student('Nikolay', 'Krog'), \
                         Student('Gleb', 'Trofimov')
    st1.add_course('Python')
    st2.add_course('C++')
    st3.add_course('Java')
    st4.add_course('Python')
    st1.add_course('Java')  # Добавление нового курса студенту
    st3.add_course('Git')  # Добавление нового курса студенту

    # Lecturers registration
    th1 = Lecturer('Aleksandr', 'Buddy', 'Python')
    th2 = Lecturer('Artem', 'Bistrov', 'Python')
    th3 = Lecturer('Sergei', 'Ivanov', 'C++')
    th4 = Lecturer('Vasya', 'Pupkin', 'Java')
    th4.add_course('Python')  # Добавление нового направления лектору
    th3.add_course('Git')  # Добавление нового направления лектору

    # Reviwers registration
    r1 = Reviewer('Michael', 'Zetta', 'Python')
    r2 = Reviewer('Timur', 'Vagubov', 'Python')
    r3 = Reviewer('Oleg', 'Sokolov', 'C++')
    r4 = Reviewer('Andrey', 'Rhanov', 'Java')

    # testing
    r1.mark_to_student(st1, 'Python', 5)  # оценка студента 1 по питону + проверка capitalize()
    r1.mark_to_student(st4, 'Python', 8)  # Оценка студента 4 по питону
    r2.mark_to_student(st1, 'Python', 4)  # Оценка студена 1 по питону
    r3.mark_to_student(st2, 'C++', 7)  # Оценка студента 2 по С++
    r4.mark_to_student(st1, 'Java', 3)  # Оценка студента 2 по Java
    st1.mark_to_lecturer(th1, 'Python', 4)  # Оценка лектора по питону
    st1.mark_to_lecturer(th4, 'Java', 3)  # Оценка лектора по джаве
    st2.mark_to_lecturer(th3, 'C++', 6)  # Оценка лектора по С++
    st1.mark_to_lecturer(th4, 'Python', 3)  # Оценка лектора по питону (лектору был добавлен доп курс

    # Проверка __str__
    # print(st2)
    # print(st3)
    # print(st1)
    # st1.finish_course('Python')  # Для сравнения результата
    # print(st1)  # Показывает среднюю оценку по дз за текущие курсы и за те, которые завершил
    # print(th1)
    # print(th3)
    # print(r2)

    # Вывод средних
    # Student.middle_grade('Python')
    # Student.middle_grade('Java')
    # Lecturer.middle_grade('Python')
    # Lecturer.middle_grade('C++')
    # Lecturer.middle_grade('Git')
    # print(th1.middle_grade_lect())
    # print(st1.middle_grade_stud())
    # print(Student.st_grades)  # Выводит всех студентов с сортировкой по курсам с оценками
    # print(Student.st_list)  # Список всех студентов
    # print(Mentor.men_list) # Список всех преподавателей
    # print(Lecturer.lect_courses)  # Список лекторов с сортировкой по курсам и оценкам
    # print(Lecturer.lect_list)  # Простой список лекторов
    # print(Reviewer.rev_courses)  # Список ревьюеров по курсам и с оценками, с оценками, которые они проставляли
    # print(Reviewer.rev_list)  # Простой список ревьеров
    # print(th3.grades)
    # print(st3.middle_grade_stud()) # средние оценки у студента
    # print(th3.middle_grade_lect())  #  Используется логика средней на курсы (1 оценка по с++ -6 и нет оценок по гиту итого 3
    # print(th1.__lt__(st3))  # сравниваем одних и тех-же
    # print(st3.__lt__(th1)) # сравниваем одних и тех-же

