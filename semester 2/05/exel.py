import pandas as pd
import numpy as np

# Читаем данные, сгенерированные первым скриптом
df_float = pd.read_csv('data_float.csv')
df_int = pd.read_csv('data_int.csv')
df_pie = pd.read_csv('data_pie.csv')
df_discrete = pd.read_csv('data_var17.txt', sep='\t')

excel_file = 'Result_Charts.xlsx'

# Создаем Excel файл и writer
writer = pd.ExcelWriter(excel_file, engine='xlsxwriter')
workbook = writer.book

# --- 1. Лист с функцией (нецелые числа) ---
df_float.to_excel(writer, sheet_name='Float Data', index=False)
worksheet_float = writer.sheets['Float Data']
chart_line = workbook.add_chart({'type': 'scatter', 'subtype': 'smooth'})
chart_line.add_series({
    'name':       'f(x)',
    'categories': ['Float Data', 1, 0, len(df_float), 0],
    'values':     ['Float Data', 1, 1, len(df_float), 1],
})
chart_line.set_title({'name': 'a) Линейный график функции'})
chart_line.set_x_axis({'name': 'x'})
chart_line.set_y_axis({'name': 'f(x)'})
worksheet_float.insert_chart('D2', chart_line)

# --- 2. Лист с функцией (целые числа, Комбинированная диаграмма) ---
df_int.to_excel(writer, sheet_name='Int Data', index=False)
worksheet_int = writer.sheets['Int Data']

# Создаем столбчатую диаграмму
chart_col = workbook.add_chart({'type': 'column'})
chart_col.add_series({
    'name':       'Столбцы',
    'categories':['Int Data', 1, 0, len(df_int), 0],
    'values':['Int Data', 1, 1, len(df_int), 1],
})

# Создаем линейную диаграмму для наложения
chart_line2 = workbook.add_chart({'type': 'line'})
chart_line2.add_series({
    'name':       'Линия',
    'categories':['Int Data', 1, 0, len(df_int), 0],
    'values':['Int Data', 1, 1, len(df_int), 1],
    'line':       {'color': 'red'},
    'marker':     {'type': 'circle', 'size': 5}
})

# Комбинируем
chart_col.combine(chart_line2)
chart_col.set_title({'name': 'b) Столбчатая + Линейная'})
worksheet_int.insert_chart('D2', chart_col)

# --- 3. Лист с круговой диаграммой ---
df_pie.to_excel(writer, sheet_name='Pie Data', index=False)
worksheet_pie = writer.sheets['Pie Data']
chart_pie = workbook.add_chart({'type': 'pie'})
chart_pie.add_series({
    'name':       'Доля рынка',
    'categories':['Pie Data', 1, 0, len(df_pie), 0],
    'values':['Pie Data', 1, 1, len(df_pie), 1],
    'data_labels': {'percentage': True}
})
chart_pie.set_title({'name': 'c) Рынок шампуней'})
worksheet_pie.insert_chart('D2', chart_pie)

# --- 4. Проверка Задания 5 в Excel (Дискретные данные) ---
df_discrete.to_excel(writer, sheet_name='Discrete Data', index=False)
worksheet_disc = writer.sheets['Discrete Data']
chart_disc = workbook.add_chart({'type': 'scatter', 'subtype': 'straight_with_markers'})
chart_disc.add_series({
    'name':       'Таблица 17',
    'categories':['Discrete Data', 1, 0, len(df_discrete), 0],
    'values':['Discrete Data', 1, 1, len(df_discrete), 1],
    'marker':     {'type': 'circle'}
})
chart_disc.set_title({'name': 'Проверка задачи №5'})
chart_disc.set_x_axis({'name': 'X'})
chart_disc.set_y_axis({'name': 'Y'})
worksheet_disc.insert_chart('D2', chart_disc)

writer.close()
print(f"Готово! Все графики успешно построены в файле {excel_file}. Откройте его для проверки.")