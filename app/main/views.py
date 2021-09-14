from flask import render_template,url_for
from . import main
from ..request import get_newsSource,get_article,top_head

# Views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - News Source Article Finder'

    # Getting the news sources
    top_headline = top_head('business')
    news_sources = get_newsSource('sources')
    print(news_sources)

    return render_template('index.html',title = title, topHeads = top_headline, newSrc = news_sources)

@main.route('/articles/<source_id>')
def articles(source_id):
    '''
    View news articles page function that returns articles details page from respective news source
    '''
    articles = get_article(source_id)
    title = 'The News Articles'
    print(articles)

    return render_template('articles.html', title = title, articles = articles)