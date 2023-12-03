from flask import Flask, render_template

# Создание сайта
app = Flask(__name__)

@app.route("/")
def page_index():
    return render_template("index.html")

# Запуск сайта
if __name__ == '__main__':
    app.run()

