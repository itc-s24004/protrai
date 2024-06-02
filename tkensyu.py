# GUIで動くアプリを作ってみるよ

import tkinter as tk #まずこの行を書く必要があるよ


root = tk.Tk() # 初めのおまじない


root.geometry("600x400") #ウィンドウのサイズ
root.title("ハローアプリ") # ウィンドウのタイトル

lbl = tk.Label(text="こんにちは世界") # いつもの
lbl.pack() # lblを配置させる必要がある





root.mainloop() # 終わりのおまじない
