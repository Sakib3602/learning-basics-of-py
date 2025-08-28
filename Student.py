class StudentDataBase:
    student_list = []
    def add_student(self,obj):
        self.student_list.append(obj)
    
stu1 = StudentDataBase()
stu1.add_student({"name" : "sakib", "age" : 23 })
stu1.add_student({"name" : "rahim", "age" : 22 })

for x in stu1.student_list:
    print(x)