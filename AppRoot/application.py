import tkinter as tk
import os , sys , subprocess 
from tkinter import messagebox

def open_tool (tool_name):
    try :
        if sys.platform.startswith('win') :
            os.system(f'start pythonw {tool_name}')
        else : 
            subprocess.Popen(['python3', tool_name])
    except Exception as e: 
        messagebox.showerror("Error :",f"Cant open tool name : {tool_name} \n {e} ")
root = tk.Tk()
root.title("Brn")
root.geometry("300x400")

tk.Label(root,text="Calac", width=20 , font=('Arial', 14, "bold")).pack(pady=20)

tk.Button(root,text="Calac", width=20 , command=lambda : open_tool("calculator.py")).pack(pady=10)
tk.Button(root,text="Paas", width=20 , command=lambda : open_tool("Password.py")).pack(pady=10)
tk.Button(root,text="Clock", width=20 , command=lambda : open_tool("world_clock.py")).pack(pady=10)
tk.Button(root,text="Count", width=20 , command=lambda : open_tool("countdown.py")).pack(pady=10)

tk.Button(root,text="Exit", width=20,fg="red",command=root.destroy).pack(pady=30)

root.mainloop()