from tkinter import *

root = Tk()
root.title("Simple Calculator")
root.geometry("300x150")

frame1 = Frame(root, relief="ridge", bd=2, padx=5, pady=5)
frame1.pack()

frame2 = Frame(root, relief="ridge", bd=2, padx=5, pady=5)
frame2.pack()

frame3 = Frame(root, relief="ridge", bd=2)
frame3.pack()

label_x = Label(frame1, text="Enter the number fox x:", font=("Arial", 12))
label_x.pack(side="left")

entry_x = Entry(frame1, font=("Airal", 12), width=10, justify="center")
entry_x.pack(side="right")

label_y = Label(frame2, text="Enter the number fox y:", font=("Arial", 12))
label_y.pack(side="left")

entry_y = Entry(frame2, font=("Airal", 12), width=10, justify="center")
entry_y.pack(side="right")

btn1 = Button(frame3, text="+", width=4, height=2, command=lambda:calc("+"))
btn1.grid(row=0, column=0)
btn2 = Button(frame3, text="-", width=4, height=2, command=lambda:calc("-"))
btn2.grid(row=0, column=1)
btn3 = Button(frame3, text="/", width=4, height=2, command=lambda:calc("/"))
btn3.grid(row=0, column=2)
btn4 = Button(frame3, text="X", width=4, height=2, command=lambda:calc("x"))
btn4.grid(row=0, column=3)
btn5 = Button(frame3, text="%", width=4, height=2, command=lambda:calc("%"))
btn5.grid(row=0, column=4)
btn6 = Button(frame3, text="x^y", width=4, height=2, command=lambda:calc("x^y"))
btn6.grid(row=0, column=5)

label_result_text = StringVar()
label_result_text.set("Result : ")
label_result = Label(root, textvariable = label_result_text, font=("Airal", 14))
label_result.config(bg="yellow")
label_result.pack()

def calc(op) :
    global label_result_text
    if op == "+" :
        add = float(entry_x.get()) + float(entry_y.get())
        label_result_text.set("Result : " + str(add))
    elif op == "-" :
        sub = float(entry_x.get()) - float(entry_y.get())
        label_result_text.set("Result : " + str(sub))
    elif op == "/" :
        div = float(entry_x.get()) / float(entry_y.get())
        label_result_text.set("Result : " + str(div))
    elif op == "x" :
        mul = float(entry_x.get()) * float(entry_y.get())
        label_result_text.set("Result : " + str(mul))
    elif op == "%" :
        rem = float(entry_x.get()) % float(entry_y.get())
        label_result_text.set("Result : " + str(rem))
    elif op == "x^y" :
        power = float(entry_x.get()) ** float(entry_y.get())
        label_result_text.set("Result : " + str(power))

root.mainloop()