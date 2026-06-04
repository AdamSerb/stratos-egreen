import serial
import customtkinter as tk
from customtkinter import CTkButton, CTkLabel
import time

arduino = serial.Serial('COM7', 9600)
time.sleep(2)

# --------- MODES ---------
def auto_mode():
    arduino.write(b'A')

def manual_mode():
    arduino.write(b'M')

# --------- PUMP ---------
def pump_on():
    arduino.write(b'1')

def pump_off():
    arduino.write(b'0')

# --------- FAN ---------
def fan_on():
    arduino.write(b'F')

def fan_off():
    arduino.write(b'f')

# --------- GUI ---------
gui = tk.CTk()
gui.title('Smart System')
gui.geometry('350x400')

label = CTkLabel(gui, text='Data: ---', font=("Arial", 18))
label.pack(pady=15)

# Buttons
CTkButton(gui, text='AUTO MODE', command=auto_mode).pack(pady=5)
CTkButton(gui, text='MANUAL MODE', command=manual_mode).pack(pady=5)

CTkButton(gui, text='Pump ON', command=pump_on).pack(pady=5)
CTkButton(gui, text='Pump OFF', command=pump_off).pack(pady=5)

CTkButton(gui, text='Fan ON', command=fan_on).pack(pady=5)
CTkButton(gui, text='Fan OFF', command=fan_off).pack(pady=5)

# --------- SENSOR UPDATE ---------
def update_sensor():
    if arduino.in_waiting:
        try:
            data = arduino.readline().decode().strip()
            label.configure(text=data)
        except:
            pass

    gui.after(500, update_sensor)

update_sensor()

gui.mainloop()







