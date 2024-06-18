
import numpy as np
from scipy.interpolate import BarycentricInterpolator

# Данные
xi = np.array([0.1 * np.pi, 0.2 * np.pi, 0.3 * np.pi, 0.4 * np.pi])
yi = np.cos(xi)

# Интерполяционный многочлен Ньютона
newton_poly = BarycentricInterpolator(xi, yi)

# Значение в точке x* = 0.25π
x_star = 0.25 * np.pi
y_star = newton_poly(x_star)

# Точное значение функции
y_exact = np.cos(x_star)

# Погрешность
error = np.abs(y_star - y_exact)

print(f"Значение интерполяции в точке x* = {x_star}: {y_star}")
print(f"Точное значение функции в точке x* = {x_star}: {y_exact}")
print(f"Погрешность интерполяции: {error}")
