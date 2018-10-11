from flask import Flask, render_template

import dining_philosophers as dp

app = Flask(__name__)
app.config['DEBUG'] = False

@app.route('/')
def dining():
    actions = dp.main()
    return render_template('dining.html', actions=actions)


if __name__ == '__main__':
    app.run(use_reloader=False)
