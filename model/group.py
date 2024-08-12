# В модуле sys хранятся константы
from sys import maxsize

class Group:
    def __init__(self, name=None, header=None, footer=None, id=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id

    # Вывод данных
    def __repr__(self):
        return "%s:%s" % (self.id, self.name)

    # Сравнение по содержимому
    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            # Maxsize выдает большое целое число
            return maxsize