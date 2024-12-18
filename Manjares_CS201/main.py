from student import StudentInfo
from search_student import Searching
from print_all_students import PrintAllStudents
from add_student import AddStudent
from main_menu import MainMenu
import os

stu = StudentInfo()
sea, pri, add= Searching(stu), PrintAllStudents(stu), AddStudent(stu)
men = MainMenu(add, sea, pri)

class MainStudent():
    def __init__(self):
        stu.read_file()

        attempts = 0
        while True:
            print("\n========Login - Student InfoSys ========\n")
            login_check = input("Enter student ID: ")
            user = sea.verify_login(stu.allstudents, login_check)
            if user != False:
                men.main_menu(user)
                os.system("cls")
                repeat = input("Are you sure you want to leave? (Y/N): ")
                if repeat.lower() != "y":
                    break
                else:
                    continue
            
            else:
                attempts += 1
                print(f"Invalid Login Credentials. You have {4 - attempts} attempts left")
            if attempts > 3:
                print("You have exceeded the number of possible attempts. Exiting program")
                break
MainStudent()