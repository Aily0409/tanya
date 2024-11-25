import tkinter

def count_ocurrences():
    user_input= entry.get().lower().replace("","")
    char_count={}
    
    for char in user_input:
        current_count= char_count.get(char, 0)
        char_count[char]=current_count +1
        
        
    result.config(text= str(char_count))
    
root=tkinter.Tk()
root.geometry("400x400")
root.title("Character Counter")

instructions= tkinter.Label(root, text="Let me count you letters")
instructions.pack(pady=10)

entry = tkinter.Entry(root, width=10)
entry.pack(pady=10)

button = tkinter.Button(root, text="Press", command=count_ocurrences)
button.pack(pady=10)

result = tkinter.Label(root, text="")
result.pack(pady=10)

root.mainloop()