n = int(input("Введіть кількість членів послідовності N: "))
total_sum = 0

for i in range(1, n + 1):
    print(f"--- Крок {i} ---")
    a = float(input(f"Введіть значення a для {i}-го члена: "))
    b = float(input(f"Введіть значення b для {i}-го члена: "))
    
    # Обчислення за формулою
    numerator = a**2 + b**2
    denominator = a**2 + b**2 + 4
    g_ab = numerator / denominator
    
    total_sum += g_ab
    print(f"Значення g(a,b) на цьому кроці: {g_ab:.4f}")

print("-" * 20)
print(f"Загальна сума перших {n} членів: {total_sum:.4f}")