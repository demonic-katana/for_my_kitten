from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index() -> str:
    return render_template("base.html")


@app.route('/meow')
def meow() -> str:
    return render_template("base1.html")


@app.route('/yes_yes_yes')
def fn_yes() -> str:
    return render_template("yes.html")


if __name__ == '__main__':
    app.run()
