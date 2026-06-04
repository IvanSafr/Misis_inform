import random

def in_matrix(row, col, min_val=-10, max_val=10, decimal_places=2):
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

# a, b = map(int, input("Введите размерность матрицы через пробел: ").split())
# matrix = in_matrix(a, b)
# index_lst = []
# max_el = -1
#
# print(f"{'_'*100}\nМатрица:")
# for a in matrix:
#     for i in range(len(a)):
#         if a[i] > 0:
#             print((f" {a[i]}" + ' ' * (5 - len(str(a[i])))), end='')
#             continue
#         print((f"{a[i]}" + ' ' * (6 - len(str(a[i])))), end='')
#     print(" ")
#
#
# j_max = len(matrix[0])
#
# for i in range(len(matrix)):
#     for j in range(j_max):
#         if max_el==-1:
#             max_el = matrix[i][j]
#         elif matrix[i][j] > max_el:
#             max_el = matrix[i][j]
#             index_lst.clear()
#             index_lst.append((i+1, j+1))
#         elif matrix[i][j] == max_el:
#             index_lst.append((i+1, j+1))
# print(f'Максимальный элемент: {max_el}')
# print(f"\nИндексы максимальных элементов:\n{index_lst}\n{'-'*100}")
#
#


import copy


a, b = map(int, input("Введите размерность матрицы через пробел: ").split())
matrix = in_matrix(a, b)

max_el = -1

print(f"{'_'*100}\nМатрица:")
for a in matrix:
    for i in range(len(a)):
        if a[i] > 0:
            print((f" {a[i]}" + ' ' * (5 - len(str(a[i])))), end='')
            continue
        print((f"{a[i]}" + ' ' * (6 - len(str(a[i])))), end='')
    print(" ")


j_max = len(matrix[0])
summ = 0
matrix_c = matrix.copy()

for i in range(len(matrix)):
    for j in range(j_max):

        if max_el==-1:
            max_el = matrix[i][j]

        elif matrix[i][j] > max_el:
            matrix_c = copy.deepcopy(matrix)
            max_el = matrix[i][j]
            matrix_c[i][j] = summ

        elif matrix[i][j] == max_el:
            matrix_c[i][j] = summ

        summ += matrix[i][j]

print(f"Максимальный элемент {max_el}")
print(f"\nНовая матрица:")
for a in matrix_c:
    for i in range(len(a)):
        if a[i] > 0:
            print((f" {a[i]}" + ' ' * (5 - len(str(a[i])))), end='')
            continue
        print((f"{a[i]}" + ' ' * (6 - len(str(a[i])))), end='')
    print(" ")
print(f"\n{'_'*100}")
