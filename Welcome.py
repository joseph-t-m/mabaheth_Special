import tkinter as Tk

def DF() :
        root.destroy()
        
root = tk.Tk()
root.title = ("Welcome")
root.geometry("320x400")
root.resizable(False,False)

tk.Label(root, text="Welcome").pack(pady=10)
tk.Button(root, text="exit", command=lambda:DF()).pack(pady=10)

root.mainloop()