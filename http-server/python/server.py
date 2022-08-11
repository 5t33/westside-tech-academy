from flask import Flask

app = Flask(__name__)

@app.route('/hello-world')
def home():
    return "<h1>hello world</h1>"

@app.route('/goodbye-world')
def away():
    return "<h1>Goodbye world</h1>"

if __name__ == '__main__':
    app.run()