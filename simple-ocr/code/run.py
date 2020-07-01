# coding:utf-8

"""
Author: Michael Shu
Created: 2020-06-30
Note:

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
from flask import Flask, jsonify, request
from model.ocr import ocr_do
from config import config
from db.affair_db import upload_insert_sql

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


def response_data(success=True, message="success", body=None):
    response_dict = {"success": success,
                    "message": message,
                    "body": body}
    return jsonify(response_dict)


@app.route('/simple-ocr/v1/image-letters', methods=['POST'])
def ocr_analysis():
    if request.method == 'POST':
        f = request.files['image_file']
        res, content = ocr_do.get_content_from_image(f)
        if not res:
            return (response_data(False, "ocr analysis image err, reason: {0}.".format(content)), "500")
        if content is None or content == "":
            return (response_data(False, "content is Null."), "500")

        res, letters_dict = ocr_do.analysis_content_to_json(content)
        if not res:
            return (response_data(False, "analysis content err, reason: {0}.".format(letters_dict)), "500")

        res, reason = upload_insert_sql(letters_dict.keys()[0], json.dumps(letters_dict))
        if not res:
            return (response_data(False, "save to database err, reason: {0}.".format(reason)), "500")

        return response_data(body=letters_dict)
    else:
        return (response_data(False, "server only support POST."), "405")


if __name__ == '__main__':
    app.debug = config.is_debug
    app.run()
