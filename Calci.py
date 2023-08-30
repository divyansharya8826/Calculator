from tkinter import * #type:ignore
from math import *  # type:ignore

def get_input(btn):
    index = txt.index(INSERT)
    if btn == 1:
        txt.delete(0,END)
    elif btn == 2:
        if txt.icursor(index) == "-":
            txt.delete(index-1,index)
        else:
            txt.insert(index-1,"")

    elif btn == 3:
        txt.insert(index,"%")
    elif btn == 4:
        txt.insert(index,"/")
    elif btn == 5:
        txt.insert(index,"7")
    elif btn == 6:
        txt.insert(index,"8")
    elif btn == 7:
        txt.insert(index,"9")
    elif btn == 8:
        txt.insert(index,"*")
    elif btn == 9:
        txt.insert(index,"4")
    elif btn == 10:
        txt.insert(index,"5")
    elif btn == 11:
        txt.insert(index,"6")
    elif btn == 12:
        txt.insert(index,"-")
    elif btn == 13:
        txt.insert(index,"1")
    elif btn == 14:
        txt.insert(index,"2")
    elif btn == 15:
        txt.insert(index,"3")
    elif btn == 16:
        txt.insert(index,"+")
    elif btn == 17:
        txt.insert(index,"0")
    elif btn == 18:
        txt.insert(index,".")
    elif btn == 19:
        res = txt.get()
        txt.delete(0,END)
        txt.insert(index,str(eval(res)))


root = Tk()
root.resizable(True, True)
root.title("Calculator")

frame = Frame(root, bg="grey")
frame.pack(anchor="center")

input = StringVar()
txt = Entry(frame, textvariable=input, width=34,
            font=("arial", 15), justify="right")
txt.grid(row=0, column=1, columnspan=4)

btn1 = Button(frame, text="AC", width="5", height="2", font=(
    "arial", 15, "bold"), command=lambda: [get_input(1)])
btn1.grid(row=1, column=1)
btn2 = Button(frame, text="+/-", width="5", height="2", font=("arial",
              15, "bold"), command=lambda: [get_input(2)])
btn2.grid(row=1, column=2)
btn3 = Button(frame, text="%", width="5", height="2", font=(
    "arial", 15, "bold"), command=lambda: [get_input(3)])
btn3.grid(row=1, column=3)
btn4 = Button(frame, text="÷", width="5", height="2", font=(
    "arial", 15, "bold"), command=lambda: [get_input(4)])
btn4.grid(row=1, column=4)

btn5 = Button(frame, text="7", width="5",
              height="2", font=("arial", 15, "bold"), command=lambda: [get_input(5)])
btn5.grid(row=2, column=1)
btn6 = Button(frame, text="8", width="5",
              height="2", font=("arial", 15, "bold"), command=lambda: [get_input(6)])
btn6.grid(row=2, column=2)
btn7 = Button(frame, text="9", width="5",
              height="2", font=("arial", 15, "bold"), command=lambda: [get_input(7)])
btn7.grid(row=2, column=3)
btn8 = Button(frame, text="x", width="5",
              height="2", font=("arial", 15, "bold"), command=lambda: [get_input(8)])
btn8.grid(row=2, column=4)

btn9 = Button(frame, text="4", width="5",
              height="2", font=("arial", 15, "bold"), command=lambda: [get_input(9)])
btn9.grid(row=3, column=1)
btn10 = Button(frame, text="5", width="5",
               height="2", font=("arial", 15, "bold"), command=lambda: [get_input(10)])
btn10.grid(row=3, column=2)
btn11 = Button(frame, text="6", width="5",
               height="2", font=("arial", 15, "bold"), command=lambda: [get_input(11)])
btn11.grid(row=3, column=3)
btn12 = Button(frame, text="-", width="5",
               height="2", font=("arial", 15, "bold"), command=lambda: [get_input(12)])
btn12.grid(row=3, column=4)

btn13 = Button(frame, text="1", width="5",
               height="2", font=("arial", 15, "bold"), command=lambda: [get_input(13)])
btn13.grid(row=4, column=1)
btn14 = Button(frame, text="2", width="5",
               height="2", font=("arial", 15, "bold"), command=lambda: [get_input(14)])
btn14.grid(row=4, column=2)
btn15 = Button(frame, text="3", width="5",
               height="2", font=("arial", 15, "bold"), command=lambda: [get_input(15)])
btn15.grid(row=4, column=3)
btn16 = Button(frame, text="+", width="5",
               height="2", font=("arial", 15, "bold"), command=lambda: [get_input(16)])
btn16.grid(row=4, column=4)

btn17 = Button(frame, text="0", width="14",
               height="2", font=("arial", 15, "bold"), command=lambda: [get_input(17)])
btn17.grid(row=5, columnspan=2, column=1)
btn18 = Button(frame, text=".", width="5",
               height="2", font=("arial", 15, "bold"), command=lambda: [get_input(18)])
btn18.grid(row=5, column=3)
btn19 = Button(frame, text="=", width="5",
               height="2", font=("arial", 15, "bold"), command=lambda: [get_input(19)])
btn19.grid(row=5, column=4)
root.mainloop()