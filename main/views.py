from flask import Blueprint, request, render_template
import logging
from main.utils import *
from config import POST_PATH


main_blueprints = Blueprint("main_blueprints", __name__, template_folder="templates")

logging.basicConfig(filename="logger.log", level=logging.INFO)


@main_blueprints.route("/")
def main_page():
    logging.info("Открытие главной страницы")
    return render_template("index.html")


@main_blueprints.route("/search")
def search_page():
    s = request.args.get("s", "")
    logging.info("Выполняеться поиск")
    posts = load_json_data(POST_PATH)
    filtered_posts = search_posts_by_substring(posts, s)
    return render_template("post_list.html", posts=filtered_posts, s=s)
