import numpy as np
from scipy.stats import norm

n = 5_000
m = 10_000

# Генеруємо вибірки
X = np.random.exponential(scale=1, size=(n,))
Y = np.random.exponential(scale=1/1.2, size=(m,))

# Формуємо варіаційний ряд вибірки X
R = np.sort(X)

a = 0 # Кількість пустих блоків

# Обчислюємо кількість пустих блоків
for i in range(n-1):
    isEmptyBlock = not np.any((R[i] <= Y) & (Y <= R[i+1]))
    a += isEmptyBlock

# Обчислюємо статистику
rho = m / n
a_n = n / (1 + rho)
z = norm.ppf(1 - 0.05 / 2)

# Обчислюємо критичну область
critical_value = n / (1 + rho) + (np.sqrt(n) * rho * z) / ((1 + rho) ** (1.5))

if a > critical_value:
    print("Distributions are different")
else:
    print("Distributions are the same")