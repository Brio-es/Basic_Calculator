import tkinter as tk
import tkinter.font as font
import math



def change_number(x):
    new_number.set(x)
    complete_number.set(complete_number.get() + new_number.get())


def operationional(x):
    if second_time.get() == False:
        old_number.set(complete_number.get())
        complete_number.set("")
    state.set(x)

def result():
    if state.get() == "addition":
            a = float(complete_number.get())
            b = float(old_number.get())
            answer = a + b
    elif state.get() == "substraction":
            b = float(complete_number.get())
            a = float(old_number.get())
            answer = a - b
    elif state.get() == "multiplication":
            a = float(complete_number.get())
            b = float(old_number.get())
            answer = a * b
    elif state.get() == "division":
            b = float(complete_number.get())
            a = float(old_number.get())
            if b == 0:
                answer = "ERROR"
            else:
                answer = a / b
    elif state.get() == "power":
            b = float(complete_number.get())
            a = float(old_number.get())

            answer = a ** b
    elif state.get() == "root":
            b = float(complete_number.get())
            a = float(old_number.get())

            answer = a ** (1/b)


    ans.set(round(answer,4))
    new_number.set("")
    complete_number.set("")
    old_number.set(ans.get())
    state.set("")
    second_time.set(True)

def AC():
    new_number.set("")
    operation.set("")
    complete_number.set("")
    old_number.set("")
    ans.set("")
    state.set("")
    second_time.set(False)



root = tk.Tk()

#varibles
new_number =tk.StringVar()
new_number.set("")

operation = tk.StringVar()
operation.set("")

complete_number =tk.StringVar()
complete_number.set("")

complete_number_op=tk.IntVar()
complete_number_op.set(complete_number)

old_number = tk.StringVar()
old_number.set("")

ans = tk.StringVar()
ans.set("")

state = tk.StringVar()
state.set("")

second_time = tk.BooleanVar()
state.set(False)




canvas1 = tk.Canvas(root, width=210, height=255)
canvas1.pack()
root.title("Calculator")

#first text font
font1 = font.Font(family='Helvetica', size=15,)


#first text
label1 = tk.Label(root,
                  textvariable=complete_number,
                  anchor="w",
                  justify=tk.RIGHT,
                  bd=1)
label1['font'] = font1



canvas1.create_window(65, 40, window=label1)

#uppernumber text
label3 = tk.Label(root, textvariable=old_number)
canvas1.create_window(160, 20, window=label3)

#ans text
label2 = tk.Label(root, textvariable=ans)
canvas1.create_window(160,65, window=label2)
label2['font'] = font1

#buttons from 0-9
button_0 = tk.Button(text='0', command=lambda:change_number("0"))
button_1 = tk.Button(text='1', command=lambda:change_number("1"))
button_2 = tk.Button(text='2', command=lambda:change_number("2"))
button_3 = tk.Button(text='3', command=lambda:change_number("3"))
button_4 = tk.Button(text='4', command=lambda:change_number("4"))
button_5 = tk.Button(text='5', command=lambda:change_number("5"))
button_6 = tk.Button(text='6', command=lambda:change_number("6"))
button_7 = tk.Button(text='7', command=lambda:change_number("7"))
button_8 = tk.Button(text='8', command=lambda:change_number("8"))
button_9 = tk.Button(text='9', command=lambda:change_number("9"))

#syntax buttons
button_AC = tk.Button(text="AC",command=AC)
button_dot = tk.Button(text=".",command=lambda:change_number(".") )
button_solve = tk.Button(text="=", command=result)

#operations buttons
button_substraction = tk.Button(text=u"\u2212",  command=lambda:operationional("substraction") )
button_addition = tk.Button(text=u"\u002B", command=lambda:operationional("addition"))
button_multiplication = tk.Button(text=u"\u00D7", command=lambda:operationional("multiplication") )
button_division = tk.Button(text=u"\u00F7", command=lambda:operationional("division") )
button_squared = tk.Button(text=u"x\u207F",command=lambda:operationional("power") )
button_squared_root = tk.Button(text=u"\u207F\u221A", command=lambda:operationional("root"))


#window for buttons from 0-9
canvas1.create_window(80,232.5, window=button_0, width=40, height=25)
canvas1.create_window(30,197.5, window=button_1, width=40, height=25)
canvas1.create_window(80,197.5, window=button_2, width=40, height=25)
canvas1.create_window(130,197.5, window=button_3, width=40, height=25)
canvas1.create_window(30,162.5, window=button_4, width=40, height=25)
canvas1.create_window(80,162.5, window=button_5, width=40, height=25)
canvas1.create_window(130,162.5, window=button_6, width=40, height=25)
canvas1.create_window(30,127.5, window=button_7, width=40, height=25)
canvas1.create_window(80,127.5, window=button_8, width=40, height=25)
canvas1.create_window(130,127.5, window=button_9, width=40, height=25)

#window for syntax buttons
canvas1.create_window(30,232.5, window=button_AC, width=40, height=25)
canvas1.create_window(130,232.5, window=button_dot, width=40, height=25)
canvas1.create_window(180,232.5, window=button_solve, width=40, height=25)

#window for operations buttons
canvas1.create_window(180,162.5, window=button_substraction, width=40, height=25)
canvas1.create_window(180,197.5, window=button_addition, width=40, height=25)
canvas1.create_window(130,92.5, window=button_multiplication, width=40, height=25)
canvas1.create_window(180,127.5, window=button_division, width=40, height=25)
canvas1.create_window(30,92.5, window=button_squared, width=40, height=25)
canvas1.create_window(80,92.5, window=button_squared_root, width=40, height=25)


root.resizable(0,0)
root.resizable(False, False)
root.attributes('-toolwindow', True)

root.mainloop()


