from blog.models import user
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from blog.models.database import db

from blog.admin.views import CustomAdminView, ArticleAdminView, TagAdminView, UserAdminView, CustomAdminIndexView

admin = Admin(name="Blog Admin",  index_view=CustomAdminIndexView(),template_mode="bootstrap4")

admin.add_view(TagAdminView(user.Tag, db.session, category="Models"))
admin.add_view(ArticleAdminView(user.Article, db.session, category="Models"))
admin.add_view(UserAdminView(user.User, db.session, category="Models"))
