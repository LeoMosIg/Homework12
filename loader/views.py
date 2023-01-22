from os import abort

from flask import Blueprint, request, render_template
from functions import load_json_data, save_picture, add_post
from config import POST_PATH
from exceptions import WrongImgType
import logging

loader_blueprints = Blueprint("loader_blueprints", __name__, template_folder="templates")
logging.basicConfig(filename="logger.log", level=logging.INFO)

"""Вьюшка страницы созданного поста и вьюшка страницы создания поста"""


@loader_blueprints.route("/post", methods=["GET"])
def create_new_post_page():
    return render_template("post_form.html")


@loader_blueprints.route("/post", methods=["POST"])
def create_new_post_by_user():
    picture = request.files.get("picture")
    content = request.form.get("content")
    if not picture or not content:
        logging.info("Данные не загружены, отсутствует часть данных")
        return "Отсутствует часть данных"

    posts = load_json_data(POST_PATH)

    """Обработка ошибок"""
    try:
        new_post = {"pic": save_picture(picture), "content": content}
    except WrongImgType:
        abort(400)

    add_post(posts, new_post)
    return render_template("post_uploaded.html", new_post=new_post)
