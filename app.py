import os
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask import render_template

BASEDIR = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASEDIR, 'sqlite.db')

DB_URL = 'postgresql+psycopg2://apsl:1234@127.0.0.1:5432/flask1'
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)


@app.route('/')
@app.route('/home')
def hello_world():
    users = User.query.all()
    return render_template("home.html", users=users)


@app.route("/user/<int:user_id>")
def user_detail(user_id):
    user = User.query.get_or_404(user_id)
    return render_template("detail.html", user=user)


if __name__ == '__main__':
    app.run()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    notes = db.Column(db.String(120), nullable=True)

    def __repr__(self):
        return 'User: {}-{}-{}'.format(
            self.id, self.username, self.email
        )

