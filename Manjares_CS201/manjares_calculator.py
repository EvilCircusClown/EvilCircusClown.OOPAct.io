from tkinter import *
win = Tk()
def add():
    lblans.config(text="Sum:"), lblansw.config(text=(int(txt1.get()) + int(txt2.get())))
def subtract():
    lblans.config(text="Difference:"), lblansw.config(text=(int(txt1.get()) - int(txt2.get())))
def multiply():
    lblans.config(text="Product:"), lblansw.config(text=(int(txt1.get()) * int(txt2.get())))
def divide():
    lblans.config(text="Quotient:"), lblansw.config(text=(int(txt1.get()) / int(txt2.get())))
def floordivide():
    lblans.config(text="Quotient:"), lblansw.config(text=(int(txt1.get()) // int(txt2.get())))
def exponent():
    lblans.config(text="Power:"), lblansw.config(text=(int(txt1.get()) ** int(txt2.get())))
def modulus():
    lblans.config(text="Remainder:"), lblansw.config(text=(int(txt1.get()) % int(txt2.get())))
lblfnum, lblsnum= Label(win, text="1st Number:", font=("Comic Sans MS", 16), fg = "#39403d", bg = "#069e55"), Label(win, text="2nd Number:", font=("Comic Sans MS", 16), fg = "#39403d", bg = "#069e55"),
lblfnum.place(x=50, y=100), lblsnum.place(x=50, y=150)
txt1, txt2 = Entry(win, width=20, font=("Comic Sans MS", 16), fg = "#39403d", bg = "#47ad7c"), Entry(win, width=20, font=("Comic Sans MS", 16), fg = "#39403d", bg = "#47ad7c")
txt1.place(x=200, y=100), txt2.place(x=200, y=150)
lblans, lblnam =  Label(win, text="Answer:", font=("Comic Sans MS", 16), fg = "#39403d", bg = "#069e55"), Label(win, text="Calculator", font=("Comic Sans MS", 16), fg = "#39403d", bg = "#47ad7c")
lblans.place(x=70, y=220), lblnam.place(x=200, y=50)
lblansw = Label(win, text="     ", font=("Comic Sans MS", 16), fg = "#39403d", bg = "#47ad7c")
lblansw.place(x=200, y=220)
btnadd, btnsub = Button(win, text=" + ", font=("Comic Sans MS", 16), command=add, fg = "#39403d", bg = "#47ad7c"), Button(win, text=" - ", font=("Comic Sans MS", 16), command=subtract, fg = "#39403d", bg = "#47ad7c")
btnadd.place(x=70, y=300), btnsub.place(x=120, y=300)
btnmul, btndiv = Button(win, text=" * ", font=("Comic Sans MS", 16), command=multiply, fg = "#39403d", bg = "#47ad7c"), Button(win, text=" / ", font=("Comic Sans MS", 16), command=divide, fg = "#39403d", bg = "#47ad7c")
btnmul.place(x=170, y=300), btndiv.place(x=220, y=300)
btnfdi, btnexp = Button(win, text="//", font=("Comic Sans MS", 16), command=floordivide, fg = "#39403d", bg = "#47ad7c"), Button(win, text=" ^ ", font=("Comic Sans MS", 16), command=exponent, fg = "#39403d", bg = "#47ad7c")
btnfdi.place(x=270, y=300), btnexp.place(x=320, y=300)
btnmod = Button(win, text=" % ", font=("Comic Sans MS", 16), command=modulus, fg = "#39403d", bg = "#47ad7c")
btnmod.place(x=370, y=300)
win.config(bg = "#069e55")
win.title("Manjares - Calculator")
win.geometry("500x400+700+300")
win.mainloop()