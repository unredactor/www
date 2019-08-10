from flask import render_template, flash, redirect, request, url_for
from app import app

from constants import context
from nlp import sort_words
from app.forms import UnredactForm
#from muellerbot import unredact
from unredactor_functions import unredact

# def sort_words(text):
#     return ' '.join(sorted(text.split()))


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', **context)


@app.route('/about')
def about():
    return render_template('about.html', **context)


@app.route('/api')
def api():
    text = request.args.get('text')
    unredacted_text = sort_words(text)
    return render_template('unredacted_text.json', text=text, unredacted_text=unredacted_text)

@app.route('/unredactor', methods=['GET', 'POST'])
def unredactor():
	form = UnredactForm()
	unredacted_text = ''

	#Depending on which module is imported, either the sort function (unredactor functions) or
	#the actual unredact function (muellerbot) runs	

	if form.validate_on_submit():
		unredacted_text = unredact(str(form.text.data))
	return render_template('unredact.html', title='Unredact', form=form, unredacted_text=unredacted_text)
