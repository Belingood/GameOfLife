from flask import Flask, render_template
from game_of_life import GameOfLife


app = Flask(__name__)


@app.route('/')
def index():
    GameOfLife(30, 25)
    return render_template('index.html')


@app.route('/live')
def live():
    new_gener = GameOfLife()
    new_gen = new_gener.world
    gen_count = new_gener.counter
    new_gener.form_new_generation()
    return render_template('live.html',
                           new_gen = new_gen,
                           gen_count = gen_count)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

