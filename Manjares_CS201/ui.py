from tkinter import *
from functools import partial
import tkinter.messagebox
from student import StudentInfo
from search_student import Searching
from print_all_students import PrintAllStudents
from add_student import AddStudent
from main_menu import MainMenu

stu = StudentInfo()
sea, pri, add= Searching(stu), PrintAllStudents(stu), AddStudent(stu)
men = MainMenu(add, sea, pri)
win=Tk()
btns, container, btn_txt=[], [], ["User Information", "Student Information","Register Student", "All students","Logout"]
def login():
    stu.read_file()
    global attempts
    login_check = login_txt.get()
    user = sea.verify_login(stu.allstudents, login_check)
    if login_check == "":
        wrong_user.config(text="No login credentials entered.")
    elif user != False:
            login_div.pack_forget(),main_div.pack(fill="both", expand=True)
            sea.show_self_result_ui(container[0], login_check)
    else:
        attempts+= 1
        if attempts > 3:
            wrong_user.config(text="You have exceeded the number of possible attempts. Exiting program")
            user.append(login_check)
            win.after(2000, win.destroy)
        else:
            wrong_user.config(text=f"Invalid Login Credentials. You have {4 - attempts} attempts left")
def exit():
    win.destroy()
def logout():
    main_div.pack_forget(),login_div.pack(fill="both", expand=True)
def open_div(div_open, close):
    for i in range(len(close)):
        if close[i].winfo_ismapped():
            close[i].pack_forget()
    div_open.pack(side="left", fill="x")
login_div=Frame(win, bg="#966245")
login_div.pack(fill="both", expand=True)
login_ui=Frame(login_div, bg="#f0ce9c", height=240, width=400)
login_ui.place(anchor="center", relx=.5, rely=.5)
wrong_user= Label(login_ui, width=50, text="",font=("Comic Sans MS", 10), pady=10, bg="#f0ce9c", fg="#ff0000")
wrong_user.grid(row=0,column=0)
attempts=0
Label(login_ui, width=20, text="Student Login System",font=("Comic Sans MS", 20), pady=10, bg="#f0ce9c").grid(row=1,column=0)
login_txt = Entry(login_ui, border=0, bg="#ffffff", width=20, font=("Comic Sans MS", 20))
login_txt.grid(row=2,column=0, padx=8, pady=8)
Button(login_ui, anchor="center", text="Login", border=0, bg="#2cc932", width=10, font=("Comic Sans MS", 20),padx=2, pady=2, command=login).grid(row=3,column=0, pady=8)
Button(login_ui, anchor="center", text="Exit", border=0, bg="#2cc932", width=10, font=("Comic Sans MS", 20),padx=2, pady=2, command=exit).grid(row=4,column=0, pady=8)
main_div=Frame(win, bg="#d8eaeb")
menu_div=Frame(main_div, bg="#00a5d4")
menu_div.pack(side="left", fill="y")
cont_div=Frame(main_div, bg="#d8eaeb")
cont_div.pack(side="left", fill="y")
Label(menu_div, width=20, text="Main Menu", font=("Comic Sans MS", 20), pady=3, bg="#966245").grid(row=0,column=0)
for i in range(len(btn_txt)-1):
    container.append(Frame(cont_div, bg="#966245", pady=8))
    Label(container[i], text=btn_txt[i], font=("Comic Sans MS", 20, "bold"), bg="#966245", width=45, anchor="center").grid(row=0,column=0,columnspan=5)
func=[partial(open_div, container[0],[container[1], container[2], container[3]]),
      partial(open_div, container[1],[container[0], container[2], container[3]]),
      partial(open_div, container[2],[container[1], container[0], container[3]]),
      partial(open_div, container[3],[container[1], container[2], container[0]]),
      logout]
for i in range(len(btn_txt)):
    btns.append(Button(menu_div, width=20, text=(f"{btn_txt[i]}"), font=("Comic Sans MS", 20), pady=3, bg="#00a5d4"))
    btns[i].grid(row=i+1,column=0)
    btns[i].config(command=(func[i]))
sea.show_search_result_ui(container[1])
add.show_reg_ui(container[2])
pri.print_all_ui(container[3])
win.config(bg="#d8eaeb")
win.title("Manjares-Ui")
win.geometry(f"1000x600+{(win.winfo_screenwidth()-1000)//2}+{(win.winfo_screenheight()-600)//2}")
win.mainloop()