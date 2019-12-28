from typing import Any, Union
from django.db import connection


def get_user_code(ch):
    cursor = connection.cursor()
    cursor.execute("select max(right(code,5)) from user_user where left(name,1)=%s", ch)
    row = cursor.fetchone()
    if type(row[0]) == str and row[0] != '':
        row = int(row[0]) + 1
    else:
        row = 10000
    row = str(row)
    row = 'W' + ch + row
    print(row)
    return row
