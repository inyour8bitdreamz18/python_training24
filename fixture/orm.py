from pony.orm import *
from datetime import datetime
from model.group import Group
from model.contact import Contact
#from pymysql.converters import decoders # На случай, если конвертация не работает по умолчанию

class ORMFixture:

    db = Database()
    # Описание структуры таблицы
    class ORMGroup(db.Entity): # Привязываем этот класс с БД с помощью db.Entity
        _table_ = "group_list" # Имя таблицы в БД
        id = PrimaryKey(int, column='group_id')
        name = Optional(str, column='group_name')
        header = Optional(str, column='group_header')
        footer = Optional(str, column='group_footer')
        contacts = Set(lambda: ORMFixture.ORMContact, table='address_in_groups', column='id', reverse="groups", lazy=True) # lazy=True подгружаем данные в момент вызова

    # Описание структуры таблицы
    class ORMContact(db.Entity): # Привязываем этот класс с БД с помощью db.Entity
        _table_ = "addressbook" # Имя таблицы в БД
        id = PrimaryKey(int, column='id')
        firstname = Optional(str, column='firstname')
        lastname = Optional(str, column='lastname')
        deprecated = Optional(datetime, column='deprecated')
        groups = Set(lambda: ORMFixture.ORMGroup, table='address_in_groups', column='group_id', reverse="contacts", lazy=True)

    # Выполняем привязку к БД
    def __init__(self, host, name, user, password):
        # Привязываем с помощью bind
        self.db.bind('mysql', host=host, database=name, user=user, password=password) # <-(....,conv=decoders) не обязательно, так как конвертируется по умолчанию
        self.db.generate_mapping()
        sql_debug(True) # Функция для отслеживания запросов в БД


    def convert_groups_to_modals(self, groups):
        def convert(group):
            return Group(id=str(group.id), name=group.name, header=group.header, footer=group.footer)
        return list(map(convert, groups))


    def convert_contacts_to_modals(self, contacts):
        def convert(contact):
            return Contact(id=str(contact.id), firstname=contact.firstname, lastname=contact.lastname)
        return list(map(convert, contacts))


    @db_session
    def get_group_list(self):
        return self.convert_groups_to_modals(list(select(g for g in ORMFixture.ORMGroup)))

    @db_session
    def get_contact_list(self):
        return self.convert_contacts_to_modals(list(select(c for c in ORMFixture.ORMContact if c.deprecated is None)))

    @db_session
    def get_contacts_in_groups(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        return self.convert_contacts_to_modals(orm_group.contacts)

    @db_session
    def get_contacts_not_in_groups(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        return self.convert_contacts_to_modals(
            list(select(c for c in ORMFixture.ORMContact if c.deprecated is None and orm_group not in c.groups)))
