a = float(input("Сторона a: "))
b = float(input("Сторона b: "))
c = float(input("Сторона c: "))

# Перевірка на існування трикутника
if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Рівносторонній")
    elif a == b or b == c or a == c:
        print("Рівнобедрений")
    else:
        print("Довільний трикутник")
else:
    print("Трикутник не існує")