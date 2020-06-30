# coding:utf-8

import re
import pytesseract
from PIL import Image


def get_content_from_image(image_path):
    try:
        image = Image.open(image_path)
        content = pytesseract.image_to_string(image, lang="eng")
    except Exception,ex:
        return ""
    
    return content


def analysis_content_to_json(content):
    regex_start = re.compile("[a-zA-Z]")
    letters = regex_start.findall(content)
    return {content: letters}
