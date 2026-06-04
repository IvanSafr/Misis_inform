import matplotlib.pyplot as plt

# Создаем график
fig, ax = plt.subplots(figsize=(8, 8))

# Точка P(3, -1)
x_point, y_point = 3, -1

# Рисуем точку
ax.plot(x_point, y_point, 'ro', markersize=12, label=f'Точка P({x_point},{y_point})')

# Настройки графика
ax.set_xlabel('x', fontsize=12)
ax.set_ylabel('y', fontsize=12)
ax.set_title('$2x^2 + 3y^2 - 12x + 6y + 21 = 0$', fontsize=14)
ax.grid(True, alpha=0.3)
ax.legend(loc='best', fontsize=10)
ax.set_aspect('equal')

# Пределы осей
ax.set_xlim(0, 6)
ax.set_ylim(-3, 1)

# Подпись точки
ax.text(x_point + 0.1, y_point + 0.1, f'P({x_point},{y_point})',
        fontsize=12, ha='left', va='bottom')

# Добавляем координатные оси
ax.axhline(y=0, color='k', linestyle='-', linewidth=0.5, alpha=0.5)
ax.axvline(x=0, color='k', linestyle='-', linewidth=0.5, alpha=0.5)

plt.tight_layout()
plt.savefig('point_plot.png', dpi=300, bbox_inches='tight')
plt.show()