import json
from flask import Blueprint, render_template, request, abort
import logging
from main import utils
from config import POST_PATH
from loader.utils import *

loader_blueprint = Blueprint("loader_blueprint", __name__, template_folder="templates")
logging.basicConfig(filename="logger.log", level=logging.INFO)


@loader_blueprint.route("/post", methods=["GET"])
def make_new_post_page():
    return render_template("post_form.html")


@loader_blueprint.route("/post", methods=["POST"])
def make_new_post_by_user():
    picture = request.files.get("picture")
    content = request.form.get("content")
    if not picture or not content:
        logging.info("Данные не загружены, не хватает данных")
        return "Отсутсвует часть данных"

    posts = utils.load_json_file(POST_PATH)

    try:
        new_post = {"pic": save_picture(picture), "content": content}
    except WrongImgType:
        abort(400)

    add_post(posts, new_post)
    return render_template("post_uploaded.html", new_post=new_post)

