from apiflask import APIBlueprint

from app.api.v1.api import api


def create_v1():
    bp_v1 = APIBlueprint('v1', __name__)
    bp_v1.register_blueprint(api, url_prefix='/api')
    return bp_v1







