import customtkinter
from customtkinter import *
customtkinter.set_default_color_theme('green')
app = CTk()
app.geometry("1080x720")
app.title("Messagerie")
app.config(bg  ='#389C86')
'''
    framename = CTkFrame(master=app)
framename.configure(height=40,fg_color = '#389C86')
framename.pack(fill=X, side=TOP)

frametool = CTkFrame(master=app,
                 width=60,)
frametool.configure(width=60,fg_color = '#389C86')
frametool.pack(fill=Y,  side=LEFT )
'''
# Toolbar
toolbar = CTkFrame(app, height=50)
toolbar.pack(side="left", fill="y")

toolbar_label = CTkLabel(
    toolbar,
    text="Chat App",
    font=CTkFont(size=16, weight="bold")
)
toolbar_label.pack(padx=15, pady=10)

framecont = CTkFrame(master=app,
                 width=300,
                height=680,
                 corner_radius=20)
framecont.configure(bg_color='#389C86',fg_color = '#389C54')
framecont.pack(padx=60, side=LEFT)

framedisc = CTkFrame(master=app,
                 height=200,
                 width=200,
                 corner_radius=8)
framedisc.configure(height =680,width=720,fg_color = '#4E9C38',bg_color='#389C86')
framedisc.pack( side=RIGHT,padx=0, pady=0)









app.mainloop()