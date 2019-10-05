import cmath
import math
import time
import sys
from tkinter import*
import threading
from fractions import*
Input_box_1 = Tk()
userInput = StringVar()
variable_a = StringVar()
variable_b = StringVar()
variable_c = StringVar()
answer_a = variable_a.get()
answer_b = variable_b.get()
answer_c = variable_c.get()
time_selection = StringVar()
mEntry = Entry()


def func1():
    global variable_a
    global variable_b
    global variable_c
 
    t = threading.Thread(target=func4)
    t.start()
    Type_of_answer = time_selection.get()
    a = float(variable_a.get())
    b = float(variable_b.get())
    c = float(variable_c.get())
    b_2 = pow(b,2)
    a_v = str(a)
    b_v = str(b)
    c_v = str(c)
    mlabel1 = Label(Input_box_1,text= "_________________________").place(x=115, y= 30)
    mlabel1 = Label(Input_box_1,text =  b_v + u'\xb1',fg = "red").place(x=125, y= 20)
    
    
    
    # x = math.sqrt(b_2) + (- math.sqrt(4) * math.sqrt(a) * math.sqrt(c))
    x_1 = b_2 + (-4 * a * c)
    x = math.sqrt(x_1)
    z = - b + x
    q = (2 * a)
    v = str(2 * a)
    answer = (z/(2 * a))
    answer_in_fraction = Fraction(int(z) , int(q))
    top_number = answer_in_fraction.numerator
    bottom_number = answer_in_fraction.denominator
    print ("(" + str(bottom_number) + "x - " + str(top_number) + ")")
    
    print ("first root " + str(answer))
    mlabel1 = Label(Input_box_1,text= "(" + v + ")                                      ", fg = "red").place(x=190, y= 50) 
    
    if (Type_of_answer == "Find quadratic answer"):
        mlabel1 = Label(Input_box_1,text='x  = ('   + str(answer_in_fraction) + ")                                     ").place(x = 50, y= 250)
    if(Type_of_answer == "Find Roots"):
        mlabel1 = Label(Input_box_1,text='first root x = ' + str(answer) + "                                  ").place(x = 50, y= 250)
    if (Type_of_answer == "Find Factors"):
        mlabel1 = Label(Input_box_1,text= "(" + str(bottom_number) + "x - " + str(top_number) + ")                                     ").place(x = 50, y= 250)
def func4():
    import math
    
    global variable_a
    global variable_b
    global variable_c
    Type_of_answer = time_selection.get()
    a = float(variable_a.get())
    b = float(variable_b.get())
    c = float(variable_c.get())
    b_2 = pow(b,2)

    

    x_1 = b_2 + (-4 * a * c)
    x = math.sqrt(x_1)
    y = (pow(b,2) - (4 * a * c))
    z = - b - x
    q = (2 * a)
    v = str(2 * a)
    answer_2 = (z/(2 * a))
    answer_in_fraction = Fraction(int(z) , int(q))
    top_number = answer_in_fraction.numerator
    bottom_number = answer_in_fraction.denominator
    print ("(" + str(bottom_number) + "x - " + str(top_number) + ")")
    mlabel1 = Label(Input_box_1,text=  "(" + str(y) + ")               ", fg = "red").place(x=190, y= 20)

    print ("With the radical not present" + str(x))
    print ("Under the radical" + str(y))
    print ("second root" + str(answer_2))
    mlabel1 = Label(Input_box_1,text='With the radical not present ' + str(x) + "                                 ").place(x = 50, y= 180)
    # mlabel1 = Label(Input_box_1,text='Under the radical ' + str(y)).place(x = 50, y= 200)
    if (Type_of_answer == "Find Roots"):
        mlabel1 = Label(Input_box_1,text='second root x = ' + str(answer_2) + "                                     ").place(x = 50, y= 300)
    #mlabel1 = Label(Input_box_1,text='second value x = ' + Fraction(answer_2)).place(x = 50, y= 350)
    if (Type_of_answer == "Find quadratic answer"):
        mlabel1 = Label(Input_box_1,text= " x = (" + str(answer_in_fraction) + ")                                     ").place(x = 50, y= 300)
        
    if (Type_of_answer == "Find Factors"):
        mlabel1 = Label(Input_box_1,text="(" + str(bottom_number) + "x - " + str(top_number) + ")                                             ").place(x = 50, y= 300)

    

    
    
def main():
    global Input_box_1
    
    Input_box_1.resizable(0,0)
    Input_box_1.geometry('400x550+380+150')
    Input_box_1.title('Quadratic Formula')
    
    mlabel1 = Label(Input_box_1,text= "______________ ").place(x=178, y= 2)
    mlabel1 = Label(Input_box_1,text= "__________________").place(x=150, y= 25)
    mlabel1 = Label(Input_box_1,text='b ' + u'\xb1' + "    b"+ u"\u00B2" + " - 4(a)(c)").place(x=150, y= 20)
    mlabel1 = Label(Input_box_1,text= u"\u221A").place(x=175, y= 12)
    mlabel1 = Label(Input_box_1,text= "2(a)").place(x=185, y= 45)
    mlabel1 = Label(Input_box_1,text='input a').place(x=50, y= 80)
    mlabel3 = Label(Input_box_1,text='input b').place(x=180, y= 80)
    mlabel4 = Label(Input_box_1,text='input c').place(x=300, y= 80)
    mEntry = Entry(Input_box_1,text ="clear",textvariable = variable_a).place(x = 0, y=100)
    mEntry = Entry(Input_box_1,text ="clear",textvariable = variable_b).place(x = 130, y=100)
    mEntry = Entry(Input_box_1,text ="clear",textvariable = variable_c).place(x = 260, y=100)
    mbutton = Button(Input_box_1, text ="Ok", command = func1).place(x = 170, y=140)
    mlabel4 = Label(Input_box_1,text='                        ', fg = "white").place(x=400, y= 103)
    time_selection.set("    select the type of answer you are looking for    ") # default value
    w = OptionMenu(Input_box_1, time_selection, "Find Roots", "Find Factors", "Find quadratic answer")
    w.place(x = 5, y=200)

    
    Input_box_1.mainloop()






main()
