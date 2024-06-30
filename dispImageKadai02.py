#s24004
#画像を　白黒/回転/水平反転/300x300リサイズ　処理する

import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image, PIL.ImageTk

def dispPhoto(path):
    newImage = PIL.Image.open(path).convert("L").rotate(90).transpose(PIL.Image.FLIP_LEFT_RIGHT).resize((300, 300))
    imageData = PIL.ImageTk.PhotoImage(newImage)
    imageLabel.configure(image = imageData)
    imageLabel.image = imageData

def openFile():
    fpath = fd.askopenfilename()
    if fpath:
        dispPhoto(fpath)
        print(fpath)
        lbl.config(text=f"{fpath} \n が開かれています")

root = tk.Tk()
root.title("画像ビューアー")
root.geometry("550x450")

lblTitle = tk.Label(text="🎨画像表示アプリ バージョン2.0🎨", font=("Helvetica", 25))
lblTitle.pack()


btn = tk.Button(text="ファイルを開く", command = openFile)
imageLabel = tk.Label()
lbl = tk.Label(text="画像が開かれていません", font=("Helvetica", 15))

btn.pack()
imageLabel.pack()
lbl.pack()

tk.mainloop()
