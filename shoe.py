from flask import Flask

app = Flask(__name__)

@app.route('/index.html')
def index():
    return '<p>we are here</p>'

@app.route('/')
def hey_shoo_viewer():
    return 'shooooo ree vyu'

if __name__ == '__main__':
    app.run()