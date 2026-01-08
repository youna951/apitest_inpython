# app.py
# 가장 심플한 파이썬 API 서버 (Flask)
# 실행하면: http://localhost:5000/ 로 접속 시 "Hello, World!" 반환

from flask import Flask

app = Flask(__name__)

@app.get("/")
def hello():
    return "Hello, World!"

if __name__ == "__main__":
    # host=0.0.0.0 : 외부(다른 PC/컨테이너)에서도 접근 가능하게 열고 싶을 때
    # 로컬에서만이면 기본값(127.0.0.1) 써도 됨
    app.run(host="0.0.0.0", port=5000, debug=True)
