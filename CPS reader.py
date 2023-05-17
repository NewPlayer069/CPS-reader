import tkinter as tk
import time

# Constants
UPDATE_INTERVAL = 1000  # Update interval in milliseconds (1 second)

# Global variables
clicks = 0
start_time = 0

def increment_counter(event=None):
    global clicks, start_time
    if clicks == 0:
        start_time = time.time()  # Record the start time
    clicks += 1

def calculate_cps():
    global clicks, start_time
    elapsed_time = time.time() - start_time
    cps = clicks / elapsed_time if elapsed_time > 0 else 0
    return cps

def update_label():
    cps = calculate_cps()
    label.config(text=f"CPS: {cps:.2f}")
    root.after(UPDATE_INTERVAL, update_label)

def close_window(event=None):
    root.destroy()

root = tk.Tk()
root.title("CPS Reader")
root.bind("<Button-1>", increment_counter)
root.bind("<Escape>", close_window)

label = tk.Label(root, text="CPS: 0.00", font=("Arial", 24))
label.pack(pady=20)

root.after(UPDATE_INTERVAL, update_label)
root.mainloop()