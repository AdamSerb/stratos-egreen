import customtkinter as tk

# ---------- Global Setup ----------
tk.set_appearance_mode("dark")
tk.set_default_color_theme("dark-blue")

root = tk.CTk()
root.title("Learn")
root.geometry("300x500")
root.configure(fg_color="#281c4f")

# ---------- Switch Buttons ----------
def clear_page():
    for widget in page_frame.winfo_children():
        widget.destroy()

def switch_option(switch_to):
    clear_page()

    if switch_to == "login":
        login_btn.configure(fg_color="white", text_color="black")
        signup_btn.configure(fg_color="#1F6AA5", text_color="white")
        login_page()
    else:
        signup_btn.configure(fg_color="white", text_color="black")
        login_btn.configure(fg_color="#1F6AA5", text_color="white")
        signup_page()

# ---------- Top Buttons ----------
login_btn = tk.CTkButton(
    root,
    text="Login",
    font=("Arial", 20, "bold"),
    width=120,
    height=40,
    corner_radius=20,
    border_width=2,
    border_color="white",
    fg_color="white",
    text_color="black",
    command=lambda: switch_option("login")
)
login_btn.place(x=25, y=40)

signup_btn = tk.CTkButton(
    root,
    text="Sign Up",
    font=("Arial", 20, "bold"),
    width=120,
    height=40,
    corner_radius=20,
    border_width=2,
    border_color="white",
    fg_color="#1F6AA5",
    text_color="white",
    command=lambda: switch_option("signup")
)
signup_btn.place(x=155, y=40)

# ---------- Page Container ----------
page_frame = tk.CTkFrame(root, width=250, height=370, corner_radius=10)
page_frame.place(x=25, y=110)

# ---------- Login Page ----------
def login_page():
    tk.CTkLabel(
        page_frame,
        text="Login",
        font=("Arial", 20, "bold")
    ).place(x=90, y=10)

    tk.CTkEntry(
        page_frame,
        width=230,
        height=35,
        placeholder_text="Email Address",
        corner_radius=10
    ).place(x=10, y=80)

    tk.CTkEntry(
        page_frame,
        width=230,
        height=35,
        placeholder_text="Password",
        show="*",
        corner_radius=10
    ).place(x=10, y=150)

    tk.CTkButton(
        page_frame,
        text="Login",
        width=200,
        height=45,
        font=("Arial", 18, "bold")
    ).place(x=25, y=250)

# ---------- Sign Up Page ----------
def signup_page():
    tk.CTkLabel(
        page_frame,
        text="Sign Up",
        font=("Arial", 20, "bold")
    ).place(x=80, y=10)

    tk.CTkEntry(
        page_frame,
        width=230,
        height=35,
        placeholder_text="Email Address",
        corner_radius=10
    ).place(x=10, y=70)

    tk.CTkEntry(
        page_frame,
        width=230,
        height=35,
        placeholder_text="Password",
        show="*",
        corner_radius=10
    ).place(x=10, y=130)

    tk.CTkEntry(
        page_frame,
        width=230,
        height=35,
        placeholder_text="Confirm Password",
        show="*",
        corner_radius=10
    ).place(x=10, y=190)

    tk.CTkButton(
        page_frame,
        text="Sign Up",
        width=200,
        height=45,
        font=("Arial", 18, "bold")
    ).place(x=25, y=290)

# ---------- Initial Page ----------
login_page()

root.mainloop()













