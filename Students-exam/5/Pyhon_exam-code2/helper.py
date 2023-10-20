from person import Lecturer, Student
import json
import csv
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


def creat_json(participants):
    for participant in participants:
        participants.append({'Code' :participant.code, 'Name' : participant.name, 'Family': participant.family})
    with open('participants.json' , 'w') as jsonfile:
        json.dump(participants, jsonfile, indent = 4)

def creat_csv(participants):
    with open('participates.csv' , 'w') as csvfile:
        writer = csv.DictWriter(csvfile,fieldnames=participants)
        for participant in participants:
            writer.writerow({'Code' :participant.code, 'Name' : participant.name, 'Family': participant.family})
