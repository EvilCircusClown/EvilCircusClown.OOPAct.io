from tkinter import *
from functools import partial
import tkinter.messagebox
class AddStudent:
    def __init__(self, student):
        self.student_data = student
 
    def add_student(self, name, age, idnum, email, phone):
        self.set_name(name)
        self.set_age(age)
        self.set_id(idnum)
        self.set_email(email)
        self.set_phone(phone)
        student_addend = [name, age, idnum, email, phone]
        self.student_data.allstudents.append(student_addend)
        print(f"{student_addend[0]} has been added to the list")
        self.write_to_file(f"{name}, {age}, {idnum}, {email}, {phone}")
        
    def write_to_file(self, data_to_write):
        with open('student_data.txt', 'a+') as file:
            for x in data_to_write:
                file.write(f"{x}")
            file.write("\n")
            file.close()
        print("\nData saved succesfully")
    
    def input_student(self):
        print ('========Student Info========')
        name = input("Enter Name: ")
        age = input("Enter Age: ") 
        idnum = input("Enter ID Number: ") 
        email = input("Enter Email: ") 
        phone = input("Enter Phone Number: ")
        print ('========End of Line========')
        self.add_student(name, age, idnum, email, phone)
        
    def show_reg_ui(self, reg_frame):
        self.lblErrors=Label(reg_frame, text ="", font=("Comic Sans MS", 10, "bold"), bg="#966245", fg="#ff0000")
        self.lblErrors.grid(row=1,column=0,columnspan=4)
        self.reg_txt= ["Name","Age","Student ID","Email Address", "Phone Number"]
        self.reg_entry= []
        for i in range(len(self.reg_txt)):
            Label(reg_frame, text=self.reg_txt[i], font=("Comic Sans MS", 20, "bold"), width=13, anchor="w", bg="#966245").grid(row=i+2, column=0)
            self.reg_entry.append(Entry(reg_frame,width=40,font=("Comic Sans MS", 20, "bold")))
            self.reg_entry[i].grid(row=i+2, column=1, columnspan=3)
        reg_btn=Button(reg_frame, width=30, text="Register", font=("Comic Sans MS", 20, "bold"),bg="#00a5d4", command=self.check_entries)
        reg_btn.grid(columnspan=4)

    def check_entries(self):
        errors=[]
        for i in range(len(self.reg_entry)):
            if self.reg_entry[i].get()=="":
                errors.append(f"You forgot to add the {self.reg_txt[i]}\n")
        if not errors:
                self.add_student(self.reg_entry[0].get(), self.reg_entry[1].get(), self.reg_entry[2].get(), self.reg_entry[3].get(), self.reg_entry[4].get())
                tkinter.messagebox.showinfo("Register success", "Added Student to the list")
        else:
            self.lblErrors.config(text=f"The following error(s) occured:\n{''.join(errors)}\n Please try again.", bg="#ffcc00")        

    def get_name(self):
        return self._name
 
    def set_name(self, value):
        self._name = value
 
    def get_age(self):
        return self._age
 
    def set_age(self, value):
        self._age = value
 
    def get_id(self):
        return self._idnum
 
    def set_id(self, value):
        self._idnum = value
 
    def get_email(self):
        return self._email
 
    def set_email(self, value):
        self._email = value
 
    def get_phone(self):
        return self._phone
 
    def set_phone(self, value):
        self._phone = value
    