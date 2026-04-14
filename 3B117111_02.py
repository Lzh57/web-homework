from flask import Flask

app = Flask(__name__)

# 1. 路由：首頁
@app.route("/")
def index():
    return "<h1>歡迎來到 Flask!</h1>"

# 2. 路由：動態問候語
@app.route("/hello/<name>")
def hello_user(name):
    return f"<h1>Hello, {name}!</h1>"

# 3. 路由：計算民國年與年齡
# 使用 <int:year> 轉換器，將網址內容自動轉為整數
@app.route("/birth/<int:year>")
def calculate_age(year):
    # 計算民國年：西元年 - 1911
    roc_year = year - 1911
    # 計算年齡：2026 - 西元年
    age = 2026 - year
    
    return f"<p>您是民國 {roc_year} 年出生，今年 {age} 歲</p>"

if __name__ == "__main__":
    # 啟動應用程式，開啟 debug 模式方便修改後自動重啟
    app.run(debug=True)