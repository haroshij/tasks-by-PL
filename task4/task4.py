import argparse

# Устанавливаем пути к файлам.
parser = argparse.ArgumentParser()
parser.add_argument('nums_path', help='nums path', type=str)
args = parser.parse_args()
nums_path = args.nums_path

# Открываем файл с числами в режиме чтения.
with open(nums_path) as nums:

    # Числа записываем в массив.
    nums = [int(num) for num in nums.readlines()]

    # Считаем среднее, до которого будем считать ходы.
    average = round(sum(nums) / len(nums), 0)

    # Считаем ходы по каждому элементу и выводим на экран.
    print(int(sum([abs(average - num) for num in nums])))
