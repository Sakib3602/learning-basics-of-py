class Classroom:
    def __init__(self,name):
        self.name = name
        self.students = []
        self.subjects = []
        
    def add_student(self,student):
        roll = f'{self.name} - {len(self.student)+1}'
        student.id = roll
        self.students.append(student)
    def add_subject(self,subject):
        self.subjects.append(subject)
    def take_semester_final(self,student):
        for sunject in self.students:
            sunject.exam(self.student)
        for stu in self.students:
            stu.calculate_final_grade()
            