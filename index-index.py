import math
import tkinter as tk
i = 0
value = {
    "k1" : 0,
    "k2" : 0,
    "k3" : 0,
    "k4" : 0,
    "k5" : 0,
    "k6" : 0,
    "k7" : 0,
    "k8" : 0,
    "k9" : 0,
    "k10" : 0,
    "k11" : 0,
    "k12" : 0,
    "k13" : 0,
    "k14" : 0,
    "k15" : 0
}
def calculate():
    global i
    i = i+1
    label_result2.config(text=f"횟수 : {i}")
    ipsa_1_val = float(entry_ipsa_1.get())
    ipsa_2_val = float(entry_ipsa_2.get())
    result = f(ipsa_1_val, ipsa_2_val)
    label_result.config(text=f"p = {result}")
    print(f"{i}번째 계산값 : {result}")
    print(f"{i}번째 반지름 : {ipsa_1_val}")
    if i == 1:
        value["k1"] = result
    elif i == 2:
        value["k2"] = result
    elif i == 3:
        value["k3"] = result
    elif i == 4:
        value["k4"] = result
    elif i == 5:
        value["k5"] = result
    elif i == 6:
        value["k6"] = result
    elif i == 7:
        value["k7"] = result
    elif i == 8:
        value["k8"] = result
    elif i == 9:
        value["k9"] = result
    elif i == 10:
        value["k10"] = result
    elif i == 11:
        value["k11"] = result
    elif i == 12:
        value["k12"] = result
    elif i == 13:
        value["k13"] = result
    elif i == 14:
        value["k14"] = result
    elif i == 15:
        value["k15"] = result
def f(x, y):
    p = (((x**2+4*y**2)**0.5)/x)
    return p
def pyunghyun():
    Val = value["k1"]+value["k2"]+value["k3"]+value["k4"]+value["k5"]+value["k6"]+value["k7"]+value["k8"]+value["k9"]+value["k10"]+value["k11"]+value["k12"]+value["k13"]+value["k14"]+value["k15"]
    return Val/15
def react():
    label_result.config(text=f"평균 계산값 : {pyunghyun()} (1~15)")
    print(f"평균값 : {pyunghyun()}")
root = tk.Tk()
label_ipsa_1 = tk.Label(root, text="원의 반지름 (mm)") #mm
label_ipsa_1.pack()
entry_ipsa_1 = tk.Entry(root)
entry_ipsa_1.pack()
label_ipsa_2 = tk.Label(root, text="시료의 두께 (mm)") #mm
label_ipsa_2.pack()
entry_ipsa_2 = tk.Entry(root)
entry_ipsa_2.pack()
button_calculate = tk.Button(root, text="p 구하기", command=calculate)
button_calculate.pack()
label_result = tk.Label(root, text="")
label_result.pack()
label_result2 = tk.Label(root, text="")
label_result2.pack()
button_calculate = tk.Button(root, text="평균 구하기", command=react)
button_calculate.pack()
label_result3 = tk.Label(root, text="")
label_result3.pack()
if __name__=='__main__':
    root.mainloop();print("실행됨")