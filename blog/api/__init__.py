from blog.api.tag import TagList, TagDetail
from combojsonapi.spec import ApiSpecPlugin
from flask_combo_jsonapi import Api
from blog.api.article import ArticleDetail, ArticleList
from blog.api.author import AuthorDetail, AuthorList
from blog.api.user import UserDetail, UserList
from combojsonapi.event import EventPlugin
from combojsonapi.permission import PermissionPlugin



def create_api_spec_plugin(app):

    api_spec_plugin = ApiSpecPlugin(
        app=app,
        tags={
            "Tag": "Tag API",
            "Author": "Author API",
            "Article": "Article API",
            "User": "User API",
        }
    )
    return api_spec_plugin
def init_api(app):
    api = Api(app)
    event_plugin = EventPlugin()
    permission_plugin = PermissionPlugin(strict=False)
    api_spec_plugin = create_api_spec_plugin(app)
    api = Api(app=app, plugins=[api_spec_plugin, event_plugin, permission_plugin])
    # api = Api(app=app, plugins=[api_spec_plugin])
    api.route(TagList, "tag_list", "/api/tags/")
    api.route(TagDetail, "tag_detail", "/api/tags/<int:id>/")

    api.route(UserList, "user_list", "/api/users/", tag="User")
    api.route(UserDetail, "user_detail", "/api/users/<int:id>", tag="User")

    api.route(AuthorList, "author_list", "/api/authors/", tag="Author")
    api.route(AuthorDetail, "author_detail", "/api/authors/<int:id>", tag="Author")

    api.route(ArticleList, "article_list", "/api/articles/", tag="Article")
    api.route(ArticleDetail, "article_detail", "/api/articles/<int:id>", tag="Article")
    return api