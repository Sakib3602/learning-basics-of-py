class School:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.teachers = {}
        self.classrooms = {}

    def add_classroom(self, classroom):
        self.classrooms[classroom.name] = classroom

    def add_teacher(self, subject, teacher):
        self.teacher[subject] = teacher

    def student_admission(self, student):
        className = student.classroom.name
        self.classrooms[className].add_student(student)

    @staticmethod
    def calculate_grade(marks):
        if marks >= 80 and marks <= 100:
            print("A+")
        elif marks >= 60 and marks <= 79:
            print("A")
        elif marks >= 50 and marks <= 59:
            print("B")
        elif marks >= 40 and marks <= 49:
            print("C")
        elif marks >= 33 and marks <= 39:
            print("D")
        elif marks >= 0 and marks <= 32:
            print("F")
        else:
            print("Invalid marks")

    @staticmethod
    def grade_to_value(grade):
        grade_values = {
            "A+": 4.00,
            "A": 3.75,
            "B+": 3.50,
            "B": 3.00,
            "C+": 2.50,
            "C": 2.00,
            "D": 1.00,
            "F": 0.00
        }
        return grade_values[grade]

    @staticmethod
    def value_to_grade(value):
        if 4.00 <= value <= 4.80:
            grade = "A+"
        elif 3.75 <= value < 4.00:
            grade = "A"
        elif 3.50 <= value < 3.75:
            grade = "B+"
        elif 3.00 <= value < 3.50:
            grade = "B"
        elif 2.50 <= value < 3.00:
            grade = "C+"
        elif 2.00 <= value < 2.50:
            grade = "C"
        elif 1.00 <= value < 2.00:
            grade = "D"
        elif 0.00 <= value < 1.00:
            grade = "F"
        else:
            grade = "Invalid value"
        return grade

    def __repr__(self):
        """
        full school , classroom details, student xm mark

        """
        result = ''
        for key in self.classrooms.keys():
            print(key)
        for key, val in self.classrooms.items():
            result += f'============{key.upper()} Classroom Student \n'

            for st in val.students:
                result += f"{st.name}\n"
        print(result)
        subject = ''
        for key in self.classrooms.keys():
            print(key)
        for key, val in self.classrooms.items():
            subject += f'============{key.upper()} Classroom Subjects \n'

            for st in val.subjects:
                subject += f"{st.name}\n"
        print(subject)
        print("===============Student Result============")
        for key,val in self.classrooms.item():
            for s in val.students:
                for a , i in s.mark.items():
                    print(s.name,a,i,s.subject_grade[a])
                print(s.calculate_final_grade())
        return ''
                    