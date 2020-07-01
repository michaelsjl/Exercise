# coding:utf-8

import re
import pytesseract
from PIL import Image


def get_content_from_image(image_path):
    try:
        image = Image.open(image_path)
        content = pytesseract.image_to_string(image, lang="eng")
    except Exception as ex:
        return False, str(ex)
    
    return True, content


def analysis_content_to_json(content):
    try:
        regex_start = re.compile("[a-zA-Z]")
        letters = regex_start.findall(content)
        content = ''.join(letters)
    except Exception as ex:
        return False, str(ex)
    return True, {content: letters}
