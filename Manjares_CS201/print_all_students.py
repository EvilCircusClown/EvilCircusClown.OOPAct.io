from tkinter import *
from functools import partial
import tkinter.messagebox
class PrintAllStudents:
    def __init__(self, student):
        self.student_data = student
 
    def print_all_students(self):
        print ('========Student Info========\n')
        for x in self.student_data.allstudents:
            print (f'Name: {x[0]}\nAge: {x[1]}\nStudent ID: {x[2]}\nEmail: {x[3]}\nPhone Number: {x[4]}\n')
        print ('========End of Line========\n')

    def print_all(self):
        for x in self.student_data.allstudents:
            return f'\nName: {x[0]}\nAge: {x[1]}\nStudent ID: {x[2]}\nEmail: {x[3]}\nPhone Number: {x[4]}\n'

    def print_all_ui(self, reg_frame):
        self.lblAll=Label(reg_frame, text=f"{str(self.print_all())}", font=("Comic Sans MS", 20, "bold"), bg="#ffe3ab")
        self.lblAll.grid(row=1,columnspan=4) 
                