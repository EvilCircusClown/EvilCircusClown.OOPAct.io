import os

class MainMenu:
    def __init__(self, student):
        self.student_data = student
        
    def __init__(self, add_student, search_student, print_all_students):
        self.add = add_student
        self.sea = search_student
        self.pri = print_all_students
        
    def add_student_option(self):
        while True:
            os.system("cls")
            self.add.input_student()
            repeat = input("Do you want to add for another student? (Y/N):")
            if repeat.lower() != "y":
                break
        
    def search_student_option(self):
        while True:
            os.system("cls")
            keyword =  input("\nEnter ID Number: ")
            print(self.sea.search_student(keyword))
            repeat = input("Do you want to search again? (Y/N):")
            if repeat.lower() != "y":
                break
            
    def print_all_students_option(self):
        os.system("cls")
        self.pri.print_all_students()
        input("Press Enter to Continue")
        
    def main_menu(self, user):
        username, user_id = user.split()
        while True:
            print("\n========Welcome to the Student Information System========")
            print("Here are your choices\n1.View your information\n2.View other student's information\n3.Register a new student\n4.Print all students\n5.Exit")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                os.system("cls")
                print("========Search Student Information========")
                print(self.sea.search_student(user_id))
            elif choice == 2:
                self.search_student_option()
            elif choice == 3:
                self.add_student_option()
            elif choice == 4:
                self.print_all_students_option()
            elif choice == 5:
                break
            
            