N = int(input("Введіть розмір таблиці N (2 <= N < 99): "))

for i in range(1, N + 1):
    row_value = i * 100 + 10  # Початкове значення для кожного рядка (110, 210...)
    for j in range(1, N + 1):
        if j % 2 != 0:
            print(f"{row_value}", end=" ")
            row_value += 20  # Збільшуємо число для наступної непарної позиції
        else:
            print("0", end=" ")
    print()  # Перехід на новий рядок