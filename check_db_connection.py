from fixture.orm import ORMFixture
from model.group import Group

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
try:
    l = db.get_contacts_not_in_groups(Group(id="356"))
    for item in l:
        print(item)
    print(len(l))
finally:
    pass # db.destroy()


'''
# pip install mysql-connector-python-rf из https://pypi.org/project/mysql-connector-python-rf/
# import mysql.connector
# Альтернативный драйвер pip install PyMySQL

import pymysql.cursors


connection = pymysql.connect(host="127.0.0.1", database="addressbook", user="root", password="")

try:
    cursor = connection.cursor()
    cursor.execute("select * from group_list")
    # Fetchall возвращает всю инфу в виде набора строк
    for row in cursor.fetchall():
        print(row)

finally:
    connection.close()
'''
