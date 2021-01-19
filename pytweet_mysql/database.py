from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()


# EXERCISE: DBの初期化処理と、マイグレーション処理を行う`init_db(app)`実装しましょう =============
# EXERCISE: Let's implement `init_db(app)` to init DB and migrate DB =============
def init_db(app):
    db.init_app(app)
    Migrate(app, db)
# ======================================================================

