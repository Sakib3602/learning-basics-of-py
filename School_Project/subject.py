from school import School
class Subject:
    def __init__(self,name,teacher):
        self.name = name
        self.teacher = teacher # teacher object 
        self.max_marks = 100
        self.min_marks = 33
    def exam(self,students): # student object ashbe
        for stu in students:
            mark = self.teacher.evaluate_exam()
            stu.marks[self.name] = mark
            stu.subject_grade[self.name] = School.calculate_grade(mark)