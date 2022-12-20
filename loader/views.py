from json import JSONDecodeError
import logging
from flask import Blueprint, render_template, request
from loader.utils import save_picture
from functions import add_post
loader_blueprint = Blueprint("loader_blueprint", __name__, template_folder='templates')

@loader_blueprint.route("/post")
def post_page():
    return render_template("post_form.html")

@loader_blueprint.route("/post", methods=['POST'])
def add_post_page():
    picture = request.files.get("picture")
    content = request.form.get("content")
    if not picture or not content:
        return "Нет картинки или текста"
    if picture.filename.split(".")[-1] not in ["jpeg", "png"]:
        logging.error("Загруженный файл не картинка")
        return "Неверный файл"
    try:
        picture_path = "/" + save_picture(picture)
    except FileNotFoundError:
        logging.error("Файл не найден")
        return "Файл не найден"
    except JSONDecodeError:
        return "Не валидный файл"
    post = add_post({"pic": picture_path, "content": content})
    return render_template("post_uploaded.html", post=post)



