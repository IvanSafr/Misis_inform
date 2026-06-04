
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

import math
import matplotlib.pyplot as plt
import numpy as np

a = float(input("Введите начало отрезка a: "))
b = float(input("Введите конец отрезка b: "))
step = float(input("Введите шаг поиска: "))

n = int((b - a) / step) + 1
X = [a + i * step for i in range(n)]
Y = [math.cos(x) + x * math.sin(x) for x in X]

print("\nМассив X:")
for x in X:
    print(f"{x:10.5f}")

print("\nМассив Y:")
for y in Y:
    print(f"{y:10.5f}")

print("\nЛокальные экстремумы:")
has_local = False
plt.figure(figsize=(10, 6))

for i in range(1, n - 1):
    if Y[i] > Y[i - 1] and Y[i] > Y[i + 1]:
        print(f"Локальный максимум в точке i={i}: x = {X[i]:10.5f}, y = {Y[i]:10.5f}")
        plt.scatter(X[i], Y[i], color='orange', marker='o', s=100, zorder=5, label=f'Max: ({X[i]:.2f}, {Y[i]:.2f})' if not has_local else "")
        has_local = True
    elif Y[i] < Y[i - 1] and Y[i] < Y[i + 1]:
        print(f"Локальный минимум в точке i={i}: x = {X[i]:10.5f}, y = {Y[i]:10.5f}")
        plt.scatter(X[i], Y[i], color='green', marker='x', s=100, zorder=5, label=f'Min: ({X[i]:.2f}, {Y[i]:.2f})' if has_local else "")
        has_local = True

if not has_local:
    print("Локальные экстремумы отсутствуют")

global_max = max(Y)
max_index = Y.index(global_max)

global_min = min(Y)
min_index = Y.index(global_min)
plt.scatter(
    X[max_index],
    Y[max_index],
    color='red',       # Фиолетовый цвет
    marker='^',           # Маркер в виде квадрата ('s' от square)
    s=150,                # Увеличенный размер
    zorder=10,            # Поверх всех остальных линий и точек
    label=f'Глобальный Max ({X[max_index]:.2f}, {Y[max_index]:.2f})'
)
plt.scatter(
    X[min_index],
    Y[min_index],
    color='black',       # Оранжевый цвет
    marker='v',           # Маркер в виде квадрата
    s=150,                # Увеличенный размер
    zorder=10,            # Поверх всех остальных линий и точек
    label=f'Глобальный Min ({X[min_index]:.2f}, {Y[min_index]:.2f})'
)
plt.plot(X, Y)
plt.title("y = cos(x) + xsin(x)")
plt.xlabel("x")
plt.ylabel("y")
# plt.show()
print("\nГлобальные экстремумы:")
print(f"Глобальный максимум: x = {X[max_index]:10.5f}, y = {global_max:10.5f}")
print(f"Глобальный минимум: x = {X[min_index]:10.5f}, y = {global_min:10.5f}")
plt.show()
