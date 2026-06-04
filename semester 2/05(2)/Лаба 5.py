import matplotlib.pyplot as plt
import math as m

print(
    "Какую программу проиграть? \n1: Линейный график \n2: Столбчатая диаграмма с линейным графиком \n3: Круговая диаграмма \n4: График по заданным значениям")
prog = int(input("Введите номер программы: "))

match prog:
    case 1:
        a = float(input("Введите a: "))
        b = float(input("Введите b: "))
        c = float(input("Введите c: "))
        X1 = float(input("Введите начало диапазона: "))
        X2 = float(input("Введите конец диапазона: "))
        dX = float(input("Введите шаг: "))

        # a) Линейный график – использовать НЕ ЦЕЛЫЕ числа при задании х
        Xlist = []
        x_curr = X1
        while x_curr <= X2:
            # Оставляем только нецелые числа (округление спасает от погрешностей float)
            if not round(x_curr, 5).is_integer():
                Xlist.append(x_curr)
            x_curr += dX

        Ylist = [a + b * x ** 2 + c * m.atan(x) for x in Xlist]

        plt.plot(Xlist, Ylist, '-b', marker='o', markersize=5)
        plt.title('Линейный график f(x) = a + b*x^2 + c*arctg(x)')

        with open("Лр5.а.txt", "w", encoding="utf-8") as file:
            file.write(f"X: {Xlist}\nY: {Ylist}")

    case 2:
        a = float(input("Введите a: "))
        b = float(input("Введите b: "))
        c = float(input("Введите c: "))
        X1 = float(input("Введите начало диапазона: "))
        X2 = float(input("Введите конец диапазона: "))
        dX = float(input("Введите шаг: "))

        # b) Столбчатая диаграмма - использовать ЦЕЛЫЕ числа при задании х
        Xlist = []
        x_curr = X1
        while x_curr <= X2:
            if round(x_curr, 5).is_integer():
                Xlist.append(round(x_curr))
            x_curr += dX

        Ylist = [a + b * x ** 2 + c * m.atan(x) for x in Xlist]

        plt.plot(Xlist, Ylist, '-b', marker='o', markersize=5)
        plt.bar(Xlist, Ylist, color='green', alpha=0.6)
        plt.title('Столбчатая диаграмма и график f(x) = a + b*x^2 + c*arctg(x)')

        with open("Лр5.б.txt", "w", encoding="utf-8") as file:
            file.write(f"Коэффициенты: a={a}, b={b}, c={c}\nДиапазон: [{X1}, {X2}], Шаг: {dX}\nX: {Xlist}\nY: {Ylist}")

    case 3:
        # Вариант 17 - Шампуни
        print("Введите данные для круговой диаграммы (Шампуни):")
        s1 = float(input("Введите кол-во Head & Shoulders: "))
        s2 = float(input("Введите кол-во Pantene: "))
        s3 = float(input("Введите кол-во Clear: "))
        s4 = float(input("Введите кол-во Syoss: "))

        sizes = [s1, s2, s3, s4]
        labels = ['Head & Shoulders', 'Pantene', 'Clear', 'Syoss']

        plt.pie(sizes, labels=labels, autopct='%1.1f%%')
        plt.title('Популярность марок шампуней')
        plt.legend()

        with open("Лр5.в.txt", "w", encoding="utf-8") as file:
            file.write(f"Данные круговой диаграммы: {labels} - {sizes}")

    case 4:
        try:
            # Читаем данные. strip() убирает переносы строк, replace меняет запятые на точки для float
            with open("Лр5.txt", "r", encoding="utf-8") as f:
                lines = f.readlines()
                Xlist = [float(x.strip().replace(',', '.')) for x in lines[0].split("\t") if x.strip()]
                Ylist = [float(y.strip().replace(',', '.')) for y in lines[1].split("\t") if y.strip()]

            plt.plot(Xlist, Ylist, '-b', marker='o', markersize=5)
            plt.title('График по дискретному набору известных значений (Таблица №17)')
            plt.grid(True)
        except FileNotFoundError:
            print("Ошибка: Файл 'Лр5.txt' не найден! Создайте его рядом со скриптом.")
        except Exception as e:
            print(f"Ошибка при чтении файла: {e}")

plt.show()