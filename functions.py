import json

from config import *
from exceptions import *

"""Чтение данных из json"""


def load_json_data(path):
    try:
        with open(path, 'r', encoding='UTF-8') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return DataJsonError


"""Функция поиска"""


def search_posts_by_substring(posts, substring):
    posts_founded = []
    for post in posts:
        if substring.lower() in post["content"].lower():
            posts_founded.append(post)
    return posts_founded


"""Сохранение картинки в uploads"""


def save_picture(picture):
    allowed_type = ["jpg", "png", "gif", "jpeg"]
    picture_type = picture.filename.split(".")[-1]
    if picture_type not in allowed_type:
        raise WrongImgType(f"Неверный формат файла! Допустимы только {','.join(allowed_type)}")
    picture_path = f"{UPLOAD_FOLDER}/{picture.filename}"
    picture.save(picture_path)
    return picture_path


"""Запись данных в json"""


def add_post(post_list, post):
    post_list.append(post)
    with open(POST_PATH, "w", encoding="UTF-8") as file:
        json.dump(post_list, file)
