import tkinter as Tk
from datetime import datetime , timezone

def Update_clock():
    local_time=datetime.now().astimezone()
    utc_time=datetime.now(timezone.utc)
    local_lable.config(text = f"local time: {local_time.strftime('%H:%M:%S')}")
    local_lable.config(text = f"utc time: {utc_time.strftime('%H:%M:%S')}")
    root.after(1000,Update_clock)


root = tk.Tk()
root.title("Count Down")
root.geometry("350x220")
tk.Label(root, text="enter your text in S : ", font=("Courier" , 24)).pack(pady=10)

entry_time= tk.Entry(root, font=("Courier" , 24), width=10)
entry_time.pack(pady=10)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

start_button = tk.Button(
    btn_frame,text="start", width=10, command=start_button,bg="#ffffff",fg="white"
)
start_button.grid(row=0,column=0,padx=5)


stop_button = tk.Button(
    btn_frame,text="start", width=10, command=stop_button,state=disabled,bg="#ffffff",fg="white"
)
stop_button.grid(row=0,column=0,padx=5)



timer_display = tk.Label(root, text="")
local_lable = tk.Label(root , font=("Courier" , 24))
local_lable.pack()
utc_lable = tk.Label(root , font=("Courier" , 24))
utc_lable.pack()
Update_clock()
root.mainloop()
    