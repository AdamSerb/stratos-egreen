import customtkinter as ctk
import tkinter as tk
ctk.set_default_color_theme('dark-blue')
ctk.set_appearance_mode('dark')
app = ctk.CTk()
app.geometry('500x500')
app.title('toolbar')
toolbar = ctk.CTkFrame(app,
                   fg_color='#3d3d3d',
                      width=50)
toolbar.pack(side="left", fill="y")
toolbar.pack_propagate(flag=False)
namebar = ctk.CTkFrame(app,
                   fg_color='#3d3d3d',
                      height=30,
                      width=500,
                      corner_radius=0)
namebar.pack(side="top", fill="x")

label = ctk.CTkLabel(toolbar,
                    bg_color='#3d3d3d',
                    fg_color='#3d3d3d',
                    text='SMIYA CHAT',
                    text_color='#ffffff',
                    font=ctk.CTkFont(size=10, weight="bold"),
                    height=30,
                    width=50,
                    corner_radius=0)
label.pack(side='top', padx=0, pady=0)

chatbtn = ctk.CTkButton(toolbar,)

contact_icon = tk.PhotoImage(file='contactsicon.png')
contact_btn = ctk.CTkButton(toolbar,image=contact_icon,bg_color='#3d3d3d')
contact_btn.place(x=10, y=400)






app.mainloop()