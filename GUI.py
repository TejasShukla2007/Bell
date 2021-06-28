from tkinter import *
main_window = Tk()
Label(main_window,text = "Speaking deaf-mute", fg="blue",bg="red").pack(side='top',fill="x")
Label(main_window,text="Bell",fg="white",bg="blue",font=('Serif',20)).pack(pady=30,padx=10,side="top",fill="x")
value = Entry(main_window,width=30)
value.pack()
def on_click():
    try:
        x = value.get()
        print(x)
    except:
        pass
Button(main_window,text="Enter",command=on_click).pack()
print(value)
main_window.mainloop()