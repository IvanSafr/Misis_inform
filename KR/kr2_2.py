import random, copy
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

n = int(input("Введите размерность квадратной матрицы n*n (n): "))

matrix = input_matrix(n, n)
matrix_new = copy.deepcopy(matrix)
print("Начальная матрица:")
for a in matrix:
    for i in range(len(a)):
        if a[i] > 0:
            print((f" {a[i]}" + ' ' * (5 - len(str(a[i])))), end='')
            continue
        print((f"{a[i]}" + ' ' * (6 - len(str(a[i])))), end='')
    print(" ")

for i in range(n):
    for j in range(n):
        matrix_new[n - 1 - j][n - 1 - i] = matrix[i][j]

print("\nМатрица после изменения:")
for a in matrix_new:
    for i in range(len(a)):
        if a[i] > 0:
            print((f" {a[i]}" + ' ' * (5 - len(str(a[i])))), end='')
            continue
        print((f"{a[i]}" + ' ' * (6 - len(str(a[i])))), end='')
    print(" ")