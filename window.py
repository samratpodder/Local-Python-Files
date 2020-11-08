import tkinter

var1=None
def myClick():
    myLabel = tkinter.Label(window,text="You will be redirected to Whatsapp.")
    myLabel.grid(row=3)
    print(var1.get())


window = tkinter.Tk()
window.title("Whatsapp")
tkinter.Label(window,text = "Number",fg="black",bg="Green").grid(row=0,column=1)
var1=tkinter.Entry(window,width=30).grid(row=0,column=2)
tkinter.Label(window,text = "Text",fg="black",bg="Green").grid(row=1,column=1)
tkinter.Entry(window,width=120,).grid(row=1,column=2)
tkinter.Button(window,text="SEND",command = myClick).grid(row=2,column=2)






window.mainloop()