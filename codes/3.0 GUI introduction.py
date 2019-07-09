import tkinter as tk

window=tk.Tk()
#creating the main window as window

font1='calibri 15 bold'

def btn_func():

    #print('PRESSED!')
    label1.config(text='HELLO PYTHON',bg='green')

label1=tk.Label(window,text='HELLO TKINTER',bg='RoyalBlue1',fg='white',font=font1)
label1.grid(row=0,column=0) #position

button1=tk.Button(window,text='PRESS',bg='red',fg='white',font=font1,height=1,width=10,command=btn_func)
button1.grid(row=1,column=0)

window.mainloop()
