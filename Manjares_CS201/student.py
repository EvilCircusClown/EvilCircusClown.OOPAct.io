class StudentInfo:
    def __init__(self):
        self.allstudents = []
    
    def __str__(self):
        return f'Name: {self.allstudents[0]}\nAge: {self.allstudents[1]}\nStudent ID: {self.allstudents[2]}\nEmail: {self.allstudents[3]}\nPhone Number: {self.allstudents[4]}\n'
    
    def read_file(self):
        try:
            with open("student_data.txt", "r") as file:
                line = file.readlines()
                for lines in line[0:]:
                    self.allstudents.append(lines.split(', '))
        except FileNotFoundError:
            print ("\nFile does not exist.")