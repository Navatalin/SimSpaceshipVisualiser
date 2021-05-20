from flask import render_template, Response
from app import rdb, r_dbcConnection
from app.main import bp

@bp.route('/streaming')
def streaming():
    def inner():
        try:
            rdb.connect("localhost", 49154).repl()
            cursor = rdb.db('test').table('Data').changes().run()
            for document in cursor:
                yield "data:" + str(document['new_val']).replace("'", '"') + "\n\n"
        except:
            pass
    return Response(inner(), status=200, mimetype='text/event-stream')


@bp.route('/', methods=['GET'])
@bp.route('/index', methods=['GET'])
def display_data():
    return render_template('live_data.html')
