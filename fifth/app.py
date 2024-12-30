from flask import Flask, render_template
import requests

app = Flask(__name__, template_folder='templates')

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/index')
def index():
    url = "https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5"
    response = requests.get(url)
    data = response.json()
    return render_template('index.html', data=data)

if __name__ == "__main__":
    app.run(debug=True, port=7050)