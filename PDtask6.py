class Student:
    list = []  # Список студентов по всему классу
    courses = {}  # Словарь из студентов с расстановкой "Язык": [имя и фамилия студента, [оценки], ....etc]

    def __init__(self, name, surname):
            self.name = name
            self.surname = surname
            self.finished = {}
            self.act_courses = {}
            Student.list.append(f'{name} {surname}')  # убрал проверку - лишнее в данной задаче.

    def __str__(self):  #
        middle = self.middle_grade_stud()  # использует метод от self
        act_courses = [i for i in self.act_courses]
        finished = self.finished
        return f'Имя: {self.name}\nФамилия: {self.surname}\n' \
               f'Средняя оценка за домашние задания: {middle}\n' \
               f'Курсы в процессе обучения: {", ".join([str(x) for x in [*act_courses]])}\n' \
               f'Завершенные курсы:  ' \
               f'{", ".join([str(x) for x in [*finished]])}'

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return 'Плохой кандидат для сравнения'
        if isinstance(self.middle_grade_stud(), float) and isinstance(other.middle_grade_lect(), float):
            if self.middle_grade_stud() > other.middle_grade_lect():
                return f'{self.name} круче чем {other.name}'
            return f'{other.name} круче чем {self.name}'
        elif not isinstance(self.middle_grade_stud(), float) and isinstance(other.middle_grade_lect(), float):
            return f'{other.name} круче чем {self.name}'
        return f'{self.name} круче чем {other.name}'

    def middle_grade_stud(self):  # Исправил порядок расчета средней т.к. в предыдущей версии путой список считался бы как за 0
        middle = sum([sum(i) for i in list(self.act_courses.values())]) + \
                 sum([sum(i) for i in list(self.finished.values())])
        m2 = []
        [[m2.append(i) for i in b] for b in self.act_courses.values()]
        if len(m2) != 0:
            return middle / len(m2)
        else:
            return f'У студента {self.name} нет оценок'

    def add_course(self, course):  # Добавление курса к студенту, планировал сделать проверку на пробелы и расстановки
        course = course.capitalize()  # Далее 3 if для
        if course not in self.act_courses:
            self.act_courses[course] = []
        if course not in Student.courses:
            Student.courses[course] = [f'{self.name} {self.surname}', []]  # Добавляет имя и список для оценок
        if f'{self.name} {self.surname}' not in Student.courses[course]:
            Student.courses[course].append(f'{self.name} {self.surname}')
            Student.courses[course].append([])

    def finish_course(self, course):  # закончить курс
        if course in self.act_courses:
            self.finished[course] = self.act_courses[course]
            del self.act_courses[course]
        else:
            return 'Ошибка'

    def grade_to_lecturer(self, lecturer, course, grade):  # Регистрирует оценку и в группе лекторов и в селфе лектора
        course = course.capitalize()
        if course in self.act_courses:
            if course in lecturer.courses and course in Lecturer.courses:
                lecturer.courses[course].append(grade)
                Lecturer.courses[course][list(Lecturer.courses[course]).index(f'{lecturer.name} {lecturer.surname}') + 1].append(grade)
                return f'Студент {self.name} поставил лектору {lecturer.name} {grade} по предмету {course}'
            else:
                return f'Преподаватель {lecturer.name} {lecturer.surname} не относится к курсу {course}'
        else:
            return f'У студента не такого курса'


class Mentor:
    men_list = []   # Список поименно

    def __init__(self, name, surname, course):  # Убрал проверку т.к.  она лишняя в данной задаче
        self.name = name
        self.surname = surname
        self.course = course.capitalize()
        Mentor.men_list.append(f'{self.name} {self.surname}')


