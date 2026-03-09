users = ["Mark", "Tom", "Bob", "Alice", "Tom", "Bill", "Tom", "Alex", "Shaun", "Mark"]

print("Tom зустрічається:", users.count("Tom"))
print("Mark зустрічається:", users.count("Mark"))
print("Alice зустрічається:", users.count("Alice"))
print("John зустрічається:", users.count("John"))

# Вилучається третій елемент 
users.pop(2)

if "Tom" in users:
    users.remove("Tom")

print("Змінений список users:", users)