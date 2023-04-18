from werkzeug.exceptions import NotFound
from flask import Blueprint
from flask import render_template, redirect

from blog.user.views import get_user_name

article = Blueprint('article', __name__, url_prefix='/articles', static_folder='../static')
ARTICLES = {
    1: {'title': 'first title', 'text': 'first text first text', 'author': 1},
    2: {'title': 'second title', 'text': 'second text second text', 'author': 2},
    3: {'title': 'third title', 'text': 'third text third text', 'author': 3}}


@article.route('/')
def article_list():
    return render_template('articles/list.html', articles=ARTICLES)


@article.route('/<int:pk>')
def get_article(pk: int):
    try:
        article = ARTICLES[pk]
    except KeyError:
        raise NotFound(f'User id {pk} not found')
    title = article["title"]
    text = article["text"]
    author =get_user_name(article["author"])

    return render_template('articles/details.html', article=article ,title=title,
        text=text,
        author=author)
