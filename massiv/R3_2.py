# Уровень 2

def input_matrix(row, col):
    print(f"Введите матрицу {row} * {col}")
    matrix = []
    cnt = 1
    while True:
        if len(matrix) == row:
            break

        in_v = []
        try:
            in_v = list(map(float, input(f"Введите через пробел строку {cnt} ({col} элементов): ").split()))
        except Exception as E:
            print(E)
        if len(in_v)!=col:
            continue
        matrix.append(in_v)
        cnt += 1

    return matrix
#
#  # 1.	Найти	сумму	элементов	матрицы	А	размером	5	×	7.
matrix = input_matrix(5, 7)

gool = '|'
summ = 0
for string in matrix:
    for el in string:
        gool += str(el) + " "
        summ += el
    gool += "|\n|"

print(gool[:-2])

print(f"\nСумма элементов в матрице = {summ}\n")



# 14 Сформировать	одномерный	массив	из	количеств	отрицательных
# элементов	столбцов	матрицы А размером	4	×	3.


matrix = input_matrix(4, 3)

answ = []
for x in range(3):
    cnt = 0
    for y in range(4):
        if matrix[y][x]<0:
            cnt += 1
    answ.append(cnt)
print(answ)



# 21	В	матрице	Н	размером	5	×	7	заполнены	первые	6	столб
# цов.	Поместить	в	качестве	предпоследнего	столбца	столбец,	состоящий	из
# максимальных	элементов	строк
matrix = input_matrix(5, 6)

print("\nСтарая матрица:\n")
for st in matrix:
    print(st)

for i in range(5):
    matrix[i].append(max(matrix[i]))

print("\n\nНовая матрица:\n")
for st in matrix:
    print(st)


# 36 Дана	матрица	A	размером	10	×	5.	Преобразовать	ма
# трицу	следующим	образом:	заменить	первый	элемент	столбца
# суммой	элементов	столбца,	расположенных	после	максималь
# ного	элемента,	если	максимальный	элемент	находится	в	пер
# вой	половине	столбца.	В	противном	случае	оставить	столбец
# без	изменения.

matrix = input_matrix(10, 5)


def transform_matrix_simple(A):

    # Создаем копию матрицы
    result = [row[:] for row in A]

    # Проходим по каждому столбцу
    for col in range(len(A[0])):
        # Извлекаем столбец
        column = [A[row][col] for row in range(len(A))]

        # Находим максимальный элемент и его индекс
        max_val = column[0]
        max_index = 0
        for i in range(1, len(column)):
            if column[i] > max_val:
                max_val = column[i]
                max_index = i

        # Проверяем, находится ли максимум в первой половине (первые 5 элементов)
        if max_index < 5:
            # Вычисляем сумму элементов после максимального
            sum_after_max = sum(column[max_index + 1:])

            # Заменяем первый элемент столбца
            result[0][col] = sum_after_max

    return result

print("Исходная матрица:")
for row in matrix:
    print(row)

print("\nПреобразованная матрица:")
transformed = transform_matrix_simple(matrix)
for row in transformed:
    print(row)