from tkinter import *
from functools import partial
win = Tk()
res = Label(win, width=20, text="0", font=("Comic Sans MS", 16), fg = "#39403d", bg = "#069e55", anchor = "e")
res.grid(row=0, column = 0, columnspan = 4)
buttons = ["**", "//", "%", "C", "7", "8", "9", "+", "4", "5", "6", "-", "1", "2", "3", "*", ".", "0","=","/"]
row_num, col_num= 0,0
def function(var):
    if str(res.cget("text")) == "Error": res.config(text=f"{var}")
    elif str(res.cget("text")) == "0": res.config(text=f"{var}")
    else: res.config(text=str(res.cget("text"))+f"{var}")
def equal():
    try: res.config(text=str(eval(res.cget("text"))))
    except Exception: res.config(text="Error")
def erase(): res.config(text="0")
for i in range(len(buttons)):
    if buttons[i] == "C": Button(win, width=4, text=buttons[i], font=("Comic Sans MS", 16), command=partial(erase), fg ="#39403d", bg ="#47ad7c").grid(row=row_num+2, column=col_num)
    elif buttons[i] == "=": Button(win, width=4, text=buttons[i], font=("Comic Sans MS", 16), command=partial(equal), fg ="#39403d", bg ="#47ad7c").grid(row=row_num+2, column=col_num)
    else: Button(win, width=4, text=buttons[i], font=("Comic Sans MS", 16), command=partial(function, buttons[i]), fg ="#39403d", bg ="#47ad7c").grid(row=row_num+2, column=col_num)
    col_num+=1
    if col_num==4:
        row_num+=1
        col_num=0
win.config(bg = "#069e55")
win.title("Manjares - Calculator")
win.geometry(f"265x290+{(win.winfo_screenwidth()-265)//2}+{(win.winfo_screenheight()-290)//2}")
win.mainloop()