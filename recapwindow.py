from tkinter import *
window = Tk()
window.geometry("1080x720")
window.title("The Final Countdown")
window.config(background ='#7A85C1')

label = Label(window, text="Click here")
label.config(font=("courier new", 40),
             background='#B2B0E8',
             foreground='black')
label.pack()


count = 0

def click():
    global count
    count += 1
    print(count)


button = Button(window, text="Click me",
                background='#3B38A0',
               activebackground='#1A2A80', )




button.pack()






window.mainloop()