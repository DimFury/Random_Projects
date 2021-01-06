from tkinter import *
import datetime
import time
import winsound


def alarm(set_alarm):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d-%m-%Y")
        date_stamp = Label(app,fg="limeGreen",bg="black", text="Current Set Date: %s" % date)
        box1.create_window(200,130, window=date_stamp)
        time_stamp = Label(app,fg="limeGreen",bg="black", text="Current Set Time: %s" % now)
        box1.create_window(200,150, window=time_stamp)
        if now == set_alarm:
            print("Wake Up Jeff")
        winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
        break

def _time():
    set_alarm = f"{Hours.get()}:{Mins.get()}:{Secs.get()}"
    alarm(set_alarm)

app = Tk()
app.title("ALARM CLOCK")
app.resizable(0,0)

box1=Canvas(app,bg='black', width = 400, height =400,)
box1.pack()


#time_format=Label(app, text= "Enter time in 24 hour format!", fg="red",bg="black",font="Arial").place(x=60,y=120)
#addTime = Label(app,text = "Hour  Min   Sec",font=60).place(x = 110)
#setYourAlarm = Label(app,text = "When to wake you up",fg="blue",relief = "solid",font=("Helevetica",7,"bold")).place(x=0, y=29)


#strings
Hours = IntVar()
Mins = IntVar()
Secs = IntVar()

#input time frame for alarm clock
hour_input= Spinbox(app,width=10, from_=1, to=24, textvariable=Hours)
box1.create_window(100,30, window=hour_input)

mins_input= Spinbox(app,width=10, from_=1, to=60, textvariable=Mins)
box1.create_window(200,30, window=mins_input)

secs_input= Spinbox(app,width=10, from_=1, to=60, textvariable=Secs)
box1.create_window(300,30, window=secs_input)


#create finalized alarm button
finalized = Button(app, text="Set Alarm", fg="limegreen", bg="black", width=50, command=_time)
box1.create_window(200,100, window=finalized)
app.mainloop()