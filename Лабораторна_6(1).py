
numbers = [10, 25, 30, 45, 50, 65]

numbers.insert(1, -5)

print("Мінімальний елемент:", min(numbers))
print("Максимальний елемент:", max(numbers))

# Додаємо список [1,2,3] починаючи з третього елементу (індекс 2)
numbers[2:2] = [1, 2, 3]

numbers.append("Петренко Олексій")

print("Кількість елементів:", len(numbers))
print("Весь список:", numbers)