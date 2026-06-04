import pandas as pd
import openpyxl
from openpyxl import load_workbook, Workbook
from openpyxl.styles import PatternFill, Font, Border, Side, Alignment
from openpyxl.utils.dataframe import dataframe_to_rows
from openpyxl.chart import (
    ScatterChart, PieChart, BarChart, LineChart, Reference
)
from openpyxl.chart.series import Series  # <--- Импортируем Series явно из подмодуля
import os
import shutil

# ==========================================
# НАСТРОЙКИ
# ==========================================
STUDENT_NAME = "Сафронов Иван Евгеньевич"  # Ваша фамилия
GROUP_NAME = "БЭН-25-1"
WORK_DIR = f"{STUDENT_NAME}"
INPUT_FILE = "Сафронов Иван Евгеньевич-БЭН-25-1_Вар18.xlsx"  # Имя вашего файла с Практической №1
OUTPUT_FILE_MAIN = "Пр.раб.-2.xlsx"
OUTPUT_FILE_PROD = "Производители.xlsx"

# Создаем папку студента
if not os.path.exists(WORK_DIR):
    os.makedirs(WORK_DIR)


# ==========================================
# 0. ГЕНЕРАЦИЯ ТЕСТОВЫХ ДАННЫХ (ЕСЛИ НЕТ ФАЙЛА)
# ==========================================
# def create_dummy_input():
#     print(f"Файл {INPUT_FILE} не найден. Создаю тестовый файл на основе PDF...")
#     wb = Workbook()
#     ws = wb.active
#     ws.title = "Лист1"
#
#     # Заголовки (строка 2 по заданию ПР1)
#     headers = ["№ п/п", "Товар", "Производитель", "Расфасовка",
#                "Сентябрь", "Октябрь", "Ноябрь", "Итого кол-во", "Итого цена"]
#     ws.append(["Таблица продаж Минеральная вода"])  # Строка 1
#     ws.append(headers)  # Строка 2
#
#     # Данные (пример из PDF стр 1 - Сафронов)
#     data = [
#         [1, "Магниевая", "Россия", 0.2, 18, 15, 69, 102, 511938],
#         [2, "Магниевая", "Россия", 0.5, 24, 80, 65, 169, 939302],
#         [3, "Магниевая", "Россия", 1.0, 99, 61, 93, 253, 1312311],
#         [4, "Железистая", "Китай", 0.2, 64, 96, 82, 242, 1214598],
#         [5, "Железистая", "Германия", 1.5, 77, 82, 85, 244, 1401048],
#         [6, "Кальциевая", "Беларусь", 0.5, 52, 36, 9, 97, 539126],
#         [7, "Натриевая", "Россия", 1.0, 53, 14, 41, 108, 560196],
#         [8, "Натриевая", "Китай", 1.5, 44, 57, 2, 103, 591426],
#         # Добавим еще данных для наглядности
#         [9, "Кальциевая", "Россия", 0.5, 30, 40, 50, 120, 600000],
#         [10, "Магниевая", "Беларусь", 1.5, 10, 20, 30, 60, 300000],
#     ]
#
#     for row in data:
#         ws.append(row)
#
#     wb.save(INPUT_FILE)
#     print("Тестовый файл создан.")


# if not os.path.exists(INPUT_FILE):
#     create_dummy_input()

# ==========================================
# ЧАСТЬ I
# ==========================================
print("Выполнение Части I...")

# 1-3. Копирование файла
shutil.copy(INPUT_FILE, os.path.join(WORK_DIR, OUTPUT_FILE_MAIN))
main_path = os.path.join(WORK_DIR, OUTPUT_FILE_MAIN)

# Загружаем книгу
wb = load_workbook(main_path)
ws_orig = wb.active  # Предполагаем, что это Лист1

# 6. Переименовать Лист1
ws_orig.title = "Исходная таблица"

# 7. Окрасить ярлычок Листа 2 (создадим, если нет, или используем существующий)
if "Лист2" not in wb.sheetnames:
    ws_sheet2 = wb.create_sheet("Лист2")
else:
    ws_sheet2 = wb["Лист2"]
ws_sheet2.sheet_properties.tabColor = "FF0000"  # Красный

# 8-9. Вставить новый лист "Связи"
if "Связи" in wb.sheetnames:
    del wb["Связи"]
ws_links = wb.create_sheet("Связи")

# 10. Скопировать "Таблицу продаж" на лист "Связи" (без формул, как значения)
# Читаем данные через pandas для удобства
df = pd.read_excel(INPUT_FILE, header=1)  # Заголовок во 2 строке
# Удаляем пустые строки если есть
df = df.dropna(how='all')

# Записываем данные на лист "Связи"
for r in dataframe_to_rows(df, index=False, header=True):
    ws_links.append(r)

wb.save(main_path)

# 11. Отсортировать таблицу по: Производитель, Расфасовка, Вид товара (Товар)
# Используем Pandas для сортировки
df_sorted = df.sort_values(by=['Производитель', 'Расфасовка', 'Товар (разновидность)'])

# Очищаем лист Связи и записываем отсортированные данные
ws_links.delete_rows(1, ws_links.max_row)
# Добавляем заголовки
headers = list(df.columns)
ws_links.append(headers)
for r in dataframe_to_rows(df_sorted, index=False, header=False):
    ws_links.append(r)

wb.save(main_path)

# 12-13. Создание файла "Производители.xlsx" и листов по производителям
prod_wb = Workbook()
# Удаляем дефолтный лист
prod_wb.remove(prod_wb.active)

producers = df_sorted['Производитель'].unique()
prod_file_path = os.path.join(WORK_DIR, OUTPUT_FILE_PROD)
# Полный абсолютный путь нужен для формул связей, но Excel любит относительные
# Для скрипта используем относительный путь в формуле, предполагая, что они в одной папке
abs_prod_path = os.path.abspath(prod_file_path)

for prod in producers:
    # 13. Данные по производителю
    prod_data = df_sorted[df_sorted['Производитель'] == prod]
    ws_p = prod_wb.create_sheet(title=str(prod))

    # Записываем заголовки и данные
    ws_p.append(headers)
    for r in dataframe_to_rows(prod_data, index=False, header=False):
        ws_p.append(r)

prod_wb.save(prod_file_path)

# 15. Связывание таблиц (Вставка формул в "Связи")
# Задание: Замените результаты продаж на листе "Связи" ссылками на файл "Производители"
# Колонки продаж: Сентябрь(E), Октябрь(F), Ноябрь(G), Итого(H), Цена(I) -> индексы 5,6,7,8,9 (в Excel E,F,G,H,I)
# В pandas df_sorted строки идут последовательно. В файле производителей они разбиты по листам.
# Нам нужно пройтись по df_sorted и сформировать формулу для каждой ячейки.

print("Создание связей...")
wb = load_workbook(main_path)
ws_links = wb["Связи"]

# Определяем индексы колонок для связывания (начиная с 1)
# E=5 (Сентябрь), F=6, G=7, H=8, I=9
cols_to_link = [5, 6, 7, 8, 9]

# Итератор для отслеживания строки внутри каждого листа производителя
prod_row_counters = {prod: 2 for prod in producers}  # Данные начинаются со 2 строки (1 - заголовок)

# Проходим по строкам листа "Связи" (пропуская заголовок)
for row_idx, row in enumerate(ws_links.iter_rows(min_row=2), start=2):
    # Получаем производителя из текущей строки (Колонка C = индекс 2)
    prod_name = row[2].value

    if prod_name in prod_row_counters:
        target_row = prod_row_counters[prod_name]

        for col_idx in cols_to_link:
            cell = row[col_idx - 1]  # -1 так как row - это кортеж ячеек
            col_letter = openpyxl.utils.get_column_letter(col_idx)

            # Формула вида: ='[Производители.xlsx]Россия'!E2
            # Примечание: Excel на Mac/Win может требовать полный путь, если файл закрыт.
            formula = f"='[{OUTPUT_FILE_PROD}]{prod_name}'!{col_letter}{target_row}"
            cell.value = formula

        prod_row_counters[prod_name] += 1

wb.save(main_path)

# 16. Отсортировать таблицу на листе "Связи" по № п/п (Колонка A)
# В openpyxl сортировка с формулами может быть опасной (формулы могут не сместиться).
# Но задание требует. Мы пересортируем данные в памяти, сохраняя формулы как строки.

# Считываем данные с формулами
data_with_formulas = []
for row in ws_links.iter_rows(values_only=False):
    row_data = []
    for cell in row:
        row_data.append(cell.value)
    data_with_formulas.append(row_data)

header = data_with_formulas[0]
body = data_with_formulas[1:]

# Сортируем body по 1-му элементу (№ п/п)
# Предполагаем, что № п/п - число
body.sort(key=lambda x: x[0] if x[0] is not None else 0)

# Перезаписываем
ws_links.delete_rows(1, ws_links.max_row)
ws_links.append(header)
for row_data in body:
    ws_links.append(row_data)

wb.save(main_path)
print("Часть I завершена.")

# ==========================================
# ЧАСТЬ II
# ==========================================
print("Выполнение Части II...")

