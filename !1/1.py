import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(10, 8))

# Гипербола: (y+1)^2/100 - (x-1)^2/144 = 1
# Верхняя ветвь: y = -1 + 10*sqrt(1 + (x-1)^2/144)
# Нижняя ветвь: y = -1 - 10*sqrt(1 + (x-1)^2/144)

x = np.linspace(-20, 22, 400)
y_upper = -1 + 10*np.sqrt(1 + (x-1)**2/144)
y_lower = -1 - 10*np.sqrt(1 + (x-1)**2/144)

# Асимптоты
y_asymp1 = -1 + (5/6)*(x-1)
y_asymp2 = -1 - (5/6)*(x-1)

ax.plot(x, y_upper, 'r-', linewidth=2, label='Верхняя ветвь гиперболы')
ax.plot(x, y_lower, 'r-', linewidth=2, label='Нижняя ветвь гиперболы')
ax.plot(x, y_asymp1, 'b--', label='Асимптота 1: y+1=5/6(x-1)')
ax.plot(x, y_asymp2, 'b--', label='Асимптота 2: y+1=-5/6(x-1)')

# Особые точки
points = [(1, -1), (1, -11), (1, 9), (1, -16.62), (1, 14.62)]
labels = ["O'(1,-1)", "A₁(1,-11)", "A₂(1,9)", "F₁(1,-16.6)", "F₂(1,14.6)"]
colors = ['red', 'green', 'green', 'orange', 'orange']

for (px, py), label, color in zip(points, labels, colors):
    ax.plot(px, py, 'o', color=color, markersize=8)
    ax.text(px+0.5, py, label, fontsize=10)

# Оси
ax.axhline(y=-1, color='gray', linestyle=':', label='Мнимая ось: y=-1')
ax.axvline(x=1, color='gray', linestyle=':', label='Действительная ось: x=1')

ax.set_xlim(-15, 17)
ax.set_ylim(-20, 20)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Гипербола: 25x² - 36y² - 50x - 72y + 3589 = 0')
ax.grid(True, alpha=0.3)
ax.legend()
ax.set_aspect('equal')
plt.tight_layout()
plt.savefig('hyperbola.png', dpi=300)
plt.show()