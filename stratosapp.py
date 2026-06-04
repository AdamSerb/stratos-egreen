import serial
import time
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock

# Connect to Arduino
arduino = serial.Serial('COM7', 9600)
time.sleep(2)

class MainApp(App):

    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        self.label = Label(text="Moisture: ---", font_size=30)
        self.layout.add_widget(self.label)

        btn_on = Button(text="ON", font_size=25)
        btn_on.bind(on_press=self.relay_on)
        self.layout.add_widget(btn_on)

        btn_off = Button(text="OFF", font_size=25)
        btn_off.bind(on_press=self.relay_off)
        self.layout.add_widget(btn_off)

        # Update sensor every 0.5s
        Clock.schedule_interval(self.update_sensor, 0.5)

        return self.layout

    def relay_on(self, instance):
        arduino.write(b'1')

    def relay_off(self, instance):
        arduino.write(b'0')

    def update_sensor(self, dt):
        if arduino.in_waiting:
            value = arduino.readline().decode().strip()

            try:
                percent = int((1023 - int(value)) / 1023 * 100)
                self.label.text = f"Moisture: {percent}%"
            except:
                pass

if __name__ == "__main__":
    MainApp().run()