# 19. Дайте листу название "Автофильтр"
# Задание говорит: скопируйте таблицу на новый лист.
# 18. После листа "Связи" вставьте лист... (в скрипте проще создать новый)
ws_filter = wb.copy_worksheet(ws_links)
ws_filter.title = "Автофильтр"

# 20. Только данные (без формул)
# Проходим и заменяем формулы на 0 (так как мы не можем вычислить внешние ссылки без открытия Excel).
# В реальной задаче лучше скопировать значения из df_sorted (отсортировав его по ID),
# так как Python не может вычислить результат формулы ='[file]sheet'!A1.
df_by_id = df.sort_values(by="№ п/п")

# Очищаем и пишем значения
ws_filter.delete_rows(1, ws_filter.max_row)
ws_filter.append(list(df_by_id.columns))
for r in dataframe_to_rows(df_by_id, index=False, header=False):
    ws_filter.append(r)

# 21. Поставьте автофильтр
ws_filter.auto_filter.ref = ws_filter.dimensions

# 22. Переименуйте Лист 3 в "Диаграммы"
if "Лист3" not in wb.sheetnames:
    ws_charts = wb.create_sheet("Диаграммы")
else:
    ws_charts = wb["Лист3"]
    ws_charts.title = "Диаграммы"

# 23. Графический анализ (Диаграммы)
print("Построение диаграмм...")

# Подготовка агрегированных данных для диаграмм
# Диаграммы строятся на основе данных. Разместим вспомогательные таблицы на листе Диаграммы.

# a) Точечный график (Объем продаж от расфасовки)
# Данные: Расфасовка, Итого кол-во
ws_charts["A1"] = "Данные для графика А"
ws_charts["A2"] = "Расфасовка"
ws_charts["B2"] = "Кол-во"

chart_a_data = df_by_id[['Расфасовка', 'Итого кол-во']].values.tolist()
for i, row in enumerate(chart_a_data):
    ws_charts.cell(row=3 + i, column=1, value=row[0])
    ws_charts.cell(row=3 + i, column=2, value=row[1])

scatter = ScatterChart()
scatter.title = "Объем продаж от расфасовки"
scatter.x_axis.title = "Расфасовка (л)"
scatter.y_axis.title = "Количество"
x_values = Reference(ws_charts, min_col=1, min_row=3, max_row=2 + len(chart_a_data))
y_values = Reference(ws_charts, min_col=2, min_row=3, max_row=2 + len(chart_a_data))
series = Series(y_values, x_values, title_from_data=False)
scatter.series.append(series)
ws_charts.add_chart(scatter, "D2")

# b) Круговая диаграмма (Зависимость проданного товара от его вида)
# Группируем по Товару
group_prod = df_by_id.groupby('Товар')['Итого кол-во'].sum().reset_index()

ws_charts["A20"] = "Данные для графика B"
ws_charts.append(["Товар", "Сумма"])
start_row_b = ws_charts.max_row
for r in dataframe_to_rows(group_prod, index=False, header=False):
    ws_charts.append(r)
end_row_b = ws_charts.max_row

pie = PieChart()
pie.title = "Доля продаж по видам товара"
labels = Reference(ws_charts, min_col=1, min_row=start_row_b, max_row=end_row_b)
data = Reference(ws_charts, min_col=2, min_row=start_row_b, max_row=end_row_b)
pie.add_data(data, titles_from_data=False)
pie.set_categories(labels)
ws_charts.add_chart(pie, "D20")

# c) Графическая (Line/Column) - Уровень продаж по временному периоду в зависимости от производителя
# Сложная структура, упростим: Сумма продаж (Итого кол-во) по производителям
group_man = df_by_id.groupby('Производитель')['Итого кол-во'].sum().reset_index()

ws_charts["A40"] = "Данные для графика C"
ws_charts.append(["Производитель", "Сумма"])
start_row_c = ws_charts.max_row
for r in dataframe_to_rows(group_man, index=False, header=False):
    ws_charts.append(r)
end_row_c = ws_charts.max_row

bar = BarChart()
bar.title = "Продажи по производителям"
cats = Reference(ws_charts, min_col=1, min_row=start_row_c, max_row=end_row_c)
data = Reference(ws_charts, min_col=2, min_row=start_row_c, max_row=end_row_c)
bar.add_data(data, titles_from_data=False)
bar.set_categories(cats)
ws_charts.add_chart(bar, "D40")

# Сохранение итогового файла
wb.save(main_path)

print("==========================================")
print(f"Готово! Результаты сохранены в папке: {WORK_DIR}")
print(f"1. Основной файл: {OUTPUT_FILE_MAIN}")
print(f"2. Файл связей: {OUTPUT_FILE_PROD}")
print("Примечание: При открытии Пр.раб.-2.xlsx Excel может попросить обновить связи.")
print("==========================================")