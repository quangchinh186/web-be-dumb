from dao.ArticleDAO import ArticleDAO
from dao.LikeDAO import LikeDAO
from Decorators import Singleton
from util.Error import Error

@Singleton
class ArticleService():
    def __init__(self) -> None:
        self.articleDAO = ArticleDAO()
        self.likeDAO = LikeDAO()

    def searchArticle(self, keyword):
        articles = []
        for item in self.articleDAO.searchArticlesByKeyword(keyword):
            articles.append(item.as_dict())
        return articles

    def getNewfeed(self):
        articles = []
        print('nf')
        for item in self.articleDAO.getArticles():
            print(item.as_dict())
            articles.append(item.as_dict())
        return articles

    def getArticleById(self, id):
        article = self.articleDAO.getArticleById(id)
        if article == None:
            return {'status': Error.NOT_FOUND_ERROR}
        return article.as_dict()

    def getUserArticles(self, userID):
        articles = []
        for item in self.articleDAO.getUserArticles(userID):
            articles.append(item.as_dict())
        return articles

    def getArticle(self, request):
        article_id = request.args.get('article_id')
        user_id = request.args.get('user_id')
        keyword = request.args.get('search')
        if user_id != None:
            return self.getUserArticles(user_id)
        if article_id != None:
            return self.getArticleById(article_id)
        if keyword != None:
            return self.searchArticle(keyword)
        return self.getNewfeed()

    def createArticle(self, request):
        formData = request.form
        self.articleDAO.createArticle(**formData)
        return {'status': 'finish create'}

    def updateArticle(self, request):  
        formData = request.form
        article = self.articleDAO.getArticleById(formData.get('article_id'))
        if article == None:
            return {'status': Error.NOT_FOUND_ERROR}
        self.articleDAO.updateArticle(article, **formData)
        return {'status': 'finish update'}

    def deleteArticle(self, request):
        article_id = request.args.get('article_id')
        article = self.articleDAO.getArticleById(article_id)
        if article == None:
            return {'status': Error.NOT_FOUND_ERROR}
        self.articleDAO.deleteArticle(article)
        return {'status': 'finish delete'}

    def likeArticle(self, request):
        formData = request.form
        self.likeDAO.create(**formData)
        return {'status': 'liked'}

    def unlikeArticle(self, request):
        article_id = request.args.get('article_id')
        user_id = request.args.get('user_id')
        like = self.likeDAO.get(user_id, article_id)
        self.likeDAO.delete(like)
        return {'status': 'unliked'}