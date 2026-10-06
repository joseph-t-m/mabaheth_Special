import tkinter as tk
from datetime import datetime , timezone

def Update_clock():
    local_time=datetime.now().astimezone()
    utc_time=datetime.now(timezone.utc)
    local_lable.config(text = f"local time: {local_time.strftime('%H:%M:%S')}")
    local_lable.config(text = f"utc time: {utc_time.strftime('%H:%M:%S')}")
    root.after(1000,Update_clock)
root = tk.Tk()
root.title("Time")
local_lable = tk.Label(root , font=("Courier" , 24))
local_lable.pack()
utc_lable = tk.Label(root , font=("Courier" , 24))
utc_lable.pack()
Update_clock()
root.mainloop()
    