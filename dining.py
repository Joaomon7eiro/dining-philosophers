from flask import Flask, render_template
from flask import request

import dining_philosophers

app = Flask(__name__)

#@app.route("/")
#def index():
#    return render_template('index.html')

@app.route('/')
def dining():
    actions = dining_philosophers.main()
    return render_template('dining.html', actions=actions)

if __name__ == '__main__':
    app.run()