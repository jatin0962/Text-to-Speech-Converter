import tkinter as tk

from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import pyttsx3
import os

root = Tk()
root.title("Text to speech")
root.geometry("900x450+200+200")
root.resizable(False,False)
root.configure(bg="#305065")

engine=pyttsx3.init()

def speaknow():
    text=t_area.get(1.0,END)
    gender=gender_combo.get()
    speed=speed_combo.get()
    voices=engine.getProperty('voices')

    def setvoice():
        if (gender=='Male'):
            engine.setProperty('voice',voices[0].id)
            engine.say(text)
            engine.runAndWait()
        else:
             engine.setProperty('voice',voices[1].id)
             engine.say(text)
             engine.runAndWait()
    if(text):
        if(speed=='Fast'):
          engine.setProperty('rate',250)
          setvoice()
        elif(speed=='Normal'):
          engine.setProperty('rate',150)
          setvoice()
        else:
            engine.setProperty('rate',60)
            setvoice()

def download():
    text=t_area.get(1.0,END)
    gender=gender_combo.get()
    speed=speed_combo.get()
    voices=engine.getProperty('voices')

    def setvoice():
        if (gender=='Male'):
            engine.setProperty('voice',voices[0].id)
            path=filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text,'text.mp3')
            engine.runAndWait()
        else:
             engine.setProperty('voice',voices[1].id)
             path=filedialog.askdirectory()
             os.chdir(path)
             engine.save_to_file(text,'text.mp3')
             engine.runAndWait()
    if(text):
        if(speed=='Fast'):
          engine.setProperty('rate',250)
          setvoice()
        elif(speed=='Normal'):
          engine.setProperty('rate',150)
          setvoice()
        else:
            engine.setProperty('rate',60)
            setvoice()
            

image_icon=PhotoImage(file="speaker.png")
root.iconphoto(False,image_icon)


tframe=Frame(root,bg="#725A7A",width=900,height=100)
tframe.place(x=0,y=0)

Logo=PhotoImage(file="speaker.png")
Label(tframe,image=Logo,bg="white").place(x=10,y=5)

Label(tframe,text="TEXT TO SPEECH",font="arial 20 bold",bg="white",fg="black").place(x=100,y=30)


t_area=Text(root,font="Robote 20",bg="white",relief=GROOVE,wrap=WORD)
t_area.place(x=10,y=150,width=500,height=250)

gender_combo=ttk.Combobox(root,values=['Male','Female'],font="arial 14",state="r",width=10)
gender_combo.place(x=550,y=200)
gender_combo.set('Gender')

speed_combo=ttk.Combobox(root,values=['Fast','Normal','Slow'],font="arial 14",state="r",width=10)
speed_combo.place(x=730,y=200)
speed_combo.set('Speed')

imageicon=PhotoImage(file="speak.png")
btn=Button(root,text="Speak",compound=LEFT,image=imageicon,width=130,font="arial 14 bold",command=speaknow)
btn.place(x=550,y=280)

imageicon2=PhotoImage(file="download.png")
save=Button(root,text="Save",compound=LEFT,image=imageicon2,width=130,bg="#39c790",font="arial 14 bold",command=download)
save.place(x=730,y=280)



root.mainloop()
