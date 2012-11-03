import os

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', methods=('GET',))
def tv():
    with open(os.environ['LOG_FILE'], 'r') as f:
        lines = [line.strip() for line in f.readlines()[-25:]]
        lines.reverse()
        return render_template('home.html', lines=lines)

if __name__ == '__main__':
    app.run(debug=True)

