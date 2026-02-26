import math

x = 4.0

y = math.atan(x) + (math.exp(0.6 * x - 1) - math.sqrt((x + 6.1)**3)) / (math.log(x) + math.tan(x)**2)
print(f"Результат: {y}")