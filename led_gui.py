import tkinter as tk
import RPi.GPIO as GPIO

# Setup GPIO
LED_PINS = {'Red': 17, 'Green': 27, 'Blue': 22}
GPIO.setmode(GPIO.BCM)
for pin in LED_PINS.values():
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

# Function to turn on the selected LED
def select_led(led_color):
    for color, pin in LED_PINS.items():
        GPIO.output(pin, GPIO.HIGH if color == led_color else GPIO.LOW)

# Create the main window
root = tk.Tk()
root.title("LED Control Panel")

# Create radio buttons
led_var = tk.StringVar()
for color, pin in LED_PINS.items():
    tk.Radiobutton(root, text=color, variable=led_var, value=color, command=lambda: select_led(led_var.get())).pack()

# Create an exit button
exit_button = tk.Button(root, text="Exit", command=root.destroy)
exit_button.pack()

# Run the GUI loop
root.mainloop()

# Cleanup GPIO when the GUI is closed
GPIO.cleanup()
