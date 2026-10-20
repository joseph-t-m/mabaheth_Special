import tkinter as tk
from datetime import datetime
import pytz
import jdatetime


def Update_clock():
    local_time = datetime.now().astimezone()
    time_strftime = local_time.strftime("%H:%M:%S")

    jalali_date = jdatetime.date.fromgregorian(date=local_time.date())

    weekdays = ["دوشنبه", "سه‌شنبه", "چهارشنبه", "پنج‌شنبه", "جمعه", "شنبه", "یک‌شنبه"]

    weekday_name = weekdays[local_time.weekday()]

    date_str = (
        f"{weekday_name} "
        f"{jalali_date.year}/{jalali_date.month:02d}/{jalali_date.day:02d}"
    )

    london_time = datetime.now(pytz.timezone("Europe/London"))

    hour = london_time.hour

    if 6 <= hour < 18:
        color = "darkblue"
        bg_color = "lightblue"
    else:
        color = "darkred"
        bg_color = "lightgray"

    root.config(bg=bg_color)
    label_title.config(fg=color, bg=bg_color)

    label_local.config(text=f"ساعت محلی: {time_strftime}", fg=color, bg=bg_color)

    label_london.config(
        text=f"ساعت لندن: {london_time.strftime('%H:%M:%S')}", fg=color, bg=bg_color
    )

    label_date.config(text=date_str, fg=color, bg=bg_color)

    root.after(1000, Update_clock)


# ساخت پنجره اصلی
root = tk.Tk()
root.title("ساعت محلی و لندن")
root.geometry("450x300")

# ساخت لیبل‌ها
label_title = tk.Label(root, text="ساعت جهانی", font=("Tahoma", 20, "bold"))
label_title.pack(pady=20)

label_local = tk.Label(root, font=("Tahoma", 15))
label_local.pack(pady=10)

label_london = tk.Label(root, font=("Tahoma", 15))
label_london.pack(pady=10)

label_date = tk.Label(root, font=("Tahoma", 13))
label_date.pack(pady=10)

# شروع بروزرسانی ساعت
Update_clock()

# باز نگه داشتن پنجره
root.mainloop()
