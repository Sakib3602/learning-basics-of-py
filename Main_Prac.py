# =========================
# 1. StudentDatabase Class
# =========================
class StudentDatabase:
    student_list = []

    @classmethod
    def add_student(cls, student_obj):
        cls.student_list.append(student_obj)

class Student:
  
    def __init__(self, student_id, name, department, is_enrolled=False):
        self._student_id = student_id
        self._name = name
        self._department = department
        self._is_enrolled = is_enrolled

        StudentDatabase.add_student(self)
    def enroll_student(self):
        if self._is_enrolled:
            print(f"Error: Student {self._name} is already enrolled.")
        else:
            self._is_enrolled = True
            print(f"Student {self._name} has been enrolled.")

    def drop_student(self):
        if not self._is_enrolled:
            print(f"Error: Student {self._name} is not enrolled.")
        else:
            self._is_enrolled = False
            print(f"Student {self._name} has been dropped.")

    # =========================
    def view_student_info(self):
        status = "Enrolled" if self._is_enrolled else "Not Enrolled"
        print(f"ID: {self._student_id}, Name: {self._name}, "
              f"Department: {self._department}, Status: {status}")



def menu():
    while True:
        print("\n=== Student Management System ===")
        print("1. View All Students")
        print("2. Enroll Student")
        print("3. Drop Student")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            print("\nAll Students:")
            for student in StudentDatabase.student_list:
                student.view_student_info()

        elif choice == "2":
            student_id = input("Enter Student ID to enroll: ")
           
            student = next((s for s in StudentDatabase.student_list
                            if str(s._student_id) == student_id), None)
            if student:
                student.enroll_student()
            else:
                print("Error: Invalid student ID.")

        elif choice == "3":
            student_id = input("Enter Student ID to drop: ")
            student = next((s for s in StudentDatabase.student_list
                            if str(s._student_id) == student_id), None)
            if student:
                student.drop_student()
            else:
                print("Error: Invalid student ID.")

        elif choice == "4":
            print("Exiting system...")
            break
        else:
            print("Invalid choice! Please select 1-4.")


# ============================================================================
student1 = Student(101, "Sakib Sarkar", "Computer Science")
student2 = Student(102, "Rahim Uddin", "Mechanical Engineering")
student3 = Student(103, "Kamal Ahmed", "BBA")

menu()
