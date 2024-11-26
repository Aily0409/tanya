import tkinter

def bmi_calculator():
    user_input= entry.get().lower()
    results={}
    height= int(instructions1.get())
    weight= int(instructions2.get())
    bmi= weight/(height**2)
    if bmi <= 16:
        
    
    
    
    
    



root=tkinter.Tk()
root.geometry("400x400")
root.title("BMI Calculator")

instructions1 = tkinter.Label(root, text="Enter your height in meters:")
instructions1.pack(pady=10)

entry = tkinter.Entry(root, width=10)
entry.pack(pady=10)

instructions2 = tkinter.Label(root, text= "Enter your weight in kilograms:")
instructions2.pack(pady=10)

entry = tkinter.Entry(root, width=10)
entry.pack(pady=10)

button = tkinter.Button(root, text="Calculate BMI")
button.pack(pady=10)

result= tkinter.Label(root, text="")
result.pack(pady=10)

root.mainloop()