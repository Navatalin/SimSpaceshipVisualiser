from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment
import rethinkdb

bootstrap = Bootstrap()
moment = Moment()
rdb = rethinkdb.RethinkDB()
r_dbcConnection = None

def create_app():
    app = Flask(__name__)

    bootstrap.init_app(app)
    moment.init_app(app)

    r_dbcConnection = rdb.connect(host='localhost', port=49154)

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    return app