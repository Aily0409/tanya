import tkinter


def display_grade():
    user_input= entry.get().upper()
    
    if user_input == "O":
        label2.config(text="Girl, chill..")
    elif user_input == "A":
        label2.config(text="Nice")
    elif user_input == "B":
        label2.config(text="Okay level")
    elif user_input == "C":
        label2.config(text="Meh..")
    elif user_input == "F":
        label2.config(text="You should study more..")
    else:
        label2.config(text="Huh")



root = tkinter.Tk()
root.geometry("400x400")
root.title("Grades Display GUI")

label1 = tkinter.Label(root, text="Enter Grade (O, A, B, C, OR F)")
label1.pack(pady=15)

entry = tkinter.Entry(root, width=10)
entry.pack()

button = tkinter.Button(root, text="Submit", command=display_grade)
button.pack(pady=15)

label2= tkinter.Label(root, text=" ")
label2.pack()


root.mainloop()