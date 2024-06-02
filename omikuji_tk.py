# s24004
# ボタンでおみくじを引けるアプリ

# GUIで動くアプリを作ってみるよ

import tkinter as tk #まずこの行を書く必要があるよ
import omikuji


root = tk.Tk() # 初めのおまじない


root.geometry("600x400") #ウィンドウのサイズ
root.title("ハローアプリ") # ウィンドウのタイトル

def omi (ev):
    lbl = tk.Label(text=omikuji.getKuji()) # いつもの
    lbl.pack() # lblを配置させる必要がある
    

button = tk.Button(text="くじを引く", width=50)
button.bind("<Button-1>", omi) 
button.pack()




root.mainloop() # 終わりのおまじない
