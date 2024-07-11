import json
import argparse

# Устанавливаем пути к файлам.
parser = argparse.ArgumentParser()
parser.add_argument('report_path', help='report path', type=str)
parser.add_argument('tests_path', help='tests path', type=str)
parser.add_argument('values_path', help='values path', type=str)
args = parser.parse_args()
report_path = args.report_path
tests_path = args.tests_path
values_path = args.values_path

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