class Lecturer(Mentor):
    courses = {}
    list = []

    def __init__(self, name, surname, course):
        super().__init__(name, surname, course)
        self.courses = {self.course: []}
        Lecturer.list.append(f'{self.name} {self.surname}')
        if self.course not in Lecturer.courses:
            Lecturer.courses[self.course] = [f'{self.name} {self.surname}', []]
        if f'{self.name} {self.surname}' not in Lecturer.courses[self.course]:
            Lecturer.courses[self.course].append(f'{self.name} {self.surname}')
            Lecturer.courses[self.course].append([])

    def __str__(self):
        middle = self.middle_grade_lect()  # по аналогии с методом в Student
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за лекции: {middle}'

    def middle_grade_lect(self):  # Исправил вычисление средней.
        middle = sum([sum(i) for i in self.courses.values()])
        m2 = []
        [[m2.append(i) for i in b] for b in self.courses.values()]
        if len(m2) != 0:
            return middle / len(m2)
        else:
            return f'У лектора {self.name} нет оценок'

    def __lt__(self, other):
        if not isinstance(other, Student):
            return f' Плохой кандидат для сравнения'  # сократил
        if isinstance(self.middle_grade_lect(), float) and isinstance(other.middle_grade_stud(), float):
            if self.middle_grade_lect() > other.middle_grade_stud():
                return f'{self.name} круче чем {other.name}'
            return f'{other.name} круче чем {self.name}'
        elif not isinstance(self.middle_grade_lect(), float) and isinstance(other.middle_grade_stud(), float):
            return f'{other.name} круче чем {self.name}'
        return f'{self.name} круче чем {other.name}'

    def add_course(self, course):
        course = course.capitalize()
        if course not in self.courses:
            self.courses[course] = []
        if course not in Lecturer.courses:
            Lecturer.courses[course] = [f'{self.name} {self.surname}', []]
        if f'{self.name} {self.surname}' not in Lecturer.courses[course]:
            Lecturer.courses[course].append(f'{self.name} {self.surname}')
            Lecturer.courses[course].append([])


class Reviewer(Mentor):
    courses = {}
    list = []

    def __init__(self, name, surname, course):
        super().__init__(name, surname, course)
        self.courses = {self.course: []}
        Reviewer.list.append(f'{self.name} {self.surname}')
        if self.course not in Reviewer.courses:
            Reviewer.courses[self.course] = [f'{self.name} {self.surname}', []]
        if self.name + ' ' + self.surname not in Reviewer.courses[self.course]:
            Reviewer.courses[self.course].append(f'{self.name} {self.surname}')
            Reviewer.courses[self.course].append([])

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

    def add_course(self, course):
        if course not in self.courses:
            self.courses.append(course)
        if course not in Reviewer.courses:
            Reviewer.courses[course] = [f'{self.name} {self.surname}', []]
        if self.name + ' ' + self.surname not in Reviewer.courses[course]:
            Reviewer.courses[course].append(f'{self.name} {self.surname}')
            Reviewer.courses[course].append([])

    def grade_to_student(self, student, course, grade):  # в список оценок оценщика вписывается студент, которому он поставил оценку)
        course = course.capitalize()
        if isinstance(student, Student) and course in self.courses and course in student.act_courses:
            if course in student.act_courses and course in Student.courses:
                student.act_courses[course].append(grade)
                # сложное вычисление т.к. основной словарь Student.courses состоит из 'язык':[имя1, [оценки], имя2, [оценки]] и нужен поиск именно списка следующего после имени.
                Student.courses[course][list(Student.courses[course]).index(f'{student.name} {student.surname}') + 1].append(grade)
                Reviewer.courses[course][list(Reviewer.courses[course]).index(f'{self.name} {self.surname}') + 1].append(grade)
                self.courses[course].append(f'{student.name} {student.surname}')
                self.courses[course].append([])
                self.courses[course][self.courses[course].index(f'{student.name} {student.surname}')+1].append(grade)
                return f'Лектор {self.name} поставил студенту {student.name} {grade} по предмету {course}'
            else:
                return 'Несоответствие курсов'
        else:
            return 'Несоответствие курсов'


def middle_grade(group, course):  # Функция для средних оценок по группам (Студенты, Лекторы, Проверяющие)
    print(group.courses)
    if course in group.courses:
        marks_quantity = 0
        marks_sum = 0
        for mark in range(1, len(group.courses[course]), 2):
            marks_quantity += len(group.courses[course][mark])
            marks_sum += sum(group.courses[course][mark])
        if marks_quantity != 0:
            return f'Средний бал среди всех по курсу {course} составляет {marks_sum / marks_quantity}'
        else:
            return 'Нет оценок'
    else:
        return f'Курса {course} нет в списке'


if __name__ == '__main__':
    # students registration
    st1 = Student('Ruoy', 'Eman')
    st2 = Student('Bobby', 'Dilan')
    st3 = Student('Nikolay', 'Krog')
    st4 = Student('Gleb', 'Trofimov')

    st1.add_course('Python')
    st1.add_course('Java')  # Добавление нового курса студенту
    st2.add_course('C++')
    st3.add_course('Java')
    st3.add_course('Git')  # Добавление нового курса студенту
    st4.add_course('Python')
    st4.add_course('Java')

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
    r5 = Reviewer('Alexandr', 'Baykov', 'Java')

    # testing
    print(r1.grade_to_student(st1, 'Python', 5))  # оценка студента 1 по питону + проверка capitalize()
    print(r1.grade_to_student(st4, 'Python', 8))  # Оценка студента 4 по питону
    print(r2.grade_to_student(st1, 'Python', 4))  # Оценка студена 1 по питону
    print(r2.grade_to_student(st4, 'Python', 7))
    print(r3.grade_to_student(st2, 'C++', 7))  # Оценка студента 2 по С++
    print(r4.grade_to_student(st1, 'Java', 3))  # Оценка студента 2 по Java

    print(st1.grade_to_lecturer(th1, 'Python', 4))  # Оценка лектора по питону
    print(st1.grade_to_lecturer(th4, 'Java', 3))  # Оценка лектора по джаве
    print(st1.grade_to_lecturer(th4, 'Python', 3))  # Оценка лектора по питону (лектору был добавлен доп курс
    print(st2.grade_to_lecturer(th3, 'C++', 6))  # Оценка лектора по С++
    print(st3.grade_to_lecturer(th3, 'Git', 7))
    print(st4.grade_to_lecturer(th2, 'python', 5))

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

    # print(middle_grade(Lecturer, 'Python'))  # Тест функции по средним для группы
    # print(middle_grade(Reviewer, 'Python')) # Тест функции по средним для группы
    # print(middle_grade(Student, 'Java')) # Тест функции по средним для группы
    # print(th1.middle_grade_lect())  # Средний бал по лектору
    # print(th3.middle_grade_lect())  # Средний бал по лектору
    # print(st1.middle_grade_stud())  # Средний бал по студенту

    # print(Student.courses)  # Выводит всех студентов с сортировкой по курсам с оценками
    # print(Student.list)  # Список всех студентов
    # print(Mentor.men_list) # Список всех преподавателей
    # print(Lecturer.courses)  # Список лекторов с сортировкой по курсам и оценкам
    # print(Lecturer.list)  # Простой список лекторов
    # print(Reviewer.courses)  # Список ревьюеров по курсам и с оценками, с оценками, которые они проставляли
    # print(Reviewer.list)  # Простой список ревьеров

    # print(st3.act_courses)
    # print(st3.middle_grade_stud()) # средние оценки у студента
    # print(th1.middle_grade_lect())  # средняя оценка у лектора
    # print(th2.middle_grade_lect())  # средняя оценка у лектора
    # print(th3.middle_grade_lect())  # средняя оценка у лектора
    print(th4.middle_grade_lect())  # средняя оценка у лектора
    # print(th1.__lt__(st3))  # сравниваем одних и тех-же
    # print(st3.__lt__(th1)) # сравниваем одних и тех-же
    # print(st2.__lt__(th1))  # сравниваем одних и тех-же
    # print(st1.__lt__(th4)) # сравниваем одних и тех-же
