from flask import Flask, render_template, send_from_directory
from main.views import main_blueprints
from loader.views import loader_blueprints
import logging

app = Flask(__name__)

"""Регистрация blueprint"""
app.register_blueprint(main_blueprints)
app.register_blueprint(loader_blueprints)

"""Вьюшка ошибки при загрузке не того формата файла и специальная вьюшка для uploads"""


@app.errorhandler(400)
def bad_request_error(error):
    logging.info(error)
    return render_template("error_400.html", error=error)


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


if __name__ == "__main__":
    app.run()
