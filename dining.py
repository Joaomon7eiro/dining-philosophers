from flask import Flask, render_template

import dining_philosophers

app = Flask(__name__)
app.config['DEBUG'] = False

@app.route('/')
def dining():
    actions = dining_philosophers.main()
    return render_template('dining.html', actions=actions)


if __name__ == '__main__':
    app.run(use_reloader=False)