#s24004
#1秒ごとに自動更新する時計アプリ


import datetime     #時間
import tkinter as tk#ウィンドウ


def update_time():#時計の更新
    now = datetime.datetime.now()
    current_time = now.strftime("%Y年%m月%d日 %H時%M分%S秒")
    
    lbl.config(text=current_time)
    root.after(1000, update_time)#自分自身を呼び出してループ


root = tk.Tk()#ウィンドウを作成

root.title("時計アプリ")

lbl = tk.Label()
lbl.config(text="", font=("Helvetica", 20))
lbl.pack()


update_time()#関数呼び出し

root.mainloop()
