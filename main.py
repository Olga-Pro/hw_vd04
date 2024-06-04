# Задание 1
from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def cur_date_time():
    now = datetime.now()
    current_time = now.strftime("%d.%m.%Y %H:%M:%S")

    return f"<h1>Сейчас: {current_time} </h1>"

if __name__ == '__main__':
    app.run()