import tkinter as tk
from math import *
def void():
    return 1
win = tk.Tk()
win.geometry("400x400")
win.title("calculator")
canvas = tk.Canvas(win, width=200, height=200)
canvas.pack()
scale = tk.Scale(win, from_=100000, to=1, length=200, orient="horizontal")
scale.pack(pady=10)
btn = tk.Button(win, text="실행", command=void)
btn.pack()
result_label = tk.Label(win, text="")
result_label.pack()
percentage_label = tk.Label(win, text="")
percentage_label.pack()
btn2 = tk.Button(win, text="닫기", command=win.quit)
btn2.pack(pady=10)
# win 실행
win.mainloop()