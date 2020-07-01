# coding: utf-8

import db_do
from config import config

def upload_insert_sql(content, letters):
    sql = ("INSERT INTO ocr_content VALUES (NULL, '{0}', '{1}');").format(content, letters) 
    try:
        with db_do.DB(config.db_path) as my_db:
            if my_db.insert(sql):
                return True, ""
            else:
                return False, "sql insert error."
    except Exception as ex:
        return False, str(ex)
