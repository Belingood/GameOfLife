from flask import Flask, render_template, request
from game_of_life import GameOfLife


app = Flask(__name__)


@app.route('/', methods=['get', 'post'])
def index():
    if request.method == 'POST':
        vert = int(request.form.get('vert'))
        horiz = int(request.form.get('horiz'))
    else:
        vert = 25
        horiz = 30
    GameOfLife(horiz, vert)
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

