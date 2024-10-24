import jsonpickle
from model.group import Group
import random
import string
import os.path
# Для чтения командной строки
import getopt
# Для доступа к чтению опций из командной строки
import sys

# Как правильно читать опции из командной строки
try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 3
f = "data/groups.json"

for o,a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Group(name="", header="", footer="")]+[
    Group(name=random_string("name", 10), header=random_string("header", 20), footer=random_string("footer", 20))
    for i in range(n)
]
'''
Генерация комбинаций данных для группы
testdata = [
    Group(name=name, header=header, footer=footer)
    for name in ["", random_string("name", 10)]
    for header in ["", random_string("header", 20)]
    for footer in ["", random_string("footer", 20)]
]
'''
# Создаем файл для сохранения данных
file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)
# Сохраняем сгенерированные данные в файл
with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))

    '''
    # json.dumps преобразует данные в строку в формате json
    # default=lambda x:x.__dict__ в случае, если не получается преобразовать данные в json
    out.write(json.dumps(testdata, default=lambda x:x.__dict__, indent=2))
    '''