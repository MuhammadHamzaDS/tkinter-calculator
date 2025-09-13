import tkinter as tk

# Function for button click
def click(event):
    global expression
    expression += str(event.widget.cget("text"))
    text_var.set(expression)

def clear():
    global expression
    expression = ""
    text_var.set(expression)

def evaluate():
    global expression
    try:
        result = str(eval(expression))
        text_var.set(result)
        expression = ""
    except:
        text_var.set("Error")
        expression = ""

# Main window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

expression = ""
text_var = tk.StringVar()

# Entry widget
entry = tk.Entry(root, textvar=text_var, font="Arial 20", bd=5, relief="ridge")
entry.pack(fill="both", ipadx=8, pady=10, padx=10)

# Buttons
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]

for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")
    for btn in row:
        b = tk.Button(frame, text=btn, font="Arial 18", relief="ridge", bd=3)
        b.pack(side="left", expand=True, fill="both")
        if btn == "=":
            b.bind("<Button-1>", lambda e: evaluate())
        else:
            b.bind("<Button-1>", click)

# Clear button
clear_btn = tk.Button(root, text="C", font="Arial 18", bd=3, relief="ridge", bg="red", fg="white", command=clear)
clear_btn.pack(fill="both", padx=10, pady=5)

root.mainloop()
