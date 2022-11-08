import tkinter as tk
calculation=""

def operation_calculation(symbol):
    global calculation
    calculation += str(symbol)
    textbox.delete(1.0,"end")
    textbox.insert(1.0, calculation)

def total_result():
    global calculation
    try:
      calculation = str(eval(calculation))
      textbox.delete(1.0,"end")
      textbox.insert(1.0,calculation)
    except:
        clear_field()
        textbox.insert(1.0,"Error")


def clear_field():
    global calculation
    calculation=""
    textbox.delete(1.0,"end")
    

window = tk.Tk()
window.geometry('400x400')
window.title("Calculator")

label= tk.Label(window, text="Lets make life Easier", font=('Arial', 14))
label.pack(padx=20, pady=20)

textbox=tk.Text(window, height=5, font=('Arial', 14))
textbox.pack(padx=5)

buttonframe= tk.Frame(window)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

btn1= tk.Button(buttonframe, text="9", command=lambda:operation_calculation(9), width=5,font=('Arial, 18'))
btn1.grid(row=0,column=0, sticky=tk.W+tk.E)  
btn2= tk.Button(buttonframe, text="8",command=lambda:operation_calculation(8),width=5, font=('Arial, 18'))
btn2.grid(row=0,column=1, sticky=tk.W+tk.E)  
btn3= tk.Button(buttonframe, text="7",command=lambda:operation_calculation(7),width=5, font=('Arial, 18'))
btn3.grid(row=0,column=2, sticky=tk.W+tk.E)  
btn4= tk.Button(buttonframe, text="6",command=lambda:operation_calculation(6),width=5, font=('Arial, 18'))
btn4.grid(row=1,column=0, sticky=tk.W+tk.E)  
btn5= tk.Button(buttonframe, text="5",command=lambda:operation_calculation(5),width=5, font=('Arial, 18'))
btn5.grid(row=1,column=1, sticky=tk.W+tk.E)
btn6= tk.Button(buttonframe, text="4",command=lambda:operation_calculation(4),width=5, font=('Arial, 18'))
btn6.grid(row=1,column=2, sticky=tk.W+tk.E)  
btn7= tk.Button(buttonframe, text="3",command=lambda:operation_calculation(3),width=5, font=('Arial, 18'))
btn7.grid(row=2,column=0, sticky=tk.W+tk.E)
btn8= tk.Button(buttonframe, text="2",command=lambda:operation_calculation(2),width=5, font=('Arial, 18'))
btn8.grid(row=2,column=1, sticky=tk.W+tk.E)  
btn9= tk.Button(buttonframe, text="1",command=lambda:operation_calculation(1),width=5, font=('Arial, 18'))
btn9.grid(row=2,column=2, sticky=tk.W+tk.E)
btn10= tk.Button(buttonframe, text="+",command=lambda:operation_calculation('+'),width=5, font=('Arial, 18'))
btn10.grid(row=2,column=3, sticky=tk.W+tk.E)
btn11= tk.Button(buttonframe, text="-",command=lambda:operation_calculation('-'),width=5, font=('Arial, 18'))
btn11.grid(row=1,column=3, sticky=tk.W+tk.E)
btn12= tk.Button(buttonframe, text="*",command=lambda:operation_calculation('*'),width=5, font=('Arial, 18'))
btn12.grid(row=0,column=3, sticky=tk.W+tk.E)
btn13= tk.Button(buttonframe, text="/",command=lambda:operation_calculation('/'),width=5, font=('Arial, 18'))
btn13.grid(row=2,column=4, sticky=tk.W+tk.E)
btn14= tk.Button(buttonframe, text="=",command=total_result,width=5, font=('Arial, 18'))
btn14.grid(row=1,column=4, sticky=tk.W+tk.E)
btn15= tk.Button(buttonframe, text="c",command=clear_field,width=5, font=('Arial, 18'))
btn15.grid(row=0,column=4, sticky=tk.W+tk.E)
btn16= tk.Button(buttonframe, text="0",command=lambda:operation_calculation(0),width=5, font=('Arial, 18'))
btn16.grid(row=1,column=5, sticky=tk.W+tk.E)

buttonframe.pack(fill='x')
 









window.mainloop()
