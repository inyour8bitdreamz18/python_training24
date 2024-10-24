import pymysql.cursors
from model.group import Group
from model.contact import Contact


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        lst = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                # Возращается кортеж - tuple
                (id, name, header, footer) = row
                lst.append(Group(id=str(id), name=name, header=header, footer=footer))

        finally:
            cursor.close()
        return lst


    def get_contact_list(self):
        lst = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname from addressbook")  # where deprecated='NULL'
            for row in cursor:
                # Возращается кортеж - tuple
                (id, firstname, lastname) = row
                lst.append(Contact(id=str(id), firstname=firstname, lastname=lastname))

        finally:
            cursor.close()
        return lst


    def destroy(self):
        self.connection.close()