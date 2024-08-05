#s24004
#Flaskの練習

#事前にFlaskモジュールをインストールすると使える
from flask import Flask, render_template

#Flaskライブラリをインスタンス化し、app変数に割り当て
#そのさい、コンストラクタへの引数は実行中のモジュールを指定する
app = Flask(__name__)

#ルートURLに対するリクエストを処理する関数を定義するデコレーター
#引数にルート'/'を指定するとアクセスした際index()関数が呼び出される
@app.route("/")
def index():
  return render_template("index.html")


@app.route("/himitsu")
def himitsu():
  return '''
<h1>秘密のページ</h1>
<a href="/">ホームに戻る</a>
'''

if __name__ == "__main__":
  app.run(host="0.0.0.0",port=5000,debug=True)

