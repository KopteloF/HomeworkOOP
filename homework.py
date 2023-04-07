class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        courses_in_progress = ", ".join(self.courses_in_progress)
        finished_courses = ", ".join(self.finished_courses)
        avg_grade = sum(sum(self.grades.values(), [])) / len(sum(self.grades.values(), []))
        return f'Студент\nИмя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {avg_grade:.1f}\nКурсы в процессе изучения: {courses_in_progress}\nЗавершенные курсы: {finished_courses}'

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        avg_grade = sum(sum(self.grades.values(), [])) / len(sum(self.grades.values(), []))
        return f'Лектор\nИмя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {avg_grade:.1f}'

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        
        return f'Имя: {self.name}\nФамилия: {self.surname}'

students = [Student('Ruoy', 'Eman', 'your_gender'), Student('Tommy', 'Andgello', 'your_gender'), Student('James', 'Gandolfini', 'your_gender')]

students[0].courses_in_progress += ['Python']
students[0].finished_courses += ['GIT', 'Introduction to programming']
students[1].courses_in_progress += ['Python']
students[1].finished_courses += ['GIT', 'Introduction to programming']
students[2].courses_in_progress += ['Python']
students[2].finished_courses += ['GIT', 'Introduction to programming']

mentors = [Reviewer('Some', 'Buddy'), Reviewer('Michael', 'Impiriolli'), Reviewer('Natan', 'Filion')]
mentors[0].courses_attached += ['Python']
mentors[1].courses_attached += ['Python']
mentors[2].courses_attached += ['Python']

lecturers = [Lecturer('Tom', 'Smith'), Lecturer('Alan', 'Tudyk'), Lecturer('Pedro', 'Pascal')]
lecturers[0].courses_attached += ['Python']
lecturers[1].courses_attached += ['Python']
lecturers[2].courses_attached += ['Python']

mentors[0].rate_hw(students[0], 'Python', 8)
mentors[1].rate_hw(students[1], 'Python', 9)
mentors[2].rate_hw(students[2], 'Python', 10)

students[0].rate_lecture(lecturers[0], 'Python', 8)
students[0].rate_lecture(lecturers[1], 'Python', 9)
students[0].rate_lecture(lecturers[2], 'Python', 10)

def course_avg_grade(course):
    grades = []
    for student in students:
        if course in student.grades.keys():
            grades += student.grades[course]
    if len(grades) > 0:
        return sum(grades) / len(grades)
    else:
        return 0

def lecturer_avg_grade(course):
    grades = []
    for lecturer in lecturers:
      if course in lecturer.grades.keys():
        grades += lecturer.grades[course]
    if len(grades) > 0:
        return sum(grades) / len(grades)
    else:
        return 0
      
print('Проверяющие')
print(mentors[0])
print(mentors[1])
print(mentors[2])

sorted_lecturer = sorted(lecturers, key=lambda lecturer: sum(sum(lecturer.grades.values(), [])) / len(sum(lecturer.grades.values(), [])), reverse=True)
best_lecturer = sorted_lecturer[0]

print(best_lecturer)

sorted_students = sorted(students, key=lambda student: sum(sum(student.grades.values(), [])) / len(sum(student.grades.values(), [])), reverse=True)
best_student = sorted_students[0]

print(best_student)

print(f"Средняя оценка на курсе: {course_avg_grade('Python'):.1f}")

print(f"Средняя оценка у лекторов: {lecturer_avg_grade('Python'):.1f}")





