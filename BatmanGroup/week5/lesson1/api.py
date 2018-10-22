import json

from flask import request, jsonify, Flask
from flask.views import MethodView

app = Flask(__name__)

db = {
        "Rooney": {"Full_name": "Wayne Mark Rooney", "Age": "32", "Club": "DC"},
        "Ibrahimovic": {"Full_name": "Zlatan Ibrahimovic", "Age": "37", "Club": "LA Galaxy"},
        "Messi": {"Full_name": "Lionel Messi", "Age": "31", "Club": "Barcelona"},
     }


class Footballers(MethodView):
    def get(self):
        args = request.args
        if not args:
            return jsonify(db)
        else:
            return jsonify(db.get(args.get("surname")))

    def post(self):
        data = dict(request.data)
        for key, value in data.items():
            db[key] = value
        return jsonify(db)

    def delete(self):
        data = request.data
        return data

# {
# 	"Salah":
# 		{"Full_name": "Mohamed Salah Ghaly",
# 		"Age": "26",
# 		"Club": "Liverpool"}
# }

app.add_url_rule('/footballers', view_func=Footballers.as_view('footballers'))


if __name__ == '__main__':
    app.run()
