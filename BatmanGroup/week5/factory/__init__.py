from flask import Flask

from getinfo.getinfo import bpinfo
from moddata.moddata import bpmod
from factory.config import runtime_config


def run_app():
    app = Flask(__name__)
    app.config.from_object(runtime_config())
    app.register_blueprint(bpinfo)
    app.register_blueprint(bpmod)

    return app
