from tkinter import *



"""
Setting up the environment
"""

#Calc_Prac = Tk()
root = Tk()

#setting the width x height
root.geometry("312x324")

#stop root from being resized
root.resizable(0,0)

#titling the window of the calc
root.title("Calculator!!!!!!!!")



"""
Defining the functions to make the calculator work
"""

def press_button(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

def press_clear():
    global expression
    expression = ""
    input_text.set("")

def press_equal():
    global expression
    result = str(eval(expression))
    input_text.set(result)
    expression = ""


expression = ""
input_text = StringVar()

"""
Setting up the actual application's look
"""
#frame properties
window = Frame(root, width = 312, height = 50, bd = 0, highlightbackground="black",
               highlightcolor="black", highlightthickness=1)
window.pack(side = TOP)

#setting up the input box dimensions and properties
input_box = Entry(window, font = ('arial', 18, 'bold'), textvariable=input_text,
                  width = 50, bg = "#eee", bd = 0, justify = RIGHT)
input_box.grid(row = 0, column = 0)
input_box.pack(ipady = 10) #ipady increases the height of the input box, internal padding

#frame where the buttons will be placed within
button_frame = Frame(root, width = 312, height = 272.5 , bg = "gray")
button_frame.pack()

#buttons non number
clear = Button(button_frame, text = "Clear", fg = "black", width = 32, height = 3, bd = 0, bg = "#eee",
               cursor = "hand2", command = lambda: press_clear()).grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)
divide = Button(button_frame, text = "/", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee",
                cursor = "hand2", command = lambda: press_button("/")).grid(row = 0, column = 3, padx = 1, pady = 1)
multiply = Button(button_frame, text = "*", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee",
                  cursor = "hand2", command = lambda: press_button("*")).grid(row = 1, column = 3, padx = 1, pady = 1)
minus = Button(button_frame, text = "-", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee",
               cursor = "hand2", command = lambda: press_button("-")).grid(row = 2, column = 3, padx = 1, pady = 1)
plus = Button(button_frame, text = "+", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee",
              cursor = "hand2", command = lambda: press_button("+")).grid(row = 3, column = 3, padx = 1, pady = 1)
point = Button(button_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee",
               cursor = "hand2", command = lambda: press_button(".")).grid(row = 4, column = 2, padx = 1, pady = 1)
equals = Button(button_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee",
                cursor = "hand2", command = lambda: press_equal()).grid(row = 4, column = 3, padx = 1, pady = 1)

#number buttons
seven = Button(button_frame, text = "7", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff",
               cursor = "hand2", command = lambda: press_button(7)).grid(row = 1, column = 0, padx = 1, pady = 1)
eight = Button(button_frame, text = "8", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff",
               cursor = "hand2", command = lambda: press_button(8)).grid(row = 1, column = 1, padx = 1, pady = 1)
nine = Button(button_frame, text = "9", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff",
              cursor = "hand2", command = lambda: press_button(9)).grid(row = 1, column = 2, padx = 1, pady = 1)
four = Button(button_frame, text = "4", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff",
              cursor = "hand2", command = lambda: press_button(4)).grid(row = 2, column = 0, padx = 1, pady = 1)
five = Button(button_frame, text = "5", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff",
              cursor = "hand2", command = lambda: press_button(5)).grid(row = 2, column = 1, padx = 1, pady = 1)
six = Button(button_frame, text = "6", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff",
             cursor = "hand2", command = lambda: press_button(6)).grid(row = 2, column = 2, padx = 1, pady = 1)
one = Button(button_frame, text = "1", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff",
             cursor = "hand2", command = lambda: press_button(1)).grid(row = 3, column = 0, padx = 1, pady = 1)
two = Button(button_frame, text = "2", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff",
             cursor = "hand2", command = lambda: press_button(2)).grid(row = 3, column = 1, padx = 1, pady = 1)
three = Button(button_frame, text = "3", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff",
               cursor = "hand2", command = lambda: press_button(3)).grid(row = 3, column = 2, padx = 1, pady = 1)

zero = Button(button_frame, text = "0", fg = "black", width = 21, height = 3, bd = 0, bg = "#fff",
              cursor = "hand2", command = lambda: press_button(0)).grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)

window.mainloop()