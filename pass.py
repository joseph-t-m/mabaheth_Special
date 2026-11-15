import tkinter as tk
import string
import random

SYMBOLS = "!()$#%^&*_-+="
MIN_LEN = 8

def check_strength(pw):
          score = 0
          if len(pw) >= MIN_LEN:
                    score +=  1
          if any(ch.isupper() for ch in pw):
                    score +=  1
          if any(ch.islower() for ch in pw):
                    score +=  1
          if any(ch.isdigit() for ch in pw):
                    score +=  1
          if any(ch in SYMBOLS for ch in pw):
                    score +=  1
          return score

def generate_pw(Length=12) :
          all_chars = string.ascii_letters + string.digits + SYMBOLS
          pw = "".join(random.choice(all_chars) for _ in range(Length))
          return pw

password = input("Enter your (برای تولید پیشنهادی با Enter)")

if password == "" : 
          password = generate_pw(12)
          print("purposed pass : ", password)

score = check_strength(password)
print("pass score : ", score, "/ 5")

if score < 3:
          print("pass is weak. purposed safer pass :")
          print(generate_pw())
else:
          print("pass is comfortable!")
