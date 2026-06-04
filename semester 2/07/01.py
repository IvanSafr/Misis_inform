import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

x_data = np.array([5, 10, 15, 20, 25, 30, 40, 50, 60, 70, 80], dtype=float)
y_data = np.array([130, 141, 150.2, 163, 170, 180, 194, 206, 213, 218, 223.5], dtype=float)
n = len(x_data)

sum_x = np.sum(x_data)
sum_y = np.sum(y_data)
sum_x2 = np.sum(x_data**2)
sum_xy = np.sum(x_data * y_data)

matrix = np.array([
    [n, sum_x, sum_y],
    [sum_x, sum_x2, sum_xy]
], dtype=float)

def gauss_solve(m):
    factor = m[1, 0] / m[0, 0]
    m[1] = m[1] - factor * m[0]
    a1 = m[1, 2] / m[1, 1]
    a0 = (m[0, 2] - m[0, 1] * a1) / m[0, 0]
    return a0, a1

a0, a1 = gauss_solve(matrix.copy())

import numpy as np
A = np.array([
    [n, sum_x],
    [sum_x, sum_x2]
], dtype=float)

B = np.array([sum_y, sum_xy], dtype=float)

def cramer_solve(A, B):
    delta = np.linalg.det(A)
    if abs(delta) < 1e-12:
        return "Система не имеет уникального решения"
    A0 = A.copy()
    A0[:, 0] = B

    delta_0 = np.linalg.det(A0)
    A1 = A.copy()
    A1[:, 1] = B
    delta_1 = np.linalg.det(A1)
    a0_res = delta_0 / delta
    a1_res = delta_1 / delta
    return a0_res, a1_res, delta, delta_0, delta_1
a0_cr, a1_cr, d, d0, d1 = cramer_solve(A, B)

y_pred = a0 + a1 * x_data

main_road_len = np.sqrt((x_data.max() - x_data.min())**2 +
(y_pred.max() - y_pred.min())**2)
distances = np.abs(a1 * x_data - y_data + a0) / np.sqrt(a1**2 + 1)
total_side_roads = np.sum(distances)
x_pol = 50
y_pol = a0 + a1 * x_pol
r_squared = 1 - (np.sum((y_data - y_pred)**2) / np.sum((y_data -
np.mean(y_data))**2))
print(f"--- РЕЗУЛЬТАТЫ (по крамеру) ---")
print(f"Главный определитель (Delta): {d:.2f}")
print(f"Delta 0: {d0:.2f}")
print(f"Delta 1: {d1:.2f}")
print(f"Результат: a0 = {a0_cr:.5f}, a1 = {a1_cr:.5f}")
print(f"")
print(f"--- РЕЗУЛЬТАТЫ (по гауссу) ---")
print(f"Коэффициент a0: {a0:.5f}")
print(f"Коэффициент a1: {a1:.5f}")
print(f"Уравнение: y = {a0:.4f} + ({a1:.4f}) * x")
print(f"")

def linear_func(x, a0, a1):
    return a0 + a1 * x

args, _ = curve_fit(linear_func, x_data, y_data)
a0_approx, a1_approx = args

y_pred_approx = linear_func(x_data, a0_approx, a1_approx)
r_squared_approx = 1 - (np.sum((y_data - y_pred_approx)**2) / np.sum((y_data - np.mean(y_data))**2))

print(f"--- АППРОКСИМАЦИЯ ---")
print(f"Коэффициент a0: {a0_approx:.5f}")
print(f"Коэффициент a1: {a1_approx:.5f}")
print(f"Уравнение: y = {a0_approx:.4f} + ({a1_approx:.4f}) * x")
print(f"Точность модели (R^2): {r_squared_approx:.4f}")
print(f"")

print(f"\n--- ГЕОМЕТРИЯ ---")
print(f"Длина основной трассы: {main_road_len:.2f}")
print(f"Сумма подъездных дорог: {total_side_roads:.2f}")
print(f"Общая длина сети: {main_road_len + total_side_roads:.2f}")
print(f"Координаты магазина (X=50): ({x_pol}, {y_pol:.3f})")
print(f"Точность модели (R^2): {r_squared:.4f}")
plt.figure(figsize=(12, 7))
plt.scatter(x_data, y_data, color='royalblue', label='Пункты (данные)', zorder=3)

plt.plot(x_data, y_pred, color='crimson', lw=2, label='Основная дорога', zorder=2)
plt.scatter(x_pol, y_pol, color='forestgreen', s=200, marker='*',
label='Магазин', zorder=4)
for i in range(n):
    plt.plot([x_data[i], x_data[i]], [y_data[i], y_pred[i]], 'gray',
linestyle='--', lw=0.8)
plt.title('Дорога', fontsize=14)
plt.xlabel('Координата X')
plt.ylabel('Координата Y')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()