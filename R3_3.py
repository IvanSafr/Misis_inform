from operator import index


def in_matrix():
    matrix = []
    n = 0
    while True:
        in_val = input("Введите строку массива (для прекращения ввода - end): ")
        string = []
        if in_val == 'end':
            break

        try:
            string = list(map(float, in_val.split()))

        except Exception as E:
            print(E)

        if n == 0:
            n = len(string)
        elif n != len(string):
            print("Введите строку той же размерности")
            continue

        matrix.append(string)

    return matrix

# 1 4 11

# .	Найти	все	максимальные	элементы	одномерного	массива
# (предполагается,	что	в	массиве	несколько	одинаковых	макси
# мальных	элементов)	за	один	проход	исходного	массива.	Сфор
# мировать	массив	из	их	индексов.

# matrix = in_matrix()
# index_lst = []
# max_el = -1
#
# print(f"{'_'*100}\nМатрица:")
# print([x for x in matrix], sep='\n')
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
#             index_lst.append((i, j))
#         elif matrix[i][j] == max_el:
#             index_lst.append((i, j))
#
# print(f"{'-'*100}\nИндексы максимальных элементов:\n{index_lst}")

#  4.	Задан	массив	В.	Максимальный	элемент	(или	макси
# мальные	элементы,	если	их	несколько)	заменить	суммой	эле
# ментов	массива,	расположенных	до	него	(до	каждого	из	них,
# если	их	несколько).

import copy
matrix = in_matrix()

max_el = -1

print(f"{'_'*100}\nМатрица:")
print([x for x in matrix], sep='\n')


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

print(f"\n{matrix}")
print(f"\n{matrix_c}")

#  11.	Вычислить	значения	функции	y =	cosx +	xsinx	в	n	точ
# ках	отрезка	[a, b].	Результат	получить	в	двух	массивах	Х	(ар
# гумент),	Y	(функция).	Используя	сформированные	массивы,
# определить	все	значения	аргумента,	при	которых	функция
# имеет	максимум	или	минимум	(включая	локальные).	Для	то
# чек,	в	которых	достигается	экстремум,	вывести	значения	ар
# гумента,	функции	и	вид	эстремума	(максимум	или	минимум).
# Определить	глобальные	экстремумы.
#  Указание.	Функция	имеет	локальный	максимум	со	значени
# ем	yi	(из	массива Y)	при	значении	аргумента	xi	(из	массива	Х),
# если	значения	функции	yi–1	и	yi+1	в	д