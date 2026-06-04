import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

# Определение параметров
x0, y0 = -2, -3
p = 4

# Создание графика
fig, ax = plt.subplots(figsize=(10, 8))

# Генерация точек для параболы
# Из уравнения: (y + 3)^2 = 16(x + 2) => x = (y + 3)^2/16 - 2
y_vals = np.linspace(-15, 9, 400)
x_vals = (y_vals + 3)**2 / 16 - 2

# Построение параболы
ax.plot(x_vals, y_vals, 'b-', linewidth=2, label='Парабола: $y^2 - 16x + 6y - 23 = 0$')

# Вершина
ax.plot(x0, y0, 'ro', markersize=8, label=f'Вершина $O({x0},{y0})$')

# Фокус
focus_x, focus_y = x0 + p, y0
ax.plot(focus_x, focus_y, 'go', markersize=8, label=f'Фокус $F({focus_x},{focus_y})$')

# Ось симметрии
ax.axhline(y=y0, color='gray', linestyle='--', alpha=0.7, label=f'Ось симметрии: $y = {y0}$')

# Директриса
directrix_x = x0 - p
ax.axvline(x=directrix_x, color='orange', linestyle='--', alpha=0.7, label=f'Директриса: $x = {directrix_x}$')

# Настройка графика
ax.set_xlabel('x', fontsize=12)
ax.set_ylabel('y', fontsize=12)
ax.set_title('Парабола: $y^2 - 16x + 6y - 23 = 0$', fontsize=14)

# Сетка и легенда
ax.grid(True, alpha=0.3)
ax.legend(loc='upper right', fontsize=10)
ax.set_aspect('equal')

# Настройка пределов осей
ax.set_xlim(-10, 10)
ax.set_ylim(-15, 10)

# Подписи
ax.text(x0, y0+0.5, f'({x0},{y0})', fontsize=10, ha='center')
ax.text(focus_x, focus_y+0.5, f'({focus_x},{focus_y})', fontsize=10, ha='center')

plt.tight_layout()
plt.savefig('parabola_plot.png', dpi=300, bbox_inches='tight')
plt.show()