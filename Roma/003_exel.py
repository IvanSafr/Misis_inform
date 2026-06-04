from openpyxl import Workbook
from openpyxl.chart import LineChart, Reference

# Имена файлов
input_file = "discrete_data.txt"
excel_file = "Result_Graph.xlsx"

# 1. Чтение данных (парсинг из текстового файла)
x_values = []
y_values = []

try:
    with open(input_file, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) == 2:
                try:
                    # Заменяем запятую на точку перед конвертацией, если она есть
                    x_str = parts[0].replace(',', '.')
                    y_str = parts[1].replace(',', '.')

                    x = float(x_str)
                    y = float(y_str)
                    x_values.append(x)
                    y_values.append(y)
                except ValueError:
                    continue
    print(f"Успешно прочитано {len(x_values)} строк данных.")
except FileNotFoundError:
    print(f"Ошибка: Файл {input_file} не найден!")
    exit()

# 2. Создание файла Excel
wb = Workbook()
ws = wb.active
ws.title = "Данные и График"

# Записываем заголовки. "f(x)" станет названием линии
ws.append(["Значение X", "f(x)"])

# Записываем данные
for x, y in zip(x_values, y_values):
    ws.append([x, y])

# 3. Создание ЛИНЕЙНОГО графика (LineChart) без использования Series
chart = LineChart()
chart.title = "График по дискретным данным"
chart.style = 13
chart.x_axis.title = "Ось X"
chart.y_axis.title = "Ось Y"

# Диапазон Y-данных (включаем 1-ю строку с заголовком "f(x)")
y_data = Reference(ws, min_col=2, min_row=1, max_row=len(y_values) + 1)

# Диапазон X-данных для подписей оси X (только числа, без заголовка)
x_data = Reference(ws, min_col=1, min_row=2, max_row=len(x_values) + 1)

# Добавляем Y-данные (название линии возьмется из шапки таблицы)
chart.add_data(y_data, titles_from_data=True)

# Устанавливаем X-данные как подписи для оси X
chart.set_categories(x_data)

# Убираем легенду, так как у нас всего одна линия (с ней график будет чище)
chart.legend = None

# Вставляем график на лист Excel, начиная с ячейки D2
ws.add_chart(chart, "D2")

# 4. Сохранение результата
wb.save(excel_file)
print(f"Файл {excel_file} успешно обновлен!")