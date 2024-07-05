# Наши пути к файлам.
# При необходимости замените на свои :)
circle_path = 'circle.txt'
dots_path = 'dots.txt'

# Считываем данные по окружности:
# радиус и координаты центра.
with open(circle_path) as circle:
    center_x, center_y = tuple(map(int, circle.readline().split()))
    radius = int(circle.readline())

# Считываем координаты точек
with open(dots_path) as dots:
    dots = [tuple(map(int, dot.split())) for dot in dots.readlines()]

# Проходим по каждой точке и считаем расстояние от центра окружности:
# если расстояние меньше радиуса, то точка внутри окружности,
# если расстояние равно радиусу, то точка на окружности,
# если расстояние больше радиуса, то точка вне окружности.
# По итогу сравнения каждой точки, выводим результат.
for dot_x, dot_y in dots:
    distance = int(((dot_x - center_x) ** 2 + (dot_y - center_y) ** 2) ** 0.5)
    if distance < radius:
        print('1')
    elif distance == radius:
        print('0')
    else:
        print('2')
