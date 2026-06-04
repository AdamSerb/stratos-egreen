import time
import customtkinter as tk
import serial
from customtkinter import *

# setup serial
try:
    arduino = serial.Serial('COM7', 9600, timeout=0.1)
    time.sleep(2)
except:
    print("couldn't connect to arduino")

# FUNCTIONS
def set_auto():
    arduino.write(b'A')
    status_label.configure(text="MODE: AUTO", text_color="#2ecc71") # Green
    # Reset button colors for visual feedback
    btn_auto.configure(fg_color="#2ecc71")
    btn_manual.configure(fg_color="#3b3b3b")

def set_manual():
    arduino.write(b'M')
    status_label.configure(text="MODE: MANUAL", text_color="#e74c3c") # Red
    # Reset button colors
    btn_auto.configure(fg_color="#3b3b3b")
    btn_manual.configure(fg_color="#e74c3c")

def pump_toggle_event():
    if pump_var.get() == 1:
        arduino.write(b'1')
    else:
        arduino.write(b'0')

def update_data():
    try:
        if arduino.in_waiting > 0:
            raw_data = arduino.readline().decode('utf-8').strip()
            if raw_data:
                parts = raw_data.split(",")
                if len(parts) == 3:
                    label_soil_value.configure(text=f"{parts[0]}")
                    label_temp_value.configure(text=f"{parts[1]} °C")
                    label_hum_value.configure(text=f"{parts[2]} %")
    except Exception as e:
        print(f"error: {e}")
    gui.after(1000, update_data)

# GUI SETUP
set_appearance_mode("dark")
gui = CTk()
gui.title('Stratos Egreen Responsive')
gui.geometry('500x600')

# main container that expands
main_container = CTkFrame(gui, fg_color="transparent")
main_container.pack(expand=True, fill="both", padx=20, pady=20)

# HEADER
header_frame = CTkFrame(main_container, fg_color="transparent")
header_frame.pack(pady=(0, 20))

CTkLabel(header_frame, text='STRATOS', font=('Anton', 40, 'bold'), text_color='#2ecc71').pack()
status_label = CTkLabel(header_frame, text="MODE: AUTO", font=('Arial', 18, 'bold'), text_color="#2ecc71")
status_label.pack()

# DATA CARDS - Grid is better for responsiveness
data_container = CTkFrame(main_container, fg_color="#333333", corner_radius=15)
data_container.pack(pady=20, fill="x")
# Make columns grow equally
data_container.grid_columnconfigure((0, 1, 2), weight=1)

# Moisture
CTkLabel(data_container, text="MOISTURE", font=("Arial", 11, "bold")).grid(row=0, column=0, pady=(15,0))
label_soil_value = CTkLabel(data_container, text="--", font=("Arial", 24, "bold"), text_color="#3498db")
label_soil_value.grid(row=1, column=0, pady=(0,15))

# Temp
CTkLabel(data_container, text="TEMP", font=("Arial", 11, "bold")).grid(row=0, column=1, pady=(15,0))
label_temp_value = CTkLabel(data_container, text="--", font=("Arial", 24, "bold"), text_color="#e67e22")
label_temp_value.grid(row=1, column=1, pady=(0,15))

# Humidity
CTkLabel(data_container, text="HUMIDITY", font=("Arial", 11, "bold")).grid(row=0, column=2, pady=(15,0))
label_hum_value = CTkLabel(data_container, text="--", font=("Arial", 24, "bold"), text_color="#9b59b6")
label_hum_value.grid(row=1, column=2, pady=(0,15))

# CONTROL SECTION
pump_frame = CTkFrame(main_container, fg_color="transparent")
pump_frame.pack(pady=30)

CTkLabel(pump_frame, text="PUMP OVERRIDE", font=("Arial", 13, "bold")).pack()
pump_var = IntVar()
pump_switch = CTkSwitch(pump_frame, text="", command=pump_toggle_event,
                        variable=pump_var, width=120, height=50,
                        switch_width=100, switch_height=50,
                        progress_color="#2ecc71")
pump_switch.pack(pady=10)

# BUTTON SECTION
btn_frame = CTkFrame(main_container, fg_color="transparent")
btn_frame.pack(pady=20, fill="x")
btn_frame.grid_columnconfigure((0, 1), weight=1)

btn_auto = CTkButton(btn_frame, text="AUTO MODE", command=set_auto,
                     height=45, fg_color="#2ecc71", font=("Arial", 12, "bold"))
btn_auto.grid(row=0, column=0, padx=10, sticky="ew")

btn_manual = CTkButton(btn_frame, text="MANUAL MODE", command=set_manual,
                       height=45, fg_color="#3b3b3b", font=("Arial", 12, "bold"))
btn_manual.grid(row=0, column=1, padx=10, sticky="ew")

gui.after(1000, update_data)
gui.mainloop()