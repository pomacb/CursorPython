from flask import Blueprint
from flask.views import MethodView
from flask import request, jsonify


class Footballers(MethodView):
    def get(self):
        from api import db
        args = request.args
        if not args:
            return jsonify(db)
        else:
            return jsonify(db.get(args.get("Surname")))


bpinfo = Blueprint('bpinfo', __name__)
bpinfo.add_url_rule('/getinfo', view_func=Footballers.as_view('bpinfo'))
