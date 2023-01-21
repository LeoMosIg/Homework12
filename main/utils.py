import json


def load_json_data(path):
    with open(path, 'r', encoding='UTF-8') as file:
        return json.load(file)


def search_posts_by_substring(posts, substring):
    posts_founded = []
    for post in posts:
        if substring.lower() in post["content"].lower():
            posts_founded.append(post)
    return posts_founded

