from tkinter import *
import itertools

# Create the Tkinter window
window = Tk()

# Define the size of the window in width(312) and height(324) using the 'geometry' method
window.geometry("312x324")

# Resizable: in order to prevent the window from getting resized
window.resizable(0, 0)

window.title("Numpad")


def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)


def btn_clear():
    global expression
    expression = ""
    input_text.set("")


expression = ""
# In order to get the instance of the input field 'StringVar()' is used

input_text = StringVar()

letters_by_pad_number = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mnop", "7": "qrs", "8": "tuv",
                         "9": "wxyz"}


# num = int(input("Enter num: "))

def number_to_text(input_text):
    message = ""
    digits = str(input_text.get())
    for digit, group in itertools.groupby(digits):
        letters = letters_by_pad_number[digit]
        presses_number = len(list(group))
        letter_index = (presses_number - 1) % len(letters)
        message += letters[letter_index]
        # print(message)
    input_text.set(message)
    # return message


# Create a frame for the input field
input_frame = Frame(window, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black",
                    highlightthickness=1)
input_frame.pack(side=TOP)

# Create an input field inside the 'Frame'

input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50,
                    bg="#eee", bd=0, justify=RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)
btns_frame = Frame(window, width=312, height=272.5, bg="grey")
btns_frame.pack()

clear = Button(btns_frame, text="C", fg="black", width=32, height=3, bd=0, bg="#eee", cursor="hand2",
               command=lambda: btn_clear()).grid(row=0, column=0, columnspan=3, padx=1, pady=1)

seven = Button(btns_frame, text="7", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
               command=lambda: btn_click(7)).grid(row=3, column=0, padx=1, pady=1)
eight = Button(btns_frame, text="8", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
               command=lambda: btn_click(8)).grid(row=3, column=1, padx=1, pady=1)
nine = Button(btns_frame, text="9", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
              command=lambda: btn_click(9)).grid(row=3, column=2, padx=1, pady=1)

four = Button(btns_frame, text="4", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
              command=lambda: btn_click(4)).grid(row=2, column=0, padx=1, pady=1)
five = Button(btns_frame, text="5", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
              command=lambda: btn_click(5)).grid(row=2, column=1, padx=1, pady=1)
six = Button(btns_frame, text="6", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
             command=lambda: btn_click(6)).grid(row=2, column=2, padx=1, pady=1)

one = Button(btns_frame, text="1", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
             command=lambda: btn_click(1)).grid(row=1, column=0, padx=1, pady=1)
two = Button(btns_frame, text="2", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
             command=lambda: btn_click(2)).grid(row=1, column=1, padx=1, pady=1)
three = Button(btns_frame, text="3", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
               command=lambda: btn_click(3)).grid(row=1, column=2, padx=1, pady=1)

equal = Button(btns_frame, text="=", fg="black", width=32, height=3, bd=0, bg="#fff", cursor="hand2",
               command=lambda: number_to_text(input_text)).grid(row=4, column=0, columnspan=3, padx=1, pady=1)

window.mainloop()
