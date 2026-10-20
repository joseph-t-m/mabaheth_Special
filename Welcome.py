import tkinter as Tk

def DF() :
        root.destroy()
        
root = Tk.Tk()
root.title = ("Welcome")
root.geometry("320x400")
root.resizable(False,False)

Tk.Label(root, text="Welcome").pack(pady=10)
Tk.Button(root, text="exit", command=lambda:DF()).pack(pady=10)

root.mainloop()