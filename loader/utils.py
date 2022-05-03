import json

from config import UPLOAD_FOLDER, POST_PATH
from exceptions import WrongImgType


def save_picture(picture):
    """Сохраняет картинку если формат из списка allowed_type, иначе вызывает ошибку WrongImgType"""
    allowed_type = ["jpg", "png", "gif", "jpeg"]
    picture_type = picture.filename.split(".")[-1]
    if picture_type not in allowed_type:
        raise WrongImgType(f"Формат изображения не поддерживается. Допустимы только {', '.join(allowed_type)}!")
    picture_path = f"{UPLOAD_FOLDER}/{picture.filename}"
    picture.save(picture_path)

    return picture_path


def add_post(post_list, post):
    """функция добавления поста с записью в json файл"""
    post_list.append(post)
    with open(POST_PATH, "w", encoding="utf-8") as file:
        json.dump(post_list, file)
