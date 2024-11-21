import tkinter

m = tkinter.Tk()

#Widgets

m.title("Top 100 reasons to why my cats are the best and the rest are lame")

#labels
#l =tkinter.Label(m, text="TOP NUMBER 1: Because they are my cats, duh")
#l.pack()

#button
#b = tkinter.Button(m, text="There are way better cats than them", command=m.destroy, width=40)
#b.pack()

#Inputs
fn_label = tkinter.Label(m, text="Do you wear wigs?").grid(row=0)
ln_label=tkinter.Label(m, text="Have you worn wigs?").grid(row=1)
ww_label=tkinter.Label(m, text="Will you wear wigs?").grid(row=2)
www_label=tkinter.Label(m, text="When will you wear wigs?").grid(row=3)
fn_input=tkinter.Entry(m).grid(row=0, column=1)
ln_input=tkinter.Entry(m).grid(row=1, column=1)
ww_input=tkinter.Entry(m).grid(row=2, column=1)
www_input=tkinter.Entry(m).grid(row=3, column=1)

#Checknoxes
#male=tkinter.IntVar()
#tkinter.Checkbutton(m, text="Cats lover", variable=male).grid(row=4, sticky=tkinter.W)
#female=tkinter.IntVar()
#tkinter.Checkbutton(m, text="Dogs lover", variable=female).grid(row=5, sticky=tkinter.W)

#Radio buttons
#group=tkinter.IntVar()
#tkinter.Radiobutton(m, text="A", variable=group, value="A").grid(row=7, sticky=tkinter.W)
#tkinter.Radiobutton(m, text="B", variable=group, value="B").grid(row=8, sticky=tkinter.W)
#tkinter.Radiobutton(m, text="C", variable=group, value="C").grid(row=9, sticky=tkinter.W)

#List box
#lb=tkinter.Listbox()
#lb.insert(1,"Have")
#lb.insert(2, "you")
#lb.insert(3, "worn")
#lb.insert(4, "wigs")
#lb.pack()

#Scrollbar
#scrollbar= tkinter.Scrollbar(m)
#scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
#giant_list= tkinter.Listbox(m, yscrollcommand=scrollbar.set)

#for line in range(100):
    #giant_list.insert(tkinter.END, "This is line number " +str(line))

#giant_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
    

#Menu
menu1 =tkinter.Menu(m)
m.config(menu=menu1)
filemenu = tkinter.Menu(menu1)
menu1.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New")



m.mainloop()