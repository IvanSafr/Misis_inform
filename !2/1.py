import numpy as np
import matplotlib.pyplot as plt

# Создаем сетку значений x и y
x = np.linspace(-5, 5, 400)
y = np.linspace(-5, 5, 400)
X, Y = np.meshgrid(x, y)

# Условие 1: Подкоренное выражение гиперболы >= 0
# (эквивалентно x^2/9 - y^2/4 <= 1)
condition1 = 1 - (X**2 / 9) + (Y**2 / 4) >= 0

# Условие 2: Подкоренное выражение полосы >= 0
# (эквивалентно |x| <= 4)
condition2 = 16 - X**2 >= 0

# Область определения - это пересечение обоих условий
domain = condition1 & condition2

# Визуализация
plt.figure(figsize=(8, 8))
plt.imshow(domain.astype(int), extent=(x.min(), x.max(), y.min(), y.max()),
           origin='lower', cmap='Blues', alpha=0.3)

# Рисуем границы для наглядности
# 1. Гипербола
plt.contour(X, Y, (X**2 / 9) - (Y**2 / 4), levels=[1], colors='red', linestyles='--')
# 2. Вертикальные прямые x = -4 и x = 4
plt.axvline(x=-4, color='black', linestyle='-')
plt.axvline(x=4, color='black', linestyle='-')

plt.title('Область определения задачи 1.16')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True, linestyle=':', alpha=0.6)
plt.axhline(0, color='black', lw=1)
plt.axvline(0, color='black', lw=1)

plt.legend(['x = ±4', 'x²/9 - y²/4 = 1'], loc='upper right')
plt.show()