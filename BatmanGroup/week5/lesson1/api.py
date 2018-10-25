from getinfo.getinfo import bpinfo
from moddata.moddata import bpmod
from flask import Flask

app = Flask(__name__)

# db = {
#         "Rooney": {"Full_name": "Wayne Mark Rooney", "Age": "32", "Club": "DC"},
#         "Ibrahimovic": {"Full_name": "Zlatan Ibrahimovic", "Age": "37", "Club": "LA Galaxy"},
#         "Messi": {"Full_name": "Lionel Messi", "Age": "31", "Club": "Barcelona"},
#      }

app.register_blueprint(bpinfo)
app.register_blueprint(bpmod)

if __name__ == '__main__':
    app.run()
