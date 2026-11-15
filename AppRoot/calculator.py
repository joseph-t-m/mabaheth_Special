from tkinter import Tk
from tkinter import messagebox

root = Tk.Tk()
root.title("Calculator")
root.geometry("300x500")
root.resizazble(width=False, height=False)
entry = Tk.Entry(root, width=10, relief = "solid", justify="left")
Tk.Label(root, text="Enter your number", font=("Courier", 12)).pack(pady=5)


entry = Tk.Entry(root, width=20, font=(Arial, 12), borderwidth=3)
Entry.grid(row= 0, columnspan=4,padx=10,pady=20)
def calculator() :
          expertion = entry.get()
          try :
                    res = eval(expertion)
                    entry.delete(0, Tk.END)
                    entry.insert(0, Tk.END)

buttons = {
          ('7', 1 ,0),('8', 1, 1),('9', 1, 2), ('/', 1, 2),
          ('4', 2 ,0),('5', 2, 1),('6', 2, 3), ('')
          ('1', 3 ,0),('2', 3, 1),('3', 3, 2)
}
relif : {
          solid : 
}
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def power(x, y):
    return x**y


def divide(x, y):
    if y == 0:
        return "خطا: تقسیم بر صفر"
    return x / y


# dictionoty
ops = {"+": add, "-": subtract, "*": multiply, "^": power, "/": divide}

while True:
          a = int(input("عدد اول:"))
          op = input("عملگر:")
          b = int(input("عدد دوم:"))

          func = ops.get(op)
          if func:
                    print("نتیحه", func(a, b))
          else:
                    print("عملگر نامعتبر")

          cont = input("do you want continue? y/n").lower()
          if cont == 'n' :
                    print("bye! bye!")
                    break





cal.mainloop()