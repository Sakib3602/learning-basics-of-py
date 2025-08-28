class Student:
    def __init__(self):
        self.student_list = []
    def add_student(self,obj):
        self.student_list.append(obj)
 
        
don = Student()
don.add_student({"Name" : "Dhoni", "age" : 22})

print(don.student_list)

