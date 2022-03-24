from flask import Flask
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, jsonify
)
from sqlalchemy import text
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
import os


app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": r"*"}})

app.config['SQLALCHEMY_DATABASE_URI'] = str(os.environ.get("DB_CONNECTION"))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class PostsModel(db.Model):
    tablename = 'posts'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String())
    text = db.Column(db.String())

    def init(self, title, text):
        self.title = title
        self.text = text

    def repr(self):
        return f"<Post {self.title, self.text}>"


@app.route('/post', methods=['POST'])
def add_post():
    data = request.get_json()
    if data is not None:
        new_post = PostsModel(title=data['title'], text=data['text'])
        db.session.add(new_post)
        db.session.commit()
        return {"message": "Post append"}
    else:
        return {"message": "Post error"}


@app.route('/count_posts', methods=['GET'])
def get_posts_num():
    return jsonify({'database_size': len(PostsModel.query.all())})


if __name__ == '__app__':
    app.run(debug=True)

