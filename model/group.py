

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
        return self.id == other.id and self.name == other.name