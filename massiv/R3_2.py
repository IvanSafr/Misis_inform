# Уровень 2

import random


def input_matrix(row, col, min_val=-10, max_val=10, decimal_places=2):
    """
    Генерирует матрицу со случайными значениями

    Параметры:
    - row: количество строк
    - col: количество столбцов
    - min_val: минимальное значение элементов (по умолчанию 0)
    - max_val: максимальное значение элементов (по умолчанию 10)
    - decimal_places: количество знаков после запятой (по умолчанию 2)
    """
    #print(f"Сгенерирована матрица {row} * {col} со случайными значениями:")
    matrix = []

    for i in range(row):
        row_values = []
        for j in range(col):
            # Генерируем случайное число в заданном диапазоне
            value = random.randint(min_val, max_val)
            # Округляем до указанного количества знаков
            value = round(value, decimal_places)
            row_values.append(value)
        matrix.append(row_values)
        #print(f"{row_values}")

    return matrix
#
#  # 1.	Найти	сумму	элементов	матрицы	А	размером	5	×	7.   +
print(f"{'_'*100}\nНайти	сумму	элементов	матрицы	А	размером	5	×	7.\n")
matrix = input_matrix(5, 7)


summ = 0
for st in matrix:
    for col in st:
        summ += col

for a in matrix:
    for i in range(len(a)):
        if a[i] > 0:
            print((f" {a[i]}" + ' ' * (5 - len(str(a[i])))), end='')
            continue
        print((f"{a[i]}" + ' ' * (6 - len(str(a[i])))), end='')
    print(" ")
#
print(f"\nСумма элементов в матрице = {summ}\n")



# 14 Сформировать	одномерный	массив	из	количеств	отрицательных   +
# элементов	столбцов	матрицы А размером	4	×	3.
print(f"{'_'*100}\nСформировать	одномерный	массив	из	количеств	отрицательных элементов	столбцов	матрицы А размером	4	×	3.")

matrix = input_matrix(4, 3)
for a in matrix:
    for i in range(len(a)):
        if a[i] > 0:
            print((f" {a[i]}" + ' ' * (5 - len(str(a[i])))), end='')
            continue
        print((f"{a[i]}" + ' ' * (6 - len(str(a[i])))), end='')
    print(" ")
answ = []
for x in range(3):
    cnt = 0
    for y in range(4):
        if matrix[y][x]<0:
            cnt += 1
    answ.append(cnt)
print(answ)



# 21	В	матрице	Н	размером	5	×	7	заполнены	первые	6	столб
# цов.	Поместить	в	качестве	последнего	столбца	столбец,	состоящий	из
# максимальных	элементов	строк    +
print(f"""{'_'*100}\nВ	матрице	Н	размером	5	×	7	заполнены	первые	6	столбцов.	
Поместить	в	качестве	предпоследнего	столбца	столбец,	состоящий	из
 максимальных	элементов	строк""")
matrix = input_matrix(5, 6)

print("\nСтарая матрица:\n")
for a in matrix:
    for i in range(len(a)):
        if a[i] > 0:
            print((f" {a[i]}" + ' ' * (5 - len(str(a[i])))), end='')
            continue
        print((f"{a[i]}" + ' ' * (6 - len(str(a[i])))), end='')
    print(" ")

for i in range(5):
    matrix[i].insert(5, max(matrix[i]))

print("\n\nНовая матрица:\n")
for a in matrix:
    for i in range(len(a)):
        if a[i] > 0:
            print((f" {a[i]}" + ' ' * (5 - len(str(a[i])))), end='')
            continue
        print((f"{a[i]}" + ' ' * (6 - len(str(a[i])))), end='')
    print(" ")


# 36 Дана	матрица	A	размером	10	×	5.	Преобразовать	ма
# трицу	следующим	образом:	заменить	первый	элемент	столбца
# суммой	элементов	столбца,	расположенных	после	максималь
# ного	элемента,	если	максимальный	элемент	находится	в	пер
# вой	половине	столбца.	В	противном	случае	оставить	столбец
# без	изменения.

print(f"""{'_'*100}\nДана	матрица	A	размером	10	×	5.	Преобразовать	матрицу	следующим	образом:	
заменить первый	элемент	столбцасуммой	элементов	столбца,	
расположенных	после	максимального	элемента,
если	максимальный	элемент	находится	в	первой	половине	столбца.	
В	противном	случае	оставить	столбец без	изменения.""")


matrix = input_matrix(10, 5)



print("Исходная матрица:")
for a in matrix:
    for i in range(len(a)):
        if a[i] > 0:
            print((f" {a[i]}" + ' ' * (5 - len(str(a[i])))), end='')
            continue
        print((f"{a[i]}" + ' ' * (6 - len(str(a[i])))), end='')
    print(" ")

# Обрабатываем каждый столбец
for col in range(5):
    # Находим максимальный элемент и его индекс в столбце
    max_val = matrix[0][col]
    max_row = 0
    for row in range(1, 10):
        if matrix[row][col] > max_val:
            max_val = matrix[row][col]
            max_row = row

    # Проверяем, находится ли максимум в первой половине (строки 0-4)
    if max_row <= 4:
        # Сумма элементов после максимального
        sum_after_max = 0
        for row in range(max_row + 1, 10):
            sum_after_max += matrix[row][col]

        # Заменяем первый элемент столбца
        matrix[0][col] = sum_after_max

print("\n\n После замены:")
for a in matrix:
    for i in range(len(a)):
        if a[i] > 0:
            print((f" {a[i]}" + ' ' * (5 - len(str(a[i])))), end='')
            continue
        print((f"{a[i]}" + ' ' * (6 - len(str(a[i])))), end='')
    print(" ")
