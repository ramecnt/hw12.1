import logging

from flask import Blueprint, render_template, request
from json import JSONDecodeError
from functions import get_by_word
main_blueprint = Blueprint("main_blueprint", __name__, template_folder='templates')

@main_blueprint.route("/")
def main_page():
    return render_template("index.html")

@main_blueprint.route("/search/")
def search_page():
    search_querry = request.args.get("s", "")
    logging.info("Выполняю поиск")
    try:
        posts = get_by_word(search_querry)
    except FileNotFoundError:
        logging.error("Файл не найден")
        return "Файл не найден"
    except JSONDecodeError:
        return "Не валидный файл"
    return render_template("post_list.html", search_querry=search_querry, posts=posts)


