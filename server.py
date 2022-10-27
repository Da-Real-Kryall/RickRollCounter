import flask, os

app = flask.Flask(__name__)

port=1234
host="0.0.0.0"

@app.route('/')
def index():
    return flask.send_file('index.html')

@app.route('/tally')
def add_to_tally():
    with open('static/media/tally.txt', 'r') as f:
        tally = int(f.read())
    with open('static/media/tally.txt', 'w') as f:
        f.write(str(tally + 1))
    return flask.send_file('static/media/tally.txt')

app.run(host=host, port=port, debug=True)