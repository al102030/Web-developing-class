
from person import Lecturer, Student

def get_lecturer_info():
    lecturer = Lecturer()
    code = input("Enter your code please: ")
    if code != "":
        lecturer.code = code
    name = input("Enter your name please: ")
    if name != "":
        lecturer.name = name
    family = input("Enter your family please: ")
    if family != "":
        lecturer.family = family
        
    lecturer.show_info()
    lecturer.greet()
    return lecturer

def get_student_info():
    std = Student()
    code = input("Enter your code please: ")
    if code != "":
        std.code = code
        name = input("Enter your name please: ")
    if name != "":
        std.name = name
    family = input("Enter your family please: ")
    if family != "":
        std.family = family
        
    std.show_info()
    return std


def creat_json():
    pass

def creat_csv():
    pass


