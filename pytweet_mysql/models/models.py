from pytweet_mysql.database import db


# EXERCISE: idとauthor_nameとbodyを持ったPytweetモデルを定義しましょう=================
# EXERCISE: Let's implement Pytweet which has id, author_name, body attributes ===
class Pytweet(db.Model):
    __tablename__ = 'pytweets'

    id = db.Column(db.Integer, primary_key=True)
    author_name = db.Column(db.Text)
    body = db.Column(db.Text)

    def __repr__(self):
        return '<Pytweet id={id} author_name={author_name!r}>'.format(
            id=self.id, author_name=self.author_name)

# ================================================================================


