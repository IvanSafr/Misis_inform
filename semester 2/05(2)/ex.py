import matplotlib.pyplot as plt
import math as m
import os

# Ввод параметров пользователя
a = float(input("Введите a: "))
b = float(input("Введите b: "))
c = float(input("Введите c: "))
X1 = float(input("Введите начало диапазона: "))
X2 = float(input("Введите конец диапазона: "))
dX = float(input("Введите шаг: "))

# ==========================================
# Часть А: Линейный график (нецелые числа)
# ==========================================
Xlist = []
x_curr = X1
while x_curr <= X2:
    # Оставляем только нецелые числа
    if not round(x_curr, 5).is_integer():
        Xlist.append(x_curr)
    x_curr += dX

Ylist = []
# for x in Xlist:
#     Y = a + b * x ** 2 + c * m.atan(x)
#     Ylist.append(Y)

Ylist = [a + b * x ** 2 + c * m.atan(x) for x in Xlist]

plt.figure(1)
plt.plot(Xlist, Ylist, '-b', marker='o', markersize=5)
plt.title('Линейный график f(x) = a + b*x^2 + c*arctg(x)')
plt.grid(True)

with open("Лр5.а.txt", "w", encoding="utf-8") as file:
    file.write(f"X: {Xlist}\nY: {Ylist}")


# ==========================================
# Часть Б: Столбчатая диаграмма (целые числа)
# ==========================================
Xlist = []
x_curr = X1
while x_curr <= X2:
    if round(x_curr, 5).is_integer():
        Xlist.append(int(round(x_curr)))
    x_curr += dX  # Исправлено: отступ изменен, чтобы избежать бесконечного цикла

Ylist = [a + b * x ** 2 + c * m.atan(x) for x in Xlist]

plt.figure(2)
plt.plot(Xlist, Ylist, '-b', marker='o', markersize=5)
plt.bar(Xlist, Ylist, color='green', alpha=0.6)
plt.title('Столбчатая диаграмма и график f(x) = a + b*x^2 + c*arctg(x)')
plt.grid(True)

with open("Лр5.б.txt", "w", encoding="utf-8") as file:
    file.write(f"Коэффициенты: a={a}, b={b}, c={c}\nДиапазон: [{X1}, {X2}], Шаг: {dX}\nX: {Xlist}\nY: {Ylist}")


# ==========================================
# Часть В: Круговая диаграмма (Шампуни)
# ==========================================
print("\nВведите данные для круговой диаграммы (Шампуни):")
s1 = float(input("Введите кол-во Head & Shoulders: "))
s2 = float(input("Введите кол-во Pantene: "))
s3 = float(input("Введите кол-во Clear: "))
s4 = float(input("Введите кол-во Syoss: "))

sizes = [s1, s2, s3, s4]
labels = ['Head & Shoulders', 'Pantene', 'Clear', 'Syoss']

plt.figure(3)
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title('Популярность марок шампуней')
plt.legend()

with open("Лр5.в.txt", "w", encoding="utf-8") as file:
    file.write(f"Данные круговой диаграммы: {labels} - {sizes}")


# ==========================================
# Часть Г: Чтение данных из файла и построение
# ==========================================
file_path = "Лр5.txt"
if os.path.exists(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        if len(lines) >= 2:
            Xlist_file = [float(x.strip().replace(',', '.')) for x in lines[0].split("\t") if x.strip()]
            Ylist_file = [float(y.strip().replace(',', '.')) for y in lines[1].split("\t") if y.strip()]

            plt.figure(4)
            plt.plot(Xlist_file, Ylist_file, '-b', marker='o', markersize=5)
            plt.title('График по дискретному набору известных значений (Таблица №17)')
            plt.grid(True)
        else:
            print(f"Файл {file_path} содержит недостаточно строк данных.")
else:
    print(f"\nПредупреждение: Файл {file_path} для построения четвертого графика не найден.")

# Отображение всех созданных окон с графиками
plt.show()