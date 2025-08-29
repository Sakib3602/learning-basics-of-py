import random
from school import School


class Person:
    def __init__(self, name):
        self.name = name


class Teacher(Person):
    def __init__(self, name):
        super().__init__(name)

    def evaluate_exam(self):
        return random.randint(1, 100)

    def teach(self):
        pass


class Student(Person):
    def __init__(self, name, classroom):
        super().__init__(name)
        self.classroom = classroom
        self.marks = {}
        self.subject_grade = {}  # {"eng": 90,"bangla" : 90}
        self.grade = None
        self.__id = None

    def calculate_final_grade(self):
        sum = 0
        for g in self.subject_grade.values():
            point = School.grade_to_value(g)  # 4.00
            sum += point
        gpa = sum / len(self.subject_grade)
        self.grade = School.grade_to_value(gpa)

    # getter
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self,val):
        self.__id = val
