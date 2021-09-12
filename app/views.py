from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    message = 'Hello World'
    return render_template('index.html',message = message)

@app.route('/articles/<int:source_id>')
def articles(source_id):

    '''
    View news articles page function that returns articles details page from respective news source
    '''
    return render_template('articles.html', id = source_id)