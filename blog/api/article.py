from flask_combo_jsonapi import ResourceList, ResourceDetail

from blog.models.database import db
from blog.models.user import Article
from blog.schemas import ArticleSchema
from combojsonapi.event.resource import EventsResource


class ArticleListEvent(EventsResource):

    def event_get_count(self, *args, **kwargs):
        return {'count': Article.query.count()}


class ArticleList(ResourceList):
    events = ArticleListEvent
    schema = ArticleSchema
    data_layer = {
        'session': db.session,
        'model': Article,
    }


class ArticleDetail(ResourceDetail):
    schema = ArticleSchema
    data_layer = {
        'session': db.session,
        'model': Article,
    }
