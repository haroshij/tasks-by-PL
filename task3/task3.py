import json

# Наши пути к файлам.
# При необходимости замените на свои :)
report_path = 'report.json'
tests_path = 'tests.json'
values_path = 'values.json'

# Выгружаем json-файлы в переменные.
with open(tests_path) as file:
    tests = json.load(file)
with open(values_path) as file:
    values = json.load(file)

# Создаём словарь со значениями из файла values.
values_dict = dict()
for el in values['values']:
    values_dict[el['id']] = el['value']


def set_value(dct):
    """Функция для рекурсивной замены значений
    по ключу value в файле test на данные
    из файла values"""

    if 'id' in dct and dct['id'] in values_dict:
        dct['value'] = values_dict[dct['id']]
    if 'values' in dct:
        for el in dct['values']:
            set_value(el)


# Проходим по tests и меняем значения по ключу value.
for el in tests['tests']:
    set_value(el)

# Записываем в файл report.json.
with open(report_path, 'w') as file:
    json.dump(tests, file)
