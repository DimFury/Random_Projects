from tkinter import *

expression = ""

def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)


def equalpress():
    try:
        global expression

        total = str(eval(expression))
        equation.set(total)

        expression = ""
    
    except:
        equation.set(" Error ")
        expression = " "
def clear():
    global expression
    expression = ""
    equation.set("")


if __name__ == "__main__":
    app = Tk()

    app.title('Calculator')

    app.geometry("1300x720")

    equation = StringVar()
    expression_field = Entry(app, fg='limegreen', bg='black',font="CourierNew 24 italic", justify="center" ,textvariable=equation )
    expression_field.grid(columnspan=4, ipady=40, ipadx=340)

    equation.set('Enter Your Equation')
    
    #Button Allocations

    button_negate = Button(app, text='+/-', fg='black', bg='light grey', 
                     command=lambda: press(), height=3, width=7, pady= 10, padx=100)
    button_negate.grid(row=8, column=0)

    button0 = Button(app, text=' 0 ', fg='black', bg='light grey', 
                     command=lambda: press(0), height=3, width=7, pady= 10, padx=100)
    button0.grid(row=8, column=1)

    button1 = Button(app, text=' . ', fg='black', bg='light grey', 
                     command=lambda: press(), height=3, width=7, pady= 10, padx=100)
    button1.grid(row=8, column=2)
    button2 = Button(app, text=' = ', fg='black', bg='light grey', 
                    command=equalpress, height=3, width=7, pady= 10, padx=100)
    button2.grid(row=8, column=3)

    #Button second Row

    button1 = Button(app, text=' 1 ', fg='black', bg='light grey', 
                     command=lambda: press(1), height=3, width=7, pady= 10, padx=100) 
    button1.grid(row=7, column=0) 

    button2 = Button(app, text=' 2 ', fg='black', bg='light grey',
                    command=lambda: press(2), height=3, width=7, pady=10, padx=100)   
    button2.grid(row=7, column=1)

    button3 = Button(app, text=' 3 ', fg='black', bg='light grey',
                    command=lambda: press(3), height=3, width=7, pady=10, padx=100)   
    button3.grid(row=7, column=2)

    button4 = Button(app, text=' + ', fg='black', bg='light grey',
                    command=lambda: press("+"), height=3, width=7, pady=10, padx=100)   
    button4.grid(row=7, column=3)

    # Button third Row
    button5 = Button(app, text=' 4 ', fg='black', bg='light grey', 
                     command=lambda: press(4), height=3, width=7, pady= 10, padx=100) 
    button5.grid(row=6, column=0) 

    button6 = Button(app, text=' 5 ', fg='black', bg='light grey',
                    command=lambda: press(5), height=3, width=7, pady=10, padx=100)   
    button6.grid(row=6, column=1)

    button7 = Button(app, text=' 6 ', fg='black', bg='light grey',
                    command=lambda: press(6), height=3, width=7, pady=10, padx=100)   
    button7.grid(row=6, column=2)

    button8 = Button(app, text=' - ', fg='black', bg='light grey',
                    command=lambda: press("-"), height=3, width=7, pady=10, padx=100)   
    button8.grid(row=6, column=3)

    #button fourth Row
    button9 = Button(app, text=' 7 ', fg='black', bg='light grey', 
                     command=lambda: press(7), height=3, width=7, pady= 10, padx=100) 
    button9.grid(row=5, column=0) 

    button10 = Button(app, text=' 8 ', fg='black', bg='light grey',
                    command=lambda: press(8), height=3, width=7, pady=10, padx=100)   
    button10.grid(row=5, column=1)

    button11 = Button(app, text=' 9 ', fg='black', bg='light grey',
                    command=lambda: press(9), height=3, width=7, pady=10, padx=100)   
    button11.grid(row=5, column=2)

    button12 = Button(app, text=' * ', fg='black', bg='light grey',
                    command=lambda: press("*"), height=3, width=7, pady=10, padx=100)   
    button12.grid(row=5, column=3)
    # clear screen
    button13 = Button(app, text=' C ', fg='black', bg='light grey',
                    command=clear, height=3, width=7, pady=10, padx=100)   
    button13.grid(row=3, column=3)

    #Exit App
    button_destroy = Button(app, text=' Exit ', fg='white', bg='red', 
                        command=app.quit, height=3, width=7, pady= 10, padx=10)
    button_destroy.grid(row=3, column=5, padx=50)
    
    app.mainloop()
    app.quit()
