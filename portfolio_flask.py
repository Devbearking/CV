from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/CV-English.html')
def cv():
    return render_template('CV-English.html')

if __name__ == '__main__':
    app.run(debug=True)