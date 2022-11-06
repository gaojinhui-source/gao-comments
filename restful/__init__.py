from flask import Blueprint, session


route_comment = Blueprint("comment", __name__, template_folder="templates")
route_user = Blueprint("user", __name__, template_folder="templates")
route_v1 = Blueprint("v1", __name__, template_folder="templates")
