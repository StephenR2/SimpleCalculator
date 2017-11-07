# Stephen Randall
# 11/06/17
# Folder: Unit8Project File: unit8proj.py
# This program is a simple calculator, deals with the functions: add, subtraction, multiplication, division, square root
import tkinter
import math


root = tkinter.Tk()
root.title("Calculator")

answer = tkinter.StringVar()


def press_one():
    """
    Gets the current numbers in the entry field and adds the number one to it when pressed.

    """
    tempnum = answer.get()
    tempnum = tempnum + "1"
    answer.set(tempnum)


def press_two():
    """
    Gets the current numbers in the entry field and adds the number two to it when pressed.

    """
    tempnum = answer.get()
    tempnum = tempnum + "2"
    answer.set(tempnum)


def press_three():
    """
    Gets the current numbers in the entry field and adds the number three to it when pressed.

    """
    tempnum = answer.get()
    tempnum = tempnum + "3"
    answer.set(tempnum)


def press_four():
    """
    Gets the current numbers in the entry field and adds the number four to it when pressed.

    """
    tempnum = answer.get()
    tempnum = tempnum + "4"
    answer.set(tempnum)


def press_five():
    """
    Gets the current numbers in the entry field and adds the number five to it when pressed.

    """
    tempnum = answer.get()
    tempnum = tempnum + "5"
    answer.set(tempnum)


def press_six():
    """
    Gets the current numbers in the entry field and adds the number six to it when pressed.

    """
    tempnum = answer.get()
    tempnum = tempnum + "6"
    answer.set(tempnum)


def press_seven():
    """
    Gets the current numbers in the entry field and adds the number seven to it when pressed.

    """
    tempnum = answer.get()
    tempnum = tempnum + "7"
    answer.set(tempnum)


def press_eight():
    """
    Gets the current numbers in the entry field and adds the number eight to it when pressed.

    """
    tempnum = answer.get()
    tempnum = tempnum + "8"
    answer.set(tempnum)


def press_nine():
    """
    Gets the current numbers in the entry field and adds the number nine to it when pressed.

    """
    tempnum = answer.get()
    tempnum = tempnum + "9"
    answer.set(tempnum)


def press_clear():
    """
    Sets the entry field to an empty string, thus clearing it.

    """
    answer.set("")


def press_multi():
    """
    Gets the current numbers in the entry field and adds a multiplication symbol to it when pressed.

    """
    tempnum = answer.get()
    tempnum = tempnum + "*"
    answer.set(tempnum)


def press_div():
    """
    Gets the current numbers in the entry field and adds a division symbol to it when pressed.

    """
    tempnum = answer.get()
    tempnum = tempnum + "/"
    answer.set(tempnum)


def press_sub():
    """
    Gets the current numbers in the entry field and adds a subtraction symbol to it when pressed.

    """
    tempnum = answer.get()
    tempnum = tempnum + "-"
    answer.set(tempnum)


def press_deci():
    """
    Gets the current numbers in the entry field and adds a decimal to it when pressed.

    """
    tempnum = answer.get()
    tempnum = tempnum + "."
    answer.set(tempnum)


def press_add():
    """
    Gets the current numbers in the entry field and adds an addition symbol to it when pressed.

    """
    tempnum = answer.get()
    tempnum = tempnum + "+"
    answer.set(tempnum)


def press_sqrt():
    """
    Gets the current numbers in the entry field and converts it to a float, sets equal to a variable and takes the
    square root of said variable. Sets the answer.
    """
    tempnum = answer.get()
    sqrtanswer = float(tempnum)
    finalsqrt = math.sqrt(sqrtanswer)
    answer.set(finalsqrt)


def press_equal():
    """
    Gets the numbers in the entryfield, evaluates the string using the command eval(), sets equal to a variable. Sets
    the answer.
    """
    tempnum = answer.get()
    finalanswer = eval(tempnum)
    answer.set(finalanswer)

entryField = tkinter.Entry(root, textvariable=answer)
entryField.grid(column=1, row=2, columnspan=5)

myButton1 = tkinter.Button(root, text="1", command=press_one)
myButton1.grid(column=1, row=3)

myButton2 = tkinter.Button(root, text="2", command=press_two)
myButton2.grid(column=2, row=3)

myButton3 = tkinter.Button(root, text="3", command=press_three)
myButton3.grid(column=3, row=3)

myButtonMulti = tkinter.Button(root, text="*", command=press_multi)
myButtonMulti.grid(column=4, row=3)

myButtonDiv = tkinter.Button(root, text="/", command=press_div)
myButtonDiv.grid(column=5, row=3)

myButton4 = tkinter.Button(root, text="4", command=press_four)
myButton4.grid(column=1, row=4)

myButton5 = tkinter.Button(root, text="5", command=press_five)
myButton5.grid(column=2, row=4)

myButton6 = tkinter.Button(root, text="6", command=press_six)
myButton6.grid(column=3, row=4)

myButtonSub = tkinter.Button(root, text="-", command=press_sub)
myButtonSub.grid(column=4, row=4)

myButtonDeci = tkinter.Button(root, text=".", command=press_deci)
myButtonDeci.grid(column=5, row=4)

myButton7 = tkinter.Button(root, text="7", command=press_seven)
myButton7.grid(column=1, row=5)

myButton8 = tkinter.Button(root, text="8", command=press_eight)
myButton8.grid(column=2, row=5)

myButton9 = tkinter.Button(root, text="9", command=press_nine)
myButton9.grid(column=3, row=5)

myButtonAdd = tkinter.Button(root, text="+", command=press_add)
myButtonAdd.grid(column=4, row=5)

myButtonRoot = tkinter.Button(root, text="√", command=press_sqrt)
myButtonRoot.grid(column=5, row=5)

myButtonEqual = tkinter.Button(root, text="=", command=press_equal)
myButtonEqual.grid(column=1, row=6, columnspan=3, sticky="E, W")
root.bind("<Return>", lambda e: press_equal())
root.bind("<=>", lambda e: press_equal())

myButtonClear = tkinter.Button(root, text="Clear", command=press_clear)
myButtonClear.grid(column=4, row=6, columnspan=2, sticky="E, W")


root.mainloop()
