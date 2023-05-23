import click
from werkzeug.security import generate_password_hash

from blog.extensions import db


@click.command("init-db")
def init_db():
    from blog.models import User
    db.create_all()
    print("done!")
@click.command("create-users")
def create_users():

    from blog.models import User
    admin = User(username="admin",email="email@email.com",password=generate_password_hash("1"))
    james = User(username="james")
    db.session.add(admin)
    db.session.add(james)
    db.session.commit()
    print("done! created users:", admin, james)
@click.command("create_init_tags")
def create_init_tags():
    from blog.models.user import Tag
    with app.app_context():
        tags = ('flask', 'django', 'python', 'gb', 'sqlite')
        for item in tags:
            db.session.add(Tag(name=item))
        db.session.commit()
    click.echo(f'Created tags: {", ".join(tags)}')