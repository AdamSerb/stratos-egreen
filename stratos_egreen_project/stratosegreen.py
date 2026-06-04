import time
import serial
import customtkinter as tk
from customtkinter import *

# setup
try:

    arduino = serial.Serial('COM7', 9600, timeout=0.1)
    time.sleep(2)
    print("Dashboard Connected!")
except Exception as e:
    print(f"Serial Error: {e}")
    class FakeSerial:
        in_waiting = 0
        def write(self, m): pass
        def readline(self): return b""
    arduino = FakeSerial()

# fonctions
def set_auto():
    arduino.write(b'A')
    status_lbl.configure(text="MODE: AUTO", text_color="#2ecc71")
    pump_frame.pack_forget()
    plant_icon.pack(pady=20)
    tune_frame.pack(fill="x", pady=20)
    btn_auto.configure(fg_color="#2ecc71", text_color="black")
    btn_manual.configure(fg_color="#333", text_color="white")

def set_manual():
    arduino.write(b'M')
    status_lbl.configure(text="MODE: MANUAL", text_color="#e67e22")
    plant_icon.pack_forget()
    tune_frame.pack_forget()
    pump_frame.pack(pady=60, before=btn_frame)
    btn_auto.configure(fg_color="#333", text_color="white")
    btn_manual.configure(fg_color="#e67e22", text_color="black")

def update_threshold(val):
    thresh = int(float(val))
    arduino.write(f"S{thresh}\n".encode())
    thresh_display.configure(text=f"Trigger Point: {thresh}")

def pump_toggle():
    arduino.write(b'1' if pump_var.get() == 1 else b'0')

def update_gui():
    try:
        if arduino.in_waiting > 0:
            raw = arduino.readline().decode('utf-8').strip()
            parts = raw.split(",")
            if len(parts) == 3:
                soil_val.configure(text=parts[0])
                temp_val.configure(text=f"{parts[1]}°C")
                hum_val.configure(text=f"{parts[2]}%")
    except: pass
    gui.after(400, update_gui)


set_appearance_mode("dark")
gui = CTk()
gui.title("Stratos E-Green")
gui.geometry("500x750")

main = CTkFrame(gui, fg_color="transparent")
main.pack(expand=True, fill="both", padx=40, pady=30)

#Header
header = CTkFrame(main, fg_color="transparent")
header.pack(fill="x")
CTkLabel(header, text="STRATOS", font=("Anton", 55, "bold")).pack()
status_lbl = CTkLabel(header, text="MODE: AUTO", font=("Arial", 18, "bold"), text_color="#2ecc71")
status_lbl.pack()

#Stats Card
card = CTkFrame(main, fg_color="#1a1a1a", corner_radius=25, border_width=1, border_color="#333")
card.pack(fill="x", pady=30)
card.grid_columnconfigure((0,1,2), weight=1)

def make_stat(col, title, color):
    CTkLabel(card, text=title, font=("Arial", 11, "bold"), text_color="#777").grid(row=0, column=col, pady=(20,0))
    lbl = CTkLabel(card, text="--", font=("Arial", 30, "bold"), text_color=color)
    lbl.grid(row=1, column=col, pady=(0,20))
    return lbl

soil_val = make_stat(0, "SOIL", "#3498db")
temp_val = make_stat(1, "TEMP", "#e67e22")
hum_val = make_stat(2, "HUMIDITY", "#9b59b6")

# Auto mode
plant_icon = CTkLabel(main, text="🌿", font=("Arial", 160))
plant_icon.pack(pady=20)

tune_frame = CTkFrame(main, fg_color="transparent")
tune_frame.pack(fill="x", pady=20)
thresh_display = CTkLabel(tune_frame, text="Trigger Point: 500", font=("Arial", 13, "bold"))
thresh_display.pack()
slider = CTkSlider(tune_frame, from_=0, to=1023, command=update_threshold,
                   button_color="#2ecc71", button_hover_color="#27ae60", progress_color="#2ecc71")
slider.set(500)
slider.pack(fill="x", pady=10)


pump_frame = CTkFrame(main, fg_color="transparent")
CTkLabel(pump_frame, text="MANUAL PUMP OVERRIDE", font=("Arial", 12, "bold"), text_color="#aaa").pack()
pump_var = IntVar()
pump_sw = CTkSwitch(pump_frame, text="", command=pump_toggle, variable=pump_var,
                    width=130, height=60, switch_width=110, switch_height=55,
                    progress_color="#2ecc71", button_hover_color="#d1d1d1")
pump_sw.pack(pady=20)

# buttons
btn_frame = CTkFrame(main, fg_color="transparent")
btn_frame.pack(side="bottom", fill="x", pady=(20,0))
btn_frame.grid_columnconfigure((0,1), weight=1)

btn_auto = CTkButton(btn_frame, text="AUTO", command=set_auto, height=55, corner_radius=15,
                     fg_color="#2ecc71", hover_color="#27ae60", text_color="black", font=("Arial", 15, "bold"))
btn_auto.grid(row=0, column=0, padx=8, sticky="ew")

btn_manual = CTkButton(btn_frame, text="MANUAL", command=set_manual, height=55, corner_radius=15,
                       fg_color="#333", hover_color="#444", font=("Arial", 15, "bold"))
btn_manual.grid(row=0, column=1, padx=8, sticky="ew")

update_gui()
gui.mainloop()