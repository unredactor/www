from flask import request
from flask import render_template
from app import app

from constants import context
from nlp import sort_words


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', **context)


@app.route('/about')
def about():
    return render_template('about.html', **context)


@app.route('/unredact')
def unredact():
    text = request.args.get('text')
    unredacted_text = sort_words(text)
    return render_template('unredacted_text.json', text=text, unredacted_text=unredacted_text)
