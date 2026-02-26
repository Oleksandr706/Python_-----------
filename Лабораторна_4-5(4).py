import math

a = float(input("Введіть початок a: "))
b = float(input("Введіть кінець b: "))
h = float(input("Введіть крок h: "))

x = a

print("Результати (x та y):")

while x <= b:
    # Проста перевірка ОДЗ
    if x == 0 or x < -3:
        print(x, "| Помилка: x поза ОДЗ")
        break
    
    
    y = 1/x + math.sqrt(x + 3) + 6
    print(x, "|", y)
    
    x = x + h