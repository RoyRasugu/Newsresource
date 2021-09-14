class Article:
    '''
    Article class todefine Article Objects
    '''

    def __init__(self,name,author,title,urlToImage,description,publisedAt,content,url):
        self.name = name
        self.author = author
        self.title = title
        self.urlToImage = urlToImage
        self.description = description
        self.publishedAt = publisedAt
        self.content = content
        self.url = url

class Newsource:
    '''
    Newsource class to define Newsource Objects
    '''

    def __init__(self,name,description,category,url,id):
        self.name = name
        self.description = description
        self.category = category
        self.url = url
        self.id = id
        