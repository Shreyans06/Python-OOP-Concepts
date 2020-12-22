class Person:
    def __init__(self, stud_name, stud_age, stud_dept):
        self.name = stud_name
        self.age = stud_age
        self.dept = stud_dept


class Student:
    def __init__(self, sid):
        self.sid = sid


class Faculty:
    def __init__(self, fid):
        self.fid = fid


class StudentMember(Person, Student):
    def __init__(self, stud_name, stud_age, stud_dept, sid):
        Person.__init__(self, stud_name, stud_age, stud_dept)
        Student.__init__(self, sid)

    def display(self):
        print('Student Details')
        print(self.name)
        print(self.age)
        print(self.dept)
        print(self.sid)


class FacultyMember(Person, Faculty):
    def __init__(self, stud_name, stud_age, stud_dept, fid):
        Person.__init__(self, stud_name, stud_age, stud_dept)
        Faculty.__init__(self, fid)

    def display(self):
        print('Faculty Details')
        print(self.name)
        print(self.age)
        print(self.dept)
        print(self.fid)


print('1.Student member\n2.Faculty member\nEnter the choice')
ch = int(input())

print('Enter the Details:')
name = input('Name\n')
age = int(input('Age\n'))
dept = input('Department\n')
stud_id = input('Id\n')

if ch == 1:
    s_account_obj = StudentMember(name, age, dept, stud_id)
    s_account_obj.display()


elif ch == 2:
    f_account_obj = FacultyMember(name, age, dept, stud_id)
    f_account_obj.display()
