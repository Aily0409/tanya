import tkinter

def calculate_bmi():
    height = float(entry1.get())
    weight = float(entry2.get())
    bmi = weight/(height*height)
    results = bmi
    
    
    if results<= 16:
        result.config(text=f"BMI: {results}Severe Thinness")
    elif 16<results<=17:
        result.config(text=f"BMI:{results} Mild Thinness")
    elif 17 < results <= 18.5:
        result.config(text=f"BMI:{results} Moderate Thinness")
    elif 18.5 < results<= 25:
        result.config(text=f"BMI:{results} Normal")
    elif 25 < results <=30:
        result.config(text=f"BMI:{results} Overweight")
    elif 30 <= results <= 35:
       result.config(text=f"BMI:{results} Obese Class I")
    elif 35 <= results <= 40:
        result.config(text=f"BMI:{results} Obese Class II")
    elif results>40:
        result.config(text=f"BMI:{results} Obese Class III")
    
    
root=tkinter.Tk()
root.geometry("400x400")
root.title("BMI Calculator")

instructions1 = tkinter.Label(root, text="Enter your height in meters:")
instructions1.pack(pady=10)

entry1 = tkinter.Entry(root, width=10)
entry1.pack(pady=10)

instructions2 = tkinter.Label(root, text= "Enter your weight in kilograms:")
instructions2.pack(pady=10)

entry2 = tkinter.Entry(root, width=10)
entry2.pack(pady=10)

button = tkinter.Button(root, text="Calculate BMI", command=calculate_bmi)
button.pack(pady=10)  

result= tkinter.Label(root, text="")
result.pack(pady=10) 

root.mainloop()