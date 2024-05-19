import math as m
import tkinter as tk
def calculate():
    ipsa_1_val = float(entry_ipsa_1.get())
    ipsa_2_val = float(entry_ipsa_2.get())
    result = f(ipsa_1_val, ipsa_2_val)
    label_result.config(text=f"Result: {result}")
    with open("values.txt", "w") as file:
        file.write(f"ipsa_1: {ipsa_1_val}\n")
        file.write(f"ipsa_2: {ipsa_2_val}")
def f(x, y):
    p = -m.sin(x/m.pi) / m.sin(y/m.pi) # 호도법에 따라 n도 = n/pi
    return p
root = tk.Tk() # Tkinter 모델
label_ipsa_1 = tk.Label(root, text="진공에서의 입사각")
label_ipsa_1.pack()
entry_ipsa_1 = tk.Entry(root)
entry_ipsa_1.pack()
label_ipsa_2 = tk.Label(root, text="매질에서의 입사각")
label_ipsa_2.pack()
entry_ipsa_2 = tk.Entry(root)
entry_ipsa_2.pack()
button_calculate = tk.Button(root, text="굴절률 구하기", command=calculate)
button_calculate.pack()
label_result = tk.Label(root, text="")
label_result.pack()
if __name__=='__main__':
    root.mainloop();print("running..")
