import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

def f(x, a, b, c):
    return a + b * x**2 + c * np.arctan(x)

# --- ЗАДАНИЕ 1: Ввод данных с клавиатуры ---
print("Введите коэффициенты и параметры для графика f(x) = a + b*x^2 + c*arctg(x)")
a = float(input("Коэффициент a: "))
b = float(input("Коэффициент b: "))
c = float(input("Коэффициент c: "))
start = float(input("Начало диапазона (например, -10): "))
end = float(input("Конец диапазона (например, 10): "))
step = float(input("Шаг для нецелых чисел (например, 0.5): "))

# Генерация данных
# a) Нецелые числа (линейный график)
x_float = np.arange(start, end + step, step)
y_float = f(x_float, a, b, c)

# b) Целые числа (столбчатая + линейная)
x_int = np.arange(int(start), int(end) + 1, 1)
y_int = f(x_int, a, b, c)

# c) Данные для круговой диаграммы (Шампуни)
shampoo_brands =['Head & Shoulders', 'Pantene', 'Clear', 'Garnier', 'Nivea']
shampoo_shares =[35, 25, 15, 15, 10]

# --- ПОСТРОЕНИЕ ГРАФИКОВ (Задание 1) ---
plt.figure(figsize=(15, 5))

# a) Линейный график
plt.subplot(1, 3, 1)
plt.plot(x_float, y_float, 'b-', label='f(x)')
plt.title("а) Линейный график (нецелые x)")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.legend()

# b) Комбинированный график
plt.subplot(1, 3, 2)
plt.bar(x_int, y_int, color='lightblue', label='Столбцы')
plt.plot(x_int, y_int, 'r-o', label='Линия')
plt.title("b) Комбинированный (целые x)")
plt.xlabel("x")
plt.grid(True)
plt.legend()

# c) Круговая диаграмма
plt.subplot(1, 3, 3)
plt.pie(shampoo_shares, labels=shampoo_brands, autopct='%1.1f%%', startangle=140)
plt.title("c) Круговая диаграмма (Шампуни)")

plt.tight_layout()
plt.show()

# --- ЗАДАНИЕ 2: Сохранение результатов в файл ---
df_float = pd.DataFrame({'x': x_float, 'f(x)': y_float})
df_int = pd.DataFrame({'x': x_int, 'f(x)': y_int})
df_pie = pd.DataFrame({'Бренд': shampoo_brands, 'Доля (%)': shampoo_shares})

df_float.to_csv('data_float.csv', index=False)
df_int.to_csv('data_int.csv', index=False)
df_pie.to_csv('data_pie.csv', index=False)
print("\nДанные для Excel сохранены в .csv файлы.")

# --- ЗАДАНИЕ 4: Сохранение дискретных данных в .txt ---
# Данные таблицы №17
discrete_x =[5, 10, 15, 20, 25, 30, 40, 50, 60, 70, 80]
discrete_y =[130, 141, 152, 163, 170, 180, 194, 206, 213, 218, 223.5]

with open('data_var17.txt', 'w', encoding='utf-8') as file:
    file.write("X\tY\n")
    for dx, dy in zip(discrete_x, discrete_y):
        file.write(f"{dx}\t{dy}\n")
print("Дискретные данные (вариант 17) сохранены в 'data_var17.txt'.")

# --- ЗАДАНИЕ 5: Чтение из файла и построение графика ---
read_x, read_y = [],[]
with open('data_var17.txt', 'r', encoding='utf-8') as file:
    next(file) # Пропускаем заголовок
    for line in file:
        vals = line.strip().split('\t')
        read_x.append(float(vals[0]))
        read_y.append(float(vals[1]))

plt.figure(figsize=(8, 5))
plt.plot(read_x, read_y, 'g-o', markersize=8)
plt.title("Задание 5: График по дискретным данным (Таблица №17)")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.show()