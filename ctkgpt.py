from PIL import Image
import customtkinter as ctk
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class FakeChatService:
    def send(self, text):
        print("Sending to backend:", text)

chat_service = FakeChatService()

app = ctk.CTk()
app.title("Convo")
app.geometry("1000x650")

# name
appname = ctk.CTkFrame(app, height=50)
appname.pack(side="top", fill="x")

title = ctk.CTkLabel(appname, text="Convo",
                     font=ctk.CTkFont(size=18, weight="bold"))
title.pack(side="left", padx=15, pady=10)

# Main area
main_area = ctk.CTkFrame(app)
main_area.pack(fill="both", expand=True)

# Contacts
contacts = ctk.CTkFrame(main_area, width=280)
contacts.pack(side="left", fill="y")

contacts_label = ctk.CTkLabel(
    contacts, text="Contacts",
    font=ctk.CTkFont(size=14, weight="bold")
)
contacts_label.pack(pady=10)

contacts_list = ctk.CTkScrollableFrame(contacts)
contacts_list.pack(fill="both", expand=True, padx=10, pady=10)

for name in ["Alice", "Bob", "Charlie", "Hamid", "Noelle"]:
    btn = ctk.CTkButton(contacts_list, text=name)
    btn.pack(fill="x", pady=5)

# Discussion
discussion = ctk.CTkFrame(main_area)
discussion.pack(side="right", fill="both", expand=True)

messages = ctk.CTkScrollableFrame(discussion)
messages.pack(fill="both", expand=True, padx=10, pady=10)

def add_message(text, sender="me"):
    align = "e" if sender == "me" else "w"
    color = "#075E54" if sender == "me" else "#2a2a2a"

    bubble = ctk.CTkLabel(
        messages,
        text=text,
        wraplength=400,
        fg_color=color,
        corner_radius=12,
        padx=10,
        pady=6
    )
    bubble.pack(anchor=align, pady=4, padx=10)

add_message("Hey 👋", "other")
add_message("helloo", "me")

# Input bar
input_bar = ctk.CTkFrame(discussion, height=60)
input_bar.pack(side="bottom", fill="x", padx=10, pady=10)

message_entry = ctk.CTkEntry(input_bar, placeholder_text="Type a message...")
message_entry.pack(side="left", fill="x", expand=True, padx=(0, 10))

def send_message():
    text = message_entry.get()
    if text.strip():
        chat_service.send(text)
        add_message(text, "me")
        message_entry.delete(0, "end")

send_btn = ctk.CTkButton(input_bar, text="Send", width=80, command=send_message)
send_btn.pack(side="right")

app.mainloop()