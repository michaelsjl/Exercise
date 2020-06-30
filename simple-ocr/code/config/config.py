# coding: utf-8

import os

root_path = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
db_path = os.path.join(root_path, 'db', 'ocr.db').replace(os.sep, '/')

is_debug = True
