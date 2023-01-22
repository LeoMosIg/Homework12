from flask import Blueprint, request, render_template
from functions import load_json_data, search_posts_by_substring
from config import POST_PATH
from exceptions import *
import logging

main_blueprints = Blueprint("main_blueprints", __name__, template_folder="templates")

logging.basicConfig(filename="logger.log", level=logging.INFO)

"""Вьюшки главной страницы и страницы поиска"""


@main_blueprints.route("/")
def main_page():
    logging.info("Открытие главной страницы")
    return render_template("index.html")


@main_blueprints.route("/search")
def search_page():
    s = request.args.get("s", "")
    logging.info("Выполняеться поиск")
    try:
        posts = load_json_data(POST_PATH)
    except DataJsonError:
        return "Проблема открытия файла постов"
    filtered_posts = search_posts_by_substring(posts, s)
    return render_template("post_list.html", posts=filtered_posts, s=s)
