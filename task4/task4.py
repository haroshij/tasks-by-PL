# Наш путь к файлу.
# При необходимости замените на свои :)
nums_path = 'nums.txt'

# Открываем файл с числами в режиме чтения.
with open(nums_path) as nums:

    # Числа записываем в массив.
    nums = [int(num) for num in nums.readlines()]

    # Считаем среднее, до которого будем считать ходы.
    average = round(sum(nums) / len(nums), 0)

    # Считаем ходы по каждому элементу и выводим на экран.
    print(int(sum([abs(average - num) for num in nums])))
