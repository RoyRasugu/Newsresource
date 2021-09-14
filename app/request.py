from os import name
import urllib.request,json
from .models import Article
from .models import Newsource

# Getting the api key
api_key = None

# Fetching the news base url
base_url = None

articles_url = None

top_url = None

def configure_request(app):
    global api_key,base_url,articles_url,top_url
    api_key = 'd4982de8e9614a69bc94ba80d1d573d9'
    base_url = app.config['NEWS_API_BASE_URL']
    articles_url = app.config['NEWS_ARTICLES_API']
    top_url = app.config['TOP_URL']

def get_newsSource(category):
    '''
    Function that gets the json response to our url
    '''
    get_source_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_source_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)

        newsSource_results = None

        if get_source_response['sources']:
            newsSource_list = get_source_response['sources']
            newsSource_results = process_sources(newsSource_list)

    return newsSource_results

def process_sources(source_list):
    '''
    Function that processes the news source result and transform them to a list of Objects

    Args:
        source_list: A list of dictionaries that contain news source details

    Returns:
        source_results: A list of news source objects
    '''
    newsSource_results = []
    for newsource_item in source_list:
        name = newsource_item.get('name')
        description = newsource_item.get('description')
        category = newsource_item.get('category')
        url = newsource_item.get('url')
        id = newsource_item.get('id')

        source_object = Newsource(name,description,category,url,id)
        newsSource_results.append(source_object)

    return newsSource_results

def get_article(id):
    '''
    Function that gets the json response to our url request
    '''
    get_srcArticles_url = articles_url.format(id,api_key)

    with urllib.request.urlopen(get_srcArticles_url) as url:
        articles_data = url.read()
        articles_response = json.loads(articles_data)

        artilces_list = None 

        if articles_response['articles']:
            artilces_list = articles_response['articles']
            articles_results = process_articles(artilces_list)
            
        return articles_results

def process_articles(articleList):
    '''
    Function that processes the movie result and transform them to a list of Objects

    Args:
        articleList: A list of dictionaries that contain article details

    Returns:
        article_results: A list of article objects
    '''
    articles_results = []
    for article_item in articleList:
        name = article_item.get('name')
        author = article_item.get('author')
        title = article_item.get('title')
        urlToImage = article_item.get('urlToImage')
        description = article_item.get('description')
        publishedAt = article_item.get('publishedAt')
        content = article_item.get('content')
        url = article_item.get('url')

        article_object = Article(name,author,title,urlToImage,description,publishedAt,content,url)
        articles_results.append(article_object)

    return articles_results

def top_head(category):
    get_top_url = top_url.format(category,api_key)

    with urllib.request.urlopen(get_top_url) as url:
        top_heads_data = url.read()
        top_heads_response = json.loads(top_heads_data)

        top_lists = None

        if top_heads_response['articles']:
            top_lists = top_heads_response['articles']
            top_headlines = process_articles(top_lists)

        return top_headlines
