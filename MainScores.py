from flask import Flask, render_template
import os.path
from Utils import *
app = Flask(__name__, template_folder='./')

@app.route('/')
def score_server():
    if os.path.exists(SCORES_FILE_NAME):
        with open(SCORES_FILE_NAME, 'r') as f:
            return render_template('ScoreHTML.html', SCORE=f.read())
    else:
            return render_template('ErrorHTML.html', ERROR=BAD_RETURN_CODE)

if __name__ == '__main__':
    app.run(debug=True)