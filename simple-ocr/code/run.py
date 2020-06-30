# coding:utf-8

"""
Simple OCR Letters

Write a web service which can take an uploaded image(jpg, png) and find any letters in it.

The result will be returned to user as JSON :

{"content": [ 'Letter1', 'Letter2'...]}
This result will also be saved to database for future use.

Requirements:
Design your own data model and API
Use any Python/Golang frameworks or libraries as needed
Should include tests and documentations
"""

import os
import json
import sqlite3
from flask import Flask, jsonify, request, make_response
from model.ocr import ocr_do
from config import config
from db import db_do
app = Flask(__name__)


def upload_insert_sql(content, letters):
    sql = ("INSERT INTO ocr_content VALUES (NULL, '{0}', '{1}');").format(content, letters) 
    try:
        with db_do.DB(config.db_path) as my_db:
            if my_db.insert(sql):
                return True
            else:
                return False
    except Exception as e:
        app.logger.error(e)
        return False


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/analysis-image-letters', methods=['POST'])
def ocr_analysis():
    if request.method == 'POST':
        f = request.files['image_file']
        # f.save('D:/Debug/simple-ocr/test/' + secure_filename(f.filename))
        content = ocr_do.get_content_from_image(f)
        letters_dict = ocr_do.analysis_content_to_json(content)
        res = upload_insert_sql(letters_dict.keys()[0], json.dumps(letters_dict))
        if res:
            return "insert sql err.", "500"
        return jsonify(letters_dict)


if __name__ == '__main__':
    app.debug = config.is_debug
    app.run()
