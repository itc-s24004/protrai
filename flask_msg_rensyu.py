#s24004
#flaskを使ったメッセージアプリ

from flask import Flask, render_template, request, redirect
import datetime


app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html")


@app.route("/himitsu")
def himitsu():
  return "<small>秘密のページ</small>"


@app.route("/msg")
def msg():
  return render_template("msg.html")

@app.route("/submit", methods=["POST"])
def submit():
  #フォームから入力された内容を取得
  content = request.form["content"]
  with open("data.txt", "a") as file:
    file.write(f"\n{datetime.datetime.now()}\n{content}\n")
    return '書き込みました<br><a href="/msg">戻る</a>'

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000, debug=False)