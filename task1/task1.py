import argparse


def circular_array_path(n, m):
    """Функция для определения пути
    по круговому массиву"""

    # Если интервал равен 1, то зациклимся:
    # в таком случае выходим из функции ни с чем.
    if m == 1:
        return

    res = 1  # Наш путь.
    cur = 1  # Здесь будем хранить положение после каждого шага.

    # Формируем наш путь.
    while True:
        cur = (cur + m - 1) % n
        if cur == 1:  # Как только пришли к первому элементу, завершаем цикл.
            break
        elif cur == 0:  # Для случая если попали на последний элемент.
            res = res * 10 + n
        else:
            res = res * 10 + cur  # Обновляем путь.

    # Выводим результат на экран.
    print(res)


if __name__ == '__main__':
    # Получаем данные по n и m.
    parser = argparse.ArgumentParser()
    parser.add_argument('n', help='lenght of array', type=int)
    parser.add_argument('m', help='interval', type=int)
    args = parser.parse_args()
    n, m = args.n, args.m
    circular_array_path(n, m)
