class Student:
    def __init__(self,id,name,deparment,is_enrolled):
        self.id = id
        self.name  = name
        self.department = deparment
        self.is_enrolled = is_enrolled
    def __repr__(self):
        return f'{self.id} : {self.name} : {self.department} : {self.is_enrolled}'
kabir = Student(23453,"kabir Sigh", "BBA",True)

print(kabir)
        