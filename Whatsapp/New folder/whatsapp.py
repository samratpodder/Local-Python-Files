import tkinter
import webbrowser
import math
import random


def myClick():
    myLabel = tkinter.Label(window,text="OTP Ready")
    myLabel.grid(row=3)
    num=var1.get()
    string = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    OTP = "" 
    length = len(string) 
    for i in range(6): 
        OTP += string[math.floor(random.random() * length)]
    url = "wa.me/"+num+"?text=Your%20OTP%20Is%20:%20"+OTP
    webbrowser.open_new_tab(url)


window = tkinter.Tk()
window.title("Whatsapp")
tkinter.Label(window,text = "Number",fg="black",bg="Green").grid(row=0,column=1)
var1=tkinter.Entry(window,width=30)
var1.grid(row=0,column=2)
#tkinter.Label(window,text = "Text",fg="black",bg="Green").grid(row=1,column=1)
#var2=tkinter.Entry(window,width=120,)
#var2.grid(row=1,column=2)
tkinter.Button(window,text="SEND",command = myClick).grid(row=2,column=2)


window.mainloop()
