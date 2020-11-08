import tkinter
import webbrowser


def myClick():
    myLabel = tkinter.Label(window,text="You will be redirected to Whatsapp.")
    myLabel.grid(row=3)
    num=var1.get()
    message = var2.get()
    word = message.replace(" ","%20")
    url = "wa.me/"+num+"?text="+word
    webbrowser.open(url)


window = tkinter.Tk()
window.title("Whatsapp")
tkinter.Label(window,text = "Number",fg="black",bg="Green").grid(row=0,column=1)
var1=tkinter.Entry(window,width=30)
var1.grid(row=0,column=2)
tkinter.Label(window,text = "Text",fg="black",bg="Green").grid(row=1,column=1)
var2=tkinter.Entry(window,width=120,)
var2.grid(row=1,column=2)
tkinter.Button(window,text="SEND",command = myClick).grid(row=2,column=2)


window.mainloop()
