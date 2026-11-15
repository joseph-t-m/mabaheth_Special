import tkinter as tk
import string, random
from tkinter import ttk , messagebox
import PIL
SYMBOLS = "!()$#%^&*_-+="
MIN_LEN = 8


def check_strength(pw):
    return sum(
        [
            len(pw) >= MIN_LEN,
            any(ch.isupper() for ch in pw),
            any(ch.islower() for ch in pw),
            any(ch.isdigit() for ch in pw),
            any(ch in SYMBOLS for ch in pw),
        ]
    )


def generate_pw(Length=12):
    all_chars = string.ascii_letters + string.digits + SYMBOLS
    pw = "".join(random.choices(all_chars, k=Length))
    pw_label = pw
    return pw

def copy_clipboard():
    password = res_label.cget("text")
    if not password:
        messagebox.showwarning("warn", "there isnt had password!")
        return

    root.clipboard_clear()
    root.clipboard_append(password)
    messagebox.showinfo("Copied!", "Your pass was copied")

password = input("Enter your password: (My opinion click Enter)")

if password == "":
    password = generate_pw(12)
    # label_pass.config(password)

score = check_strength(password)
print(f"pass : {password} score : {score}/ 5")


print("nice its good pass" if score >= 3 else f"pass is weak. purpose {generate_pw(12)}")
# if score < 3:
#     print("pass is weak. purposed safer pass :")
#     print(generate_pw())
# else:
#     print("pass is comfortable!")


root = tk.Tk()
root.title("Pass Gen2")
root.geometry("290x300")

tk.Label(root, text="Enter your password: (My opinion click Enter)", font("Courier",24)).pack(pady=10)
entry_pass = tk.Entry(root, font=("Courier", 24), width=10)

pw_label = tk.Label(root, font=("Courier", 24))

tk.Label(root, label_pass)

# if password == "":
#     password = generate_pw(12)
#     print("purposed pass : ", password)
    
tk.Label(root,"nice its good pass")

root.mainloop()