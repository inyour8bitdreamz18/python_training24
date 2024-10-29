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
            cursor.execute("select id, firstname, lastname, address, home, mobile, work, email, email2, email3 from addressbook")  # where deprecated='NULL'
            for row in cursor:
                # Возращается кортеж - tuple
                (id, firstname, lastname, address, home, mobile, work, email, email2, email3) = row
                lst.append(Contact(id=str(id), firstname=firstname, lastname=lastname, address=address,
                                   home=home, mobile=mobile, work=work, email=email, email2=email2, email3=email3))

        finally:
            cursor.close()
        return lst

    def get_contact_by_id(self, id):
        contact = None
        cursor = self.connection.cursor()
        try:
            cursor.execute(f'''select id, firstname, lastname, address, home, mobile, work, email, email2, email3 from addressbook  where id={id}''')  # where deprecated='NULL'
            for row in cursor:
                # Возращается кортеж - tuple
                (id, firstname, lastname, address, home, mobile, work, email, email2, email3) = row
                contact = (Contact(id=str(id), firstname=firstname, lastname=lastname, address=address,
                                   home=home, mobile=mobile, work=work, email=email, email2=email2, email3=email3))
        finally:
            cursor.close()
        return contact

    def get_contacts_by_group_id(self, id_group):
         lst = []
         cursor = self.connection.cursor()
         try:
             cursor.execute(f'''select id, group_id from address_in_groups where group_id={id_group}''')
             for row in cursor:
                  (id, group_id) = row
                  lst.append(Contact(id=str(id), group_id=group_id))
         finally:
            cursor.close()
         return lst


    def destroy(self):
        self.connection.close()