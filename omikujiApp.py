import tkinter as tk
import random

root = tk.Tk()
root.geometry("300x200")

kuji = ["大吉","中吉","小吉","凶"]

def getKuji():
    luck = random.choice(kuji)
    lbl.config(text=luck)


lbl = tk.Label(text="", font=("Helvetica", 30))
btn = tk.Button(text="くじを引く", font=("Helvetica", 15), command=getKuji)

lbl.pack()
btn.pack()
