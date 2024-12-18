from tkinter import *
from functools import partial
import tkinter.messagebox
class Searching:
    def __init__(self, student):
        self.student_data = student
        
    def search_student(self, keyword):
        for student_id in self.student_data.allstudents:
            if student_id[2] == keyword:
                return f'\n========Student Info========\n\nName: {student_id[0]}\nAge: {student_id[1]}\nStudent ID: {student_id[2]}\nEmail: {student_id[3]}\nPhone Number: {student_id[4]} \n========End of Line========\n'
        return f'Student with the ID number {keyword} is not found'
        
    def verify_login(self, list, idnum):
        for x in list:
            if x[2] == idnum:
                return f"{x[0]} {x[2]}"
        return False
    
    def show_search_result_ui(self, reg_frame):
        self.lblSearch=Label(reg_frame, text ="Enter ID Number", font=("Comic Sans MS", 20, "bold"), bg="#966245")
        self.lblSearch.grid(row=1,column=0)
        self.search_entry=Entry(reg_frame, font=("Comic Sans MS", 20, "bold"))
        self.search_entry.grid(row=1,column=1, columnspan=3)
        search_btn=Button(reg_frame, width=30, text="Search", font=("Comic Sans MS", 15, "bold"),bg="#00a5d4", command=self.search_result)
        search_btn.grid(row=2,columnspan=4)
        self.lblSearchResult=Label(reg_frame, text ="", font=("Comic Sans MS", 20, "bold"), bg="#966245")
        self.lblSearchResult.grid(row=3,columnspan=4)
    
    def search_result(self):
        self.lblSearchResult.config(text=self.search_student(self.search_entry.get()), bg="#ffe3ab")

    def show_self_result_ui(self, reg_frame, student_id):
        self.lblSelf=Label(reg_frame, text=f"{self.search_student(student_id)}", font=("Comic Sans MS", 20, "bold"), bg="#ffe3ab")
        self.lblSelf.grid(row=1,columnspan=4) 