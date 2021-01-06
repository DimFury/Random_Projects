import random
from random_word import RandomWords
from tkinter import *


app = Tk()
app.resizable(0,0)
app.title(" Random Password Generator Demo ")

box1=Canvas(app,bg='black', width = 400, height =500,)
box1.pack()

label3 = Label(app, fg='white', bg='black', text ='Input For a Generated New Password')
label3.config(font=("Courier", 10))
box1.create_window(200,110, window=label3)

passfield = Entry(app)
box1.create_window(200,140, window=passfield)

paslength = IntVar() #set integer
S_pin = Spinbox(app, from_=6, to=32, textvariable=paslength, width=10)
box1.create_window(200, 170, window=S_pin)


#setting random values based on input
def getrandom():

    user = passfield.get()

    n = paslength.get()

    #results are conjoing by ''.join while the input is selecting 
    #the variable and determining for variable in range of numeric values
    results = ''.join(random.choice(user) for _ in range(n))

    label = Label(app,fg="limegreen",bg='black', text=results)
    label.config(font=("Courier", 12))
    box1.create_window(200,230, window=label)

    

button1 = Button(text='Generate Random Password',bg='aqua',fg='black', 
                    relief=RIDGE ,command=getrandom)
button1.config(font=("Arial", 10))
box1.create_window(200,200, window=button1)

#label 2 -
label2 = Label(app, fg="white",bg='black', text='Here is your random password')
label2.config(font=("Courier", 10))
box1.create_window(200,260, window=label2)


#defy email input values

app.mainloop()