from blog.app import create_app
from blog.models.database import db
from werkzeug.security import generate_password_hash
app=create_app()

if __name__ == "__main__":
    app = create_app()

    app.run(
        host="0.0.0.0",
        # port=8001,
        debug=True
    )
@app.cli.command("init-db")
def init_db():

    db.create_all()
    print("done!")
@app.cli.command("create-users")
def create_users():

    from blog.models import User
    admin = User(username="admin",email="email@email.com",password=generate_password_hash("1"))
    james = User(username="james")
    db.session.add(admin)
    db.session.add(james)
    db.session.commit()
    print("done! created users:", admin, james)
