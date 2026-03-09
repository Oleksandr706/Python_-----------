str_info = "Олександр, група КН-3, спеціальність 122"
print("Початковий рядок: ", str_info)

# Виводиться тільки назву групи
parts = str_info.split(", ")
print("Назва групи:", parts[1])

# Заміна імені 
str_info = str_info.replace("Олександр", "Юрій")
print("Змінений рядок:", str_info)

# Розподіл по пробілу та кількість слів 
words = str_info.split()
print("Кількість слів:", len(words))