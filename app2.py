import tkinter as tk


def dispLabel():
    lbl.config(text="こんにちは")



root = tk.Tk()#ウィンドウ作成
root.geometry("200x100")#大きさを設定


lbl = tk.Label(text="LABEL")#ラベルを作成
btn = tk.Button(text="PUSH", command=dispLabel)#ボタンを作成

#ウィンドウに配置▼
lbl.pack()
btn.pack()
#ウィンドウに配置▲



lbl2 = tk.Label(text="ラベル2", font=("Helvetica", 20)).pack()

btn2 = tk.Button(text="何もしないボタン", command=dispLabel,
                 font=("Helcetica", 20)).pack()



tk.mainloop()
