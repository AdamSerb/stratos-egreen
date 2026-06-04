from tkinter import *
application = Tk()
application.geometry('600x600')
icon = PhotoImage(file='logo.png')
application.iconphoto(True,icon)
application.title('Global Lens The News')
application.config(background='#002c6d')
photo = PhotoImage(file='logoclair.png')
label = Label(application,
              text='Global Lens The News',
              font=('antonio', 30),
              fg='white',
              bg='#002c6d',)
label.pack()
button = Button(application,text='click for more news !!')


def click():
    print('More news! ')

button.config(command=click)
button.config(font=('arial', 20))
button.config(bg='#3196f5')
button.config(activebackground='#002b54')
button.config(activeforeground='white')
button.pack()






application.mainloop()
