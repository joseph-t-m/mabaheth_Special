import tkinter as Tk
from tkinter import messagebox
            

def start_timer():
    try:
        total = int(entry_time.get())
        if total <= 0:
            messagebox.showwarning = ("warn", "must be greater than ZERO")
            return
        running[0] = True
        start_button.config(state="disabled")
        stop_button.config(state="normal")
        run_countdown(total)
    except ValueError:
        messagebox.showerror("warn", "must be greater than ZERO!")


def run_countdown(t):
    mins, secs = divmod(t, 60)
    timer_display.config(text=f"{mins:02d} : {secs:02d}")
    if t > 0 and running[0]:
        root.after(1000, run_countdown, t - 1)
    else:
        start_button.config(state=normal)
        stop_button.config(state=disabled)
        if t == 0 and running[0]:
            messagebox.showinfo("end", "your time is end...")


def stop_timer():
    running[0] = True
    start_button.config(state="disabled")
    stop_button.config(state="normal")




root = Tk.Tk()
root.title("Count Down")
root.geometry("350x220")
Tk.Label(root, text="enter your text in S : ", font=("Courier", 24)).pack(pady=10)

entry_time = Tk.Entry(root, font=("Courier", 24), width=10)
entry_time.pack(pady=10)

btn_frame = Tk.Frame(root)
btn_frame.pack(pady=10)

start_button = Tk.Button(
    btn_frame, text="start", width=10, command=start_timer, bg="#ffffff", fg="white"
)
start_button.grid(row=0, column=0, padx=5)


stop_button = Tk.Button(
    btn_frame,
    text="start",
    width=10,
    command=start_timer,
    state="disabled",
    bg="#ffffff",
    fg="white",
)
stop_button.grid(row=0, column=1, padx=5)


timer_display = Tk.Label(root, text="00:00", font=("Courier", 24), fg="white")
running = [True]


root.mainloop()
