import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# 1. Исходные данные варианта 17
x_data = np.array([5, 10, 15, 20, 25, 30, 40, 50, 60, 70, 80])
y_data = np.array([130, 141, 150.2, 163, 170, 180, 194, 206, 213, 218, 223.5])

# 2. Функция для аппроксимации (линейная регрессия)
def linear_func(x, a1, a0):
    return a1 * x + a0

# 3. Нахождение коэффициентов с помощью curve_fit
# args содержит [a1, a0]
args, _ = curve_fit(linear_func, x_data, y_data)
a1, a0 = args

print("--- Результаты линейной регрессии ---")
print(f"Коэффициент a1: {a1:.5f}")
print(f"Коэффициент a0: {a0:.5f}")
print(f"Уравнение прямой: Y = {a1:.5f} * X + {a0:.5f}")

# 4. Поиск ближайшей точки к прямой (Дополнительное задание)
# Формула расстояния: d = |a1*x - y + a0| / sqrt(a1^2 + (-1)^2)
distances = np.abs(a1 * x_data - y_data + a0) / np.sqrt(a1**2 + 1)

# Находим индекс минимального расстояния
min_idx = np.argmin(distances)
closest_x = x_data[min_idx]
closest_y = y_data[min_idx]
min_distance = distances[min_idx]

print("\n--- Дополнительное задание (Вариант 17) ---")
print(f"Ближайшая точка: X = {closest_x}, Y = {closest_y}")
print(f"Кратчайшее расстояние до прямой: {min_distance:.5f}")

# 5. Построение графика
plt.figure(figsize=(10, 6))

# Исходные точки
plt.scatter(x_data, y_data, color='blue', label='Исходные данные', zorder=2)

# Аппроксимирующая прямая
x_line = np.linspace(min(x_data) - 5, max(x_data) + 5, 100)
y_line = linear_func(x_line, a1, a0)
plt.plot(x_line, y_line, color='red', linestyle='--', label=f'Аппроксимация (Y = {a1:.2f}X + {a0:.2f})', zorder=1)

# Выделение ближайшей точки
plt.scatter(closest_x, closest_y, color='green', s=150, edgecolor='black',
            label='Ближайшая точка', zorder=3)

# Оформление графика
plt.title('Линейная регрессия (Вариант 17)', fontsize=14)
plt.xlabel('X', fontsize=12)
plt.ylabel('Y', fontsize=12)
plt.grid(True, linestyle=':', alpha=0.7)
plt.legend()
plt.show()