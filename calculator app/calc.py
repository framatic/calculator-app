# It imports tkinter as tk
import tkinter as tk

# 🎨 Subtle Color Palette
COLORS = {
    "bg": "#2E2E2E",             # Charcoal Gray
    "display_bg": "#3C4F76",     # Slate Blue
    "display_fg": "#F5F5F5",     # Ivory White
    "btn_num_bg": "#B0B0B0",     # Misty Gray
    "btn_op_bg": "#C8A2A2",      # Dusty Rose
    "btn_eq_bg": "#A3B18A",      # Sage Green
    "btn_clr_bg": "#D4A373",     # Soft Clay
    "btn_fg": "#2E2E2E",         # Charcoal for text
}

root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.resizable(False , False)
root.configure(bg=COLORS["bg"])  # Apply background color

namee = tk.Label(root, text = "Welcome to calculator app", bg=COLORS["bg"], fg=COLORS["display_fg"])
namee.pack()

# These were first used to enter two number manually old display
"""
outputno1 = tk.Label(root, text = "Enter a number" , font = ("Arial",12))


outputno2 = tk.Label(root, text ="Enter another number", font = ("Arial",12))  


outputno1.pack() 
entry1 = tk.Entry(root, width = "6")
entry1.pack()

outputno2.pack()
entry2 = tk.Entry(root , width = "6")
entry2.pack()
"""

# new display
expression = tk.StringVar()

display = tk.Entry(root, textvariable=expression, font=("Arial", 24), justify="right",
                   bg=COLORS["display_bg"], fg=COLORS["display_fg"], relief="sunken")
display.pack(fill="x", padx=10, pady=10)

"""
# function that handle button press
def press(value):
    current = expression.get()
    expression.set(current + value)
"""

# cursor
new_position = len(expression.get())
display.icursor(new_position)

# These function were used to do arithmatic problems
"""
def addition():  
    number1 = int(entry1.get())   
    number2 = int(entry2.get())
    result1 = number1 + number2
    resultt.config(text = f"result: {result1}") 

def subtraction():
    number1 = int(entry1.get())   
    number2 = int(entry2.get())
    result1 = number1 - number2
    resultt.config(text = f"result: {result1}")

def multiply():
    number1 = int(entry1.get())   
    number2 = int(entry2.get())
    result1 = number1 * number2
    resultt.config(text = f"result: {result1}")

def divide():
    number1 = int(entry1.get())   
    number2 = int(entry2.get())
    result1 = number1 / number2
    resultt.config(text = f"result: {result1}")

def exponent():
    number1 = int(entry1.get())   
    number2 = int(entry2.get())
    result1 = number1 ** number2
    resultt.config(text = f"result: {result1}")
"""

# Creating numberpad and arithmatic symbols pad
"""
"""

def press(value):
    current = expression.get()
    expression.set(current + value)

def clear():
    expression.set("")

def calculate():
    try:
        result = str(eval(expression.get()))
        expression.set(result)
    except:
        expression.set("Error")

def backspace():
    current = expression.get()
    expression.set(current[:-1])

def move_cursor_left():
    pos = display.index(tk.INSERT)
    if pos > 0:
        display.icursor(pos - 1)

def move_cursor_right():
    pos = display.index(tk.INSERT)
    if pos < len(display.get()):
        display.icursor(pos + 1)

pad_frame = tk.Frame(root, bg=COLORS["bg"])
pad_frame.pack()

my_frame = tk.Frame(root, bg=COLORS["bg"])
my_frame.pack()

# Helper to style buttons
def styled_btn(master, text, row, col, cmd, bg_color):
    tk.Button(master, text=text, width=5, height=2, command=cmd,
              bg=bg_color, fg=COLORS["btn_fg"], font=("Arial", 12)).grid(row=row, column=col, padx=2, pady=2)

# Number buttons
styled_btn(my_frame, "7", 0, 0, lambda: press("7"), COLORS["btn_num_bg"])
styled_btn(my_frame, "8", 0, 1, lambda: press("8"), COLORS["btn_num_bg"])
styled_btn(my_frame, "9", 0, 2, lambda: press("9"), COLORS["btn_num_bg"])
styled_btn(my_frame, "⌫", 5, 2, backspace, COLORS["btn_clr_bg"])
styled_btn(my_frame, "+", 0, 3, lambda: press("+"), COLORS["btn_op_bg"])

styled_btn(my_frame, "4", 1, 0, lambda: press("4"), COLORS["btn_num_bg"])
styled_btn(my_frame, "5", 1, 1, lambda: press("5"), COLORS["btn_num_bg"])
styled_btn(my_frame, "6", 1, 2, lambda: press("6"), COLORS["btn_num_bg"])
styled_btn(my_frame, "-", 1, 3, lambda: press("-"), COLORS["btn_op_bg"])

styled_btn(my_frame, "1", 2, 0, lambda: press("1"), COLORS["btn_num_bg"])
styled_btn(my_frame, "2", 2, 1, lambda: press("2"), COLORS["btn_num_bg"])
styled_btn(my_frame, "3", 2, 2, lambda: press("3"), COLORS["btn_num_bg"])
styled_btn(my_frame, "*", 2, 3, lambda: press("*"), COLORS["btn_op_bg"])

styled_btn(my_frame, "0", 3, 0, lambda: press("0"), COLORS["btn_num_bg"])
styled_btn(my_frame, ".", 3, 1, lambda: press("."), COLORS["btn_num_bg"])
styled_btn(my_frame, "C", 3, 2, clear, COLORS["btn_clr_bg"])
styled_btn(my_frame, "÷", 3, 3, lambda: press("/"), COLORS["btn_op_bg"])

styled_btn(my_frame, "(", 4, 0, lambda: press("("), COLORS["btn_op_bg"])
styled_btn(my_frame, ")", 4, 1, lambda: press(")"), COLORS["btn_op_bg"])
styled_btn(my_frame, "^", 4, 2, lambda: press("**"), COLORS["btn_op_bg"])
styled_btn(my_frame, "=", 4, 3, calculate, COLORS["btn_eq_bg"])

styled_btn(my_frame, "←", 5, 0, move_cursor_left, COLORS["btn_clr_bg"])
styled_btn(my_frame, "→", 5, 1, move_cursor_right, COLORS["btn_clr_bg"])

resultt = tk.Label(root, text="", font=("Arial",12), bg=COLORS["bg"], fg=COLORS["display_fg"])
resultt.pack()

root.mainloop()
