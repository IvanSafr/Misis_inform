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

